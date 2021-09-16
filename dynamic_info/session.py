
import ctypes
import frida
import keyboard
import mouse
import time
import sys

from abc import ABC
from memory import Hook, MissingKwargError, ScriptInfo
from pymem import Pymem
from pymem.exception import WinAPIError, ProcessNotFound
from pymem.process import *
from dynamic_info import PlaceableHook
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

    @property
    def location(self):
        try:
            return self.hooks['PlaceableHook'].location
        except AttributeError:
            return None

    def output_values(self):
        with open('./contants.py', 'w') as file:
            file.write(f'hex_to_x = {self.hooks["PlaceableHook"].x_values}\nhex_to_y = {self.hooks["PlaceableHook"].y_values}\n')


def get_placeable_const_info(btd6_session):
    mouse.move(0, 0)
    keyboard.press_and_release('a', .2)
    pairs = []
    i = 0
    for x in range(30, 1600):
        mouse.move(x, 540)
        while btd6_session.location != (x, 540):
            pass
        if i > 50:
            btd6_session.output_values()
            i = 0
        else:
            i += 1

    i = 0
    for y in range(0, 1080):
        mouse.move(800, y)
        while btd6_session.location != (800, y):
            pass
        if i > 30:
            btd6_session.output_values()
            i = 0
        else:
            i += 1


if __name__ == '__main__':
    btd6_session = Btd6Session(hooks=[PlaceableHook])
    while True:
        pass
