import keyboard
import time

from tower import Tower, Point
from typing import Union, Iterable
from config import keybinds


class Map:
    name = ''
    difficulty = ''
    page = 0
    placement = []

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def point_to_map(cls, location: Union[Point, Iterable]):
        location = Tower.coerce_to_point(location)
        if 340 < location.x < 742:
            x = 0
        elif 742 < location.x < 1184:
            x = 1
        elif 1184 < location.x < 1600:
            x = 2
        else:
            raise Exception('Point.x outside of acceptable ranges')

        if 100 < location.y < 428:
            y = 0
        elif 428 < location.y < 740:
            y = 1
        else:
            raise Exception('Point.y outside of acceptable ranges')
        return x, y

    @classmethod
    def is_round_over(cls):
        pass

    @classmethod
    def handle_insta_monkey_popup(cls):
        return True

    @classmethod
    def start(cls):
        keyboard.press_and_release(keybinds['play'], .2)
        time.sleep(.1)

    @classmethod
    def play_collection(cls):
        raise NotImplementedError

    @classmethod
    def toggle_fast_forward(cls):
        keyboard.press_and_release(keybinds['fast_forward'], .2)
        time.sleep(.1)



