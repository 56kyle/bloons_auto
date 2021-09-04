
from maps import *
from tower import Tower, Point

from towers import *
from map import Map

import mouse
import keyboard
import pyscreeze
import time
import win32gui


def give_info(*args):
    x, y = mouse.get_position()
    img = pyscreeze.screenshot()
    win = win32gui.GetActiveWindow()
    keyboard.press_and_release(DartMonkey.keybind, .2)
    print('===============================')
    print('= Can Place Setup             =')
    print('===============================')
    can_place_setup = DartMonkey.can_place(Point(x, y), img)
    print(f'= Result - {can_place_setup}')
    print('===============================')
    DartMonkey.deselect()
    time.sleep(1)
    print('===============================')
    print('= Can Place Not Setup         =')
    print('===============================')
    can_place_new = DartMonkey.can_place(Point(x, y))
    print(f'= Result - {can_place_new}')
    print('===============================')


if __name__ == '__main__':
    keyboard.on_press_key('control', give_info)
    while True:
        pass
