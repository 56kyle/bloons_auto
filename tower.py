from typing import Union, Iterable, Optional

import mouse
import keyboard
import numpy as np
import pyscreeze
import collections
import time
import win32con
import win32gui
import win32ui


from dynamic_info.session import Btd6Session
from dynamic_info.money import MoneyHook
from dynamic_info.placeable import PlaceableHook

from window_input import Window, Key
from PIL import Image
from config import keybinds

# Various usefull types
from exceptions import PixelNotChangingError

Point = collections.namedtuple('Point', 'x y')
Color = collections.namedtuple('Color', 'r g b')
Pixel = collections.namedtuple('Pixel', 'point color')

# Types for coercing down into one type
PointLike = Union[Point, Iterable]


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

# Utility functions that I really don't want to need to google for again
def capture(x, y):
    hwnd = win32gui.FindWindow(None, 'BloonsTD6.exe')
    w_dc = win32gui.GetWindowDC(hwnd)
    dc_obj = win32ui.CreateDCFromHandle(w_dc)
    c_dc = dc_obj.CreateCompatibleDC()
    data_bit_map = win32ui.CreateBitmap()
    data_bit_map.CreateCompatibleBitmap(dc_obj, 1, 1)
    c_dc.SelectObject(data_bit_map)
    c_dc.BitBlt((x, y), (x+1, y+1), dc_obj, (x, y), win32con.SRCCOPY)
    bmpinfo = data_bit_map.GetInfo()
    bmpstr = data_bit_map.GetBitmapBits(True)
    return Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)


def get_pixel(i_x, i_y, win=None):
    #win = win32gui.FindWindow(None, "BloonsTD6") if not win else win
    win = win32gui.GetActiveWindow() if not win else win
    dc = win32gui.GetDC(win)
    long_colour = win32gui.GetPixel(dc, i_x, i_y)
    i_colour = int(long_colour)
    win32gui.DeleteDC(dc)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


class Tower:
    """Base class for all towers"""
    name = None
    range = None
    height = None
    width = None
    keybind = None
    aquatic = False
    size = None
    session = Btd6Session([MoneyHook, PlaceableHook])

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
        if self.place():
            upgrades = kwargs.get('upgrades')
            self.upgrades = [0, 0, 0]
            if upgrades:
                self.assign_upgrades(upgrades)
        else:
            del self

    @classmethod
    def placeable(cls, x: Union[Iterable, int], y: Optional[int] = None) -> bool:
        if isinstance(x, Iterable) and not y:
            x = list(*x)
            (x, y) = (x[0], x[1])
        keyboard.press_and_release(cls.keybind, .03)
        ti = time.time()
        while cls.session.location != (x, y) and time.time() - ti < .5:
            mouse.move(x, y)
        keyboard.press_and_release('escape', .03)
        return cls.session.placeable and cls.session.location == (x, y)

    def can_place(self, *args, **kwargs):
        return self.placeable(args[0])

    def teardown(self):
        self.select()
        keyboard.press_and_release(keybinds['sell'], .1)
        self.session.hooks['PlaceableHook'].script.unload()
        self.session.hooks['MoneyHook'].script.unload()

    @classmethod
    def find_placeable_areas(cls, map):
        mouse.move(1920, 1080)
        img_before = pyscreeze.screenshot()
        img_file_name = f'../maps/{map.name}/placement/{"land" if not cls.aquatic else "sea"}/{cls.size if cls.size != "rectangle" else cls.name}.png'
        try:
            img_new = Image.open(img_file_name)
        except:
            img_new = Image.new('RGB', (1920, 1080))

        img_new.save(img_file_name)

        grain = 10
        keyboard.press_and_release(cls.keybind, .01)
        for x in range(30, 1890, grain):
            for y in range(30, 1050, grain):
                if cls.can_place(Point(x, y), img_before):
                    img_new.putpixel((x, y), (255, 255, 255))
                else:
                    img_new.putpixel((x, y), (0, 0, 0))
            img_new.save(img_file_name)

    @classmethod
    def have_funds(cls):
        mouse.move(900, 500)
        time.sleep(.3)
        img_i = pyscreeze.screenshot()
        keyboard.press_and_release(cls.keybind, .2)
        time.sleep(.2)
        img_f = pyscreeze.screenshot()
        cls.deselect()
        if img_i.getpixel(900, 510) == img_f.getpixel(900, 510):
            return False
        else:
            return True

    @staticmethod
    def coerce_to_point(location: Union[Point, Iterable]):
        if isinstance(location, Point):
            return location
        if hasattr(location, 'x') and hasattr(location, 'y'):
            location = Point(location.x, location.y)
        elif len(location) >= 2:
            location = Point(location[0], location[1])
        return location

    @classmethod
    def can_place_quick(cls,
                         location: Union[Point, Iterable],
                         before=Union[Image.Image, np.ndarray, Iterable],
                         area_to_manual_delay=Union[np.ndarray, None],
                         *args,
                         **kwargs):
        # Just format stuff to be easier to use
        location = cls.coerce_to_point(location)
        if not isinstance(before, np.ndarray):
            before = np.array(before)
        measuring_point = cls.get_measuring_point(location)
        try:
            cls.quick_move(location, measuring_point, before, area_to_manual_delay)
        except PixelNotChangingError:
            measuring_point = cls.get_measuring_point(location, backup=True)
        before_px = [*before[measuring_point.y, measuring_point.x]]
        after_px = [*np.array(get_pixel(*measuring_point))]
        #print(f'before - {before_px}')
        #print(f'after - {after_px}')
        if after_px[0] - before_px[0] > after_px[2] - before_px[2]:
            return False
        else:
            return True

    @classmethod
    def quick_move(cls, location: Point, measuring_point: Point, before: np.ndarray, area_to_manual_delay: Union[np.ndarray, None]):
        current_px = before[measuring_point.y, measuring_point.x]
        t1 = time.time()
        '''
        if area_to_manual_delay is not None:
            if area_to_manual_delay[measuring_point.y, measuring_point.x]:
                mouse.move(location.x, location.y)
                time.sleep(.04)
                return
        '''

        while [*current_px] == [*before[measuring_point.y, measuring_point.x]]:
            if mouse.get_position() == (0, 0, 0):
                break
            if time.time() - t1 > .09:
                raise PixelNotChangingError('Pixel has been static')
            mouse.move(location.x, location.y)
            current_px = np.array(get_pixel(*measuring_point))

    @classmethod
    def get_measuring_point(cls, location: Point, backup: bool = False) -> Point:
        # Basically, figure out whether x or y is closest to an edge relative to the size,
        # then pick the point closest to the center of the map to measure from
        playable_x = 1645
        playable_y = 1080
        x_fraction = float(location.x) / playable_x
        y_fraction = float(location.y) / playable_y

        if not backup:
            if .5 - x_fraction < 0:
                measuring_point = Point(location.x - cls.range, location.y)
            else:
                measuring_point = Point(location.x + cls.range, location.y)
        else:
            if .5 - y_fraction < 0:
                measuring_point = Point(location.x, location.y - int(cls.range * .5))
            else:
                measuring_point = Point(location.x, location.y + int(cls.range * .5))
        return measuring_point

    @classmethod
    def _can_place_slow(cls, location: Point):
        pass

    @classmethod
    def _can_place(cls, location, im_1=None):
        cls.keybind = keybinds[cls.name]
        mouse.move(location.x, location.y)

        if location.x > 1100:
            measuring_point = Point(location.x - cls.range, location.y)
        else:
            measuring_point = Point(location.x + cls.range, location.y)

        start_from_blue = False
        if im_1:
            start_from_blue = True
            before = im_1.getpixel(measuring_point)
            time.sleep(.07)
        else:
            before = get_pixel(*measuring_point)
            keyboard.press_and_release(cls.keybind, .04)
            time.sleep(.04)

        after = get_pixel(*measuring_point)
        if not start_from_blue:
            cls.deselect()

        #after = capture(*measuring_point).getpixel((0, 0))
        #after = pyscreeze.screenshot().getpixel(measuring_point)
        print(f'before - {before}')
        print(f'after - {after}')

        if after[0] > before[0] and abs(after[0] - before[0]) > 10 and (after[2] < before[2] or start_from_blue):
            return False
        else:
            return True

    def place(self):
        if self.can_place(self.location):
            mouse.move(*self.location)
            time.sleep(.05)
            keyboard.press_and_release(self.keybind, .1)
            time.sleep(.05)
            mouse.click()
            return True
        return False

    @staticmethod
    def deselect():
        time.sleep(.1)
        keyboard.press_and_release('escape', .1)
        time.sleep(.1)
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
        time.sleep(.1)
        for i in range(3):
            for _ in range(desired_upgrades[i] - self.upgrades[i]):
                keyboard.press_and_release(keybinds['upgrade_path_' + str(i + 1)], .2)
                time.sleep(.2)
        self.upgrades = desired_upgrades
        time.sleep(.1)
        self.deselect()

    def relocate_lock(self, location):
        mouse.move(*self.target_type_button)
        mouse.click()
        mouse.move(*location)
        mouse.click()


if __name__ == '__main__':
    time.sleep(5)



