from abc import ABC

import frida.core
import pymem.ressources.structure

from memory import Hook, ScriptInfo, MissingKwargError
from typing import Union


def load_placeable_script(session: frida.core.Session, game_assembly: pymem.ressources.structure.MODULEINFO):
    placeable_hook = PlaceableHook(
        address=str(int(game_assembly.lpBaseOfDll + PlaceableHook.offset)),
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

    def on_message(self, message, data):
        payload = data.get('payload')
        print(payload)






