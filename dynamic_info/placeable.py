from abc import ABC

import collections
import frida.core
import mouse
import pymem.ressources.structure
import numpy as np

from memory import Hook, ScriptInfo, MissingKwargError
from pymem import Pymem
from typing import Union


Region = collections.namedtuple('Region', 'xi yi xf yf')


def load_placeable_script(session: frida.core.Session, game_assembly: pymem.ressources.structure.MODULEINFO):
    placeable_hook = PlaceableHook(
        address=str(int(game_assembly.lpBaseOfDll + PlaceableHook.offset)),
        on_enter='send(args[0]);send(args[1]);send(args[2]);send(args[3]);send(args[4]);',
        on_leave='send(args);',
    )
    placeable_script = session.create_script(str(placeable_hook))
    placeable_script.on('message', placeable_hook.on_message)
    placeable_script.load()
    placeable_hook.script = placeable_script
    return placeable_hook


class PlaceableHook(Hook, ABC):
    offset = 0x634FA0
    loader = load_placeable_script
    script = None

    def __init__(self, address: Union[str, int, None] = None, **kwargs):
        super(PlaceableHook, self).__init__(address, **kwargs)
        self.placeable = False
        self.location = None
        self.checkable_locations = Region(32, 36, 1600, 1050)
        self.checked_locations = np.full((1080, 1920), False)
        self.placeable_locations = np.full((1080, 1920), False)
        self.btd6 = Pymem('BloonsTD6.exe')

    def on_message(self, message, data):
        if len(message.get('payload')) > 3:
            read_bytes = self.btd6.read_bytes(message.get('payload').get('rsp'), 8)
            print(read_bytes)
            print(self.btd6.read_bytes(int(message.get('payload'), 0), 4))
            print(message)
        elif message == 'on_leave':
            payload = data.get('payload')
            print(payload)
            if payload == '0x0':
                self.placeable = False
                self.location = mouse.get_position()
            elif payload == '0x1':
                self.placeable = True
                self.location = mouse.get_position()
            else:
                self.location = None
        else:
            print(message)
            print(data)








