import frida.core
import pymem.ressources.structure

from abc import ABC
from memory import Hook, ScriptInfo, MissingKwargError
from pymem import Pymem
from pymem.exception import WinAPIError
from typing import Union


def load_money_script(session: frida.core.Session, game_assembly: pymem.ressources.structure.MODULEINFO, **kwargs):
    money_hook = MoneyHook(
        address=str(int(game_assembly.lpBaseOfDll + MoneyHook.offset)),
        # on_enter='send(this.context);',
        on_leave='send(this.context);',
    )
    money_script = session.create_script(str(money_hook))
    money_script.on('message', money_hook.on_message)
    money_script.load()
    return money_hook


class MoneyHook(Hook, ABC):
    offset = 0x368380
    loader = load_money_script

    def __init__(self, address: Union[str, int, None] = None, **kwargs):
        super(MoneyHook, self).__init__(address, **kwargs)
        self.value = None
        self.btd6 = Pymem("BloonsTD6.exe")
        self.money_address = None

    def on_message(self, message, data):
        context = message.get('payload')
        if context:
            if context.get('r12') == '0x0':
                return
            print(message)
            self.money_address = int(context.get('rbx'), 0) + 0x28
            try:
                value = self.btd6.read_double(self.money_address)
                self.value = value if value > 1 else self.value
            except WinAPIError:
                pass

            print(f'address - {hex(self.money_address)}')
            print(f'money - {self.value}')











