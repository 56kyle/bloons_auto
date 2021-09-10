from abc import ABC

import collections
import frida.core
import mouse
import pymem.ressources.structure
import numpy as np

from memory import Hook, ScriptInfo, MissingKwargError
from pymem import Pymem
from pymem.ressources.structure import MODULEINFO
from typing import Union


Region = collections.namedtuple('Region', 'xi yi xf yf')
#var getCursorPositionPointer = ptr("{PlaceableHook.get_cursor_offset}");
#var getCursorPosition = new NativeFunction(getCursorPositionPointer, "void", pointer);
#var cursorVector2 = getCursorPosition();


def load_placeable_script(session: frida.core.Session, game_assembly: pymem.ressources.structure.MODULEINFO):
    placeable_hook = PlaceableHook(
        address=str(int(game_assembly.lpBaseOfDll + PlaceableHook.offset)),
        on_enter='''
        ''',
        on_leave=f'''
            var cursorXPointer = cursorVector2.add("0x10")
            var cursorYPointer = cursorVector2.add("0x14")
            var x = cursorXPointer.readFloat();
            var y = cursorYPointer.readFloat();
            var coordinates = [x, y];
            send(x);
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
        self.location = None
        self.checkable_locations = Region(32, 36, 1600, 1050)
        self.checked_locations = np.full((1080, 1920), False)
        self.placeable_locations = np.full((1080, 1920), False)
        self.btd6 = Pymem('BloonsTD6.exe')
        self.game_assembly = game_assembly

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
        if payload == '0x0':
            self.placeable = False
            self.location = mouse.get_position()
        elif payload == '0x1':
            self.placeable = True
            self.location = mouse.get_position()
        else:
            self.location = None








