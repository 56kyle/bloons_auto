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


def get_placement_map(a_map, tower, regions):
    win = Window()
    im = win.capture(((0, 0), (1920, 1080)))
    im.save(f'../maps/{a_map.name}/{a_map.name}.png')
    img = Image.new('RGB', (1920, 1080))
    keyboard.press_and_release(keybinds.get(tower.name))
    for region in regions:
        xi, yi, xf, yf = region
        for x in range(xi, xf):
            for y in range(yi, yf):
                if mouse.get_position() == (0, 0):
                    return
                if can_place(tower, Point(x, y), im, win):
                    img.putpixel((x, y), (255, 255, 255))
            img.save(f'../maps/{a_map.name}/placement/{"land" if not tower.aquatic else "sea"}/{tower.size if tower.size != "rectangle" else tower.name}.png')


def can_place(cls, location, img, win):
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

    regions = [
        Region(56, 424, 164, 714),
        Region(394, 154, 548, 300),
        Region(760, 262, 912, 410),
        Region(1106, 136, 1286, 308),
        Region(388, 752, 562, 932),
        Region(752, 664, 920, 818),
        Region(1126, 766, 1278, 926),
        Region(1502, 426, 1638, 710),
    ]
    print(towers.SMALL)
    get_placement_map(Infernal(), towers.SMALL[0], regions)
    # get_placement_map(towers.MEDIUM[0])
    # get_placement_map(towers.SpikeFactory)
    # get_placement_map(towers.XL[0])
    # for tower in towers.RECTANGLE:
    # get_placement_map(tower)

