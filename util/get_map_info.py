from maps import *
from map import Map
import pyscreeze
import win32gui

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
    im = pyscreeze.screenshot()
    img_file_name = f'../maps/{a_map.name}/placement/{"land" if not tower.aquatic else "sea"}/{tower.size if tower.size != "rectangle" else tower.name}.png'
    im.save(f'../maps/{a_map.name}/{a_map.name}.png')
    try:
        img = Image.open(img_file_name)
    except:
        img = Image.new('RGB', (1920, 1080))

    keyboard.press_and_release(tower.keybind)
    for region in regions:
        grain = 1
        win = win32gui.GetActiveWindow()
        xi, yi, xf, yf = region
        for x in range(xi, xf, grain):
            for y in range(yi, yf, grain):
                if mouse.get_position() == (0, 0):
                    print('fuck')
                    return
                if tower.can_place(Point(x, y), im, win):
                    img.putpixel((x, y), (255, 255, 255))
            img.save(img_file_name)


def get_map_img(a_map):
    mouse.move(1910, 1070)
    time.sleep(.3)
    im = pyscreeze.screenshot()
    im.save(f'../maps/{a_map.name}/{a_map.name}.png')


if __name__ == '__main__':
    time.sleep(2)

    infernal_regions = [
        Region(56, 424, 164, 714),
        Region(394, 154, 548, 300),
        Region(760, 262, 912, 410),
        Region(1106, 136, 1286, 308),
        Region(388, 752, 562, 932),
        Region(752, 664, 920, 818),
        Region(1126, 766, 1278, 926),
        Region(1502, 426, 1638, 710),
    ]
    dark_castle_regions = [
        #Region(350, 30, 1048, 1050),
        Region(1264, 30, 1890, 1050)
    ]
    bloody_puddles_regions = [
        Region(58, 28, 1890, 1050)
    ]
    get_map_img(BloodyPuddles())
    #get_placement_map(BloodyPuddles(), towers.SMALL[0], bloody_puddles_regions)
    # get_placement_map(towers.MEDIUM[0])
    # get_placement_map(towers.SpikeFactory)
    # get_placement_map(towers.XL[0])
    # for tower in towers.RECTANGLE:
    # get_placement_map(tower)
