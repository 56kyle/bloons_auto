
import ctypes
import frida
import sys

from abc import ABC
from memory import Hook, MissingKwargError, ScriptInfo
from pymem import Pymem
from pymem.exception import WinAPIError, ProcessNotFound
from pymem.process import module_from_name
from typing import Union, Callable, SupportsInt


class Btd6Session:
    def __init__(self, hooks: [Hook], **kwargs):
        self.session = frida.attach('BloonsTD6.exe')
        self.btd6 = Pymem('BloonsTD6.exe')
        self.game_assembly = None
        while not self.game_assembly:
            try:
                self.game_assembly = module_from_name(ctypes.c_void_p(self.btd6.process_handle), 'GameAssembly.dll')
            except ModuleNotFoundError:
                pass
        self.hooks = {}
        for hook_cls in hooks:
            hook = hook_cls.loader(self.session, self.game_assembly)
            self.hooks[hook_cls.__name__] = hook
        sys.stdin.read()

    @property
    def money(self):
        try:
            return self.hooks['MoneyHook'].money
        except AttributeError:
            return 0

    @property
    def placeable(self):
        try:
            return self.hooks['PlaceableHook'].placeable
        except AttributeError:
            return False
