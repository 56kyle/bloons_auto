
from maps import *
from map import Map

import towers
from tower import Tower, Point

from PIL import Image

import mouse
import keyboard
from window_input import Window, Key
import collections
import time
from config import keybinds

Region = collections.namedtuple('Region', 'xi yi xf yf')


def can_place(cls, location, img, win):
    win = Window()
    while not mouse.get_position() == location:
        mouse.move(location.x, location.y)
        print(f'mouse moved to {location}')

    if location.x > 1100:
        measuring_point = Point(location.x - (cls.range - 2), location.y)
    else:
        measuring_point = Point(location.x + (cls.range - 2), location.y)

    print(f'measuring point is at {measuring_point}')

    before = img.getpixel(measuring_point)
    print(f'before = {before}')
    after = win.pixel(measuring_point.x, measuring_point.y)
    print(f'after = {after}')
    if (after[0] - before[0]) >= 8:
        return False
    else:
        return True


if __name__ == '__main__':
    time.sleep(5)
    win = Window()
    tower = towers.SMALL[0]
    a_map = DarkCastle()
    im = win.capture(((0, 0), (1920, 1080)))
    im.save(f'../maps/{a_map.name}/{a_map.name}.png')
    img = Image.new('RGB', (1920, 1080))
    keyboard.press_and_release(keybinds.get(tower.name))
    while True:
        if mouse.get_position() == (0, 0):
            break
        x, y = mouse.get_position()
        if can_place(tower, Point(x, y), im, win):
            img.putpixel((x, y), (255, 255, 255))
            img.save(f'../maps/{a_map.name}/placement/{"land" if not tower.aquatic else "sea"}/{tower.size}.png')

