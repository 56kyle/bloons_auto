from abc import ABC

import collections
import frida.core
import mouse
import struct
import time
import pymem.ressources.structure
import numpy as np

from .const import hex_to_x, hex_to_y
from memory import Hook, ScriptInfo, MissingKwargError
from pymem import Pymem
from pymem.ressources.structure import MODULEINFO
from typing import Union


Region = collections.namedtuple('Region', 'xi yi xf yf')


def load_placeable_script(session: frida.core.Session, game_assembly: pymem.ressources.structure.MODULEINFO):
    # args[1] = at: Assets.Scripts.Simulation.SMath.Vector2
    # args[2] = at: Assets.Scripts.Models.Towers.TowerModel
    placeable_hook = PlaceableHook(
        address=str(int(game_assembly.lpBaseOfDll + PlaceableHook.offset)),
        on_enter='''
            this.vec_2 = args[1];
        ''',
        on_leave='''
            send(this.vec_2.toString() + " " + args);
        ''',
        game_assembly=game_assembly,
    )
    placeable_script = session.create_script(str(placeable_hook))
    placeable_script.on('message', placeable_hook.on_message)
    placeable_script.load()
    placeable_hook.script = placeable_script
    return placeable_hook


class PlaceableHook(Hook, ABC):
    offset = 0x634FA0
    get_cursor_offset = 0x5D59A0
    loader = load_placeable_script
    script = None

    def __init__(self, address: Union[str, int], game_assembly: MODULEINFO, **kwargs):
        super(PlaceableHook, self).__init__(address, **kwargs)
        self.placeable = False
        self.location = []
        self.btd6 = Pymem('BloonsTD6.exe')
        self.game_assembly = game_assembly
        self.x_values = hex_to_x
        self.y_values = hex_to_y
        self.np_placeable = np.full((1080, 1920), False)
        self.np_checked = np.full((1080, 1920), False)

    def code(self, address) -> str:
        on_enter_text = self.on_enter_container()
        on_leave_text = self.on_leave_container()
        return f'''
        Interceptor.attach(ptr("{address}"), {{
            {on_enter_text}
            {on_leave_text}
        }});
        ''' if on_enter_text or on_leave_text else ''

    def on_message(self, message, data):
        payload = message.get('payload')
        hex_y = payload[2:10]
        hex_x = payload[10:18]
        value = payload.split(' ')[1]
        x = hex_to_x.get(hex_x)
        y = hex_to_y.get(hex_y)
        if x and y:
            self.location = (x, y)
            self.placeable = value == '0x1'
            self.np_placeable[y, x] = self.placeable
            self.np_checked[y, x] = True


