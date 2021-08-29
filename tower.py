import mouse
import keyboard
from window_input import Window, Key
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

sizes = {
    'small': (65, 57),
    'medium': (75, 65),
    'large': (87, 75),
    'xl': (119, 103),
}

class Tower:
    """Base class for all towers"""
    name = None
    range = None
    height = None
    width = None
    keybind = None
    aquatic = False
    size = None

    target_type_button = (222, 374)
    tower_deselect_button = (398, 77)

    tower_panel_background = (40, 110)
    tower_panel_background_color = (193, 152, 95)

    tower_placement_button = (1578, 139)
    tower_placement_button_color = (255, 62, 0)

    def __init__(self, **kwargs):
        self.window = Window()
        self.location = kwargs.get('location')
        if self.location:
            try:
                self.location.x = self.location.x
            except AttributeError:
                self.location = Point(*self.location)
        else:
            self.location = Point(*mouse.get_position())

        self.keybind = keybinds.get(self.name)
        self.price = kwargs.get('price')
        self.value = self.price
        self.place()
        upgrades = kwargs.get('upgrades')
        self.upgrades = [0, 0, 0]
        if upgrades:
            self.assign_upgrades(upgrades)

    def __del__(self):
        self.select()
        keyboard.press_and_release(keybinds['sell'], .1)

    @classmethod
    def can_place(cls, location):
        window = Window()
        cls.keybind = keybinds[cls.name]
        while mouse.get_position() != (location.x, location.y):
            mouse.move(location.x, location.y)

        if location.x > 1100:
            measuring_point = Point(location.x - (cls.range - 2), location.y)
        else:
            measuring_point = Point(location.x + (cls.range - 2), location.y)

        before = window.pixel(measuring_point.x, measuring_point.y)
        keyboard.press_and_release(cls.keybind)
        after = window.pixel(measuring_point.x, measuring_point.y)
        time.sleep(.05)
        cls.deselect()
        if (after[0] - before[0]) >= 8:
            return False
        else:
            return True

    def place(self):
        if self.can_place(self.location):
            mouse.move(*self.location)
            time.sleep(.0)
            keyboard.press_and_release(self.keybind, .1)
            time.sleep(.1)
            mouse.click()
            return True
        return False

    @staticmethod
    def deselect():
        keyboard.press_and_release('escape', .1)
        '''
        x, y = Tower.tower_placement_button
        mouse.move(x + 10, y - 10)
        time.sleep(.2)
        mouse.click()
        time.sleep(.1)
        '''

    def select(self):
        mouse.move(*self.location)
        time.sleep(.1)
        mouse.click()
        time.sleep(.1)

    def assign_upgrades(self, desired_upgrades):
        self.select()
        for i in range(3):
            for _ in range(desired_upgrades[i] - self.upgrades[i]):
                keyboard.press_and_release(keybinds['upgrade_path_' + str(i + 1)], .1)
                time.sleep(.1)
        self.upgrades = desired_upgrades

    def relocate_lock(self, location):
        mouse.move(*self.target_type_button)
        mouse.click()
        mouse.move(*location)
        mouse.click()


if __name__ == '__main__':
    time.sleep(5)



