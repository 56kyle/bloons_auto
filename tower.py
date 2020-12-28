import mouse
import keyboard
import pyscreeze
import collections
import time
from config import keybinds

# Various usefull types
Point = collections.namedtuple('Point', 'x y')
Color = collections.namedtuple('Color', 'r g b')
Pixel = collections.namedtuple('Pixel', 'point color')

# Targeting Types
FIRST = 1000
LAST = 1001
CLOSE = 1002
STRONG = 1003
FAR = 1004
SMART = 1005
SET_TARGET = 1006
FOLLOW_MOUSE = 1007
LOCKED_IN_PLACE = 1008
PATROL_POINTS = 1009
CIRCLE = 1010
FIGURE_INFINITE = 1011
FIGURE_EIGHT = 1012
WINGMONKEY = 1013
ELITE = 1014


class Tower:
    """Base class for all towers"""
    target_type_button = (222, 374)

    def __init__(self, **kwargs):
        self.location = kwargs.get('location')
        self.name = kwargs.get('name')
        self.range = kwargs.get('range')
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.keybind = keybinds[self.name]
        self.price = kwargs.get('price')
        self.value = self.price
        self.upgrades = kwargs.get('upgrades')
        if self.upgrades:
            if self.upgrades[0] > 0:
                self.upgrade(1, self.upgrades[0])
            if self.upgrades[1] > 0:
                self.upgrade(2, self.upgrades[1])
            if self.upgrades[2] > 0:
                self.upgrade(3, self.upgrades[2])
        else:
            self.upgrades = [0, 0, 0]
        self.place()

    def can_place(self, location):
        mouse.move(location.x, location.y)
        if location.x > 1100:
            measuring_point = Point(location.x - (self.range - 2), location.y)
        else:
            measuring_point = Point(location.x + (self.range - 2), location.y)

        before = pyscreeze.pixel(measuring_point.x, measuring_point.y)
        keyboard.press_and_release(self.keybind, .1)
        after = pyscreeze.pixel(measuring_point.x, measuring_point.y)
        if (after[0] - before[0]) >= 8:
            return False
        else:
            return True

    def place(self):
        if self.can_place(self.location):
            mouse.click()
            return True
        return False

    def deselect(self):
        keyboard.press_and_release("escape", .1)

    def select(self):
        mouse.move(*self.location)
        mouse.click()
        time.sleep(.1)

    def upgrade(self, pathway, times=1):
        self.select()
        for _ in range(times):
            keyboard.press_and_release(keybinds['upgrade_path_' + str(pathway)], .1)
            time.sleep(.1)

    def relocate_lock(self, location):
        mouse.move(*self.target_type_button)
        mouse.click()
        mouse.move(*location)
        mouse.click()

    def __del__(self):
        self.select()
        keyboard.press_and_release(keybinds['sell'], .1)


if __name__ == '__main__':
    time.sleep(5)



