
from maps import *
from map import Map

from towers import *
from tower import Tower

from exceptions import *

import mouse
import keyboard
import time


class Recorder:
    def __init__(self):
        pass

    def mark_click(self, *args):
        marker = time.time()
        location = mouse.get_position()
        print()

    def mark_press(self):




if __name__ == '__main__':
    recorder = Recorder()
    for tower in ALL:
        keyboard.on_press_key(tower.keybind())
    mouse.on_click(recorder.)




