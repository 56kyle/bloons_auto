import os
import sys

from maps import *
from map import Map
import pyscreeze
import win32gui

import towers
from tower import Tower, Point


from dynamic_info import Btd6Session, MoneyHook, PlaceableHook

from hitbox import Hitbox

from PIL import Image

import numpy as np
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
        win = win32gui.GetActiveWindow()
        xi, yi, xf, yf = region
        for x in range(xi, xf, 16):
            for y in range(yi, yf, 12):
                if mouse.get_position() == (0, 0):
                    print('fuck')
                    return
                if tower.can_place(Point(x, y), im):
                    a = False
                    b = False
                    if img.getpixel((x - 16, y)) == (255, 255, 255):
                        a = True
                        for dx in range(1, 17):
                            img.putpixel((x - dx, y), (255, 255, 255))
                    if img.getpixel((x, y - 12)) == (255, 255, 255):
                        b = True
                        for dy in range(1, 17):
                            img.putpixel((x, y - dy), (255, 255, 255))
                    if img.getpixel((x - 16, y - 12)) == (255, 255, 255) and a and b:
                        for dy in range(1, 17):
                            for dx in range(1, 17):
                                img.putpixel((x - dx, y - dy), (255, 255, 255))
                    img.putpixel((x, y), (255, 255, 255))

            img.save(img_file_name)


def get_changing():
    location_i = mouse.get_position()
    mouse.move(1900, 1060)
    time.sleep(.3)
    img_i = pyscreeze.screenshot()
    time.sleep(.3)
    img_f = pyscreeze.screenshot()
    np_i = np.array(img_i)
    np_f = np.array(img_f)
    diff = np_f - np_i
    new_data = []
    diff_img = Image.fromarray(diff)
    for px in diff_img.getdata():
        if px == (0, 0, 0):
            new_data.append((0, 0, 0))
        else:
            new_data.append((255, 255, 255))
    diff_img.putdata(new_data)
    diff_img.putpixel(location_i, (0, 0, 0))
    return np.array(diff_img.convert('1'))


def get_np_placement_map(a_map, tower, regions):
    manual_delay_locations = get_changing()
    im = pyscreeze.screenshot()
    img_file_name = f'../maps/{a_map.name}/placement/{"land" if not tower.aquatic else "sea"}/{tower.size if tower.size != "rectangle" else tower.name}'
    im.save(f'../maps/{a_map.name}/{a_map.name}.png')
    np_im = np.array(im)
    if os.path.isfile(img_file_name + '.npy'):
        placeable = np.load(img_file_name + '.npy')
    else:
        placeable = np.full((1080, 1920), False)

    checked = np.full((1080, 1920), False)

    keyboard.press_and_release(tower.keybind)
    for region in regions:
        xi, yi, xf, yf = region
        #gx = int(16 / 2)
        #gy = int(12 / 2)
        gx = 16
        gy = 12
        while not (gx == 1 and gy == 1):
            for x in range(xi, xf, gx):
                for y in range(yi, yf, gy):
                    #print('=====')
                    if mouse.get_position() == (0, 0):
                        print('fuck')
                        return
                    if not checked[y, x]:
                        print(f'not checked[{y}, {x}]')
                        placeable[y, x] = tower.can_place_quick(Point(x, y), np_im, manual_delay_locations)
                    quadrants = [
                        [gx, gy],  # Top Left
                        [-gx, gy],  # Top Right
                        [gx, -gy],  # Bot Left
                        [-gx, -gy],  # Bot Right
                    ]
                    for pair in quadrants:
                        print(f'pair - {pair}')
                        if gx > 2 and gy > 2 and not checked[y - int(abs(pair[1] / pair[1])), x - int(abs(pair[0] / pair[0]))]:
                            checked, placeable = should_fill_quad(checked, placeable, x, y, pair[0], pair[1])
                        else:
                            print('else')
                np.save(img_file_name, placeable)
                Image.fromarray(placeable).save(img_file_name + '.png')
            gx = int(gx / 2) if gx != 1 else gx
            gy = int(gy / 2) if gy != 1 else gy


def should_fill_quad(checked, placeable, x, y, gx, gy):
    """Checks if a given rectangle can be filled in and does so if possible"""
    #print('should_fill_quad')
    #print(f'\tx - {x}')
    #print(f'\ty - {y}')
    #print(f'\tgx - {gx}')
    #print(f'\tgy - {gy}')
    point_one = checked[y - gy, x - gx] and placeable[y - gy, x - gx]
    point_two = checked[y, x - gx] and placeable[y, x - gx]
    point_three = checked[y - gy, x] and placeable[y - gy, x]
    #print(f'\tpoint_one - {point_one}')
    #print(f'\tpoint_tow - {point_two}')
    #print(f'\tpoint_threee - {point_three}')
    desired_result = placeable[y, x]
    #print(f'\tdesired_result = {desired_result}')
    if point_one == desired_result and point_two == desired_result and point_three == desired_result:
        placeable[y - gy:y, x - gx:x] = np.full((abs(gy), abs(gx)), desired_result)
        checked[y - gy:y, x - gx:x] = np.full((abs(gy), abs(gx)), True)

    return checked, placeable

def get_np_placement_map_one(a_map, tower, regions):
    manual_delay_locations = get_changing()
    im = pyscreeze.screenshot()
    img_file_name = f'../maps/{a_map.name}/placement/{"land" if not tower.aquatic else "sea"}/{tower.size if tower.size != "rectangle" else tower.name}'
    im.save(f'../maps/{a_map.name}/{a_map.name}.png')
    np_im = np.array(im)
    if os.path.isfile(img_file_name + '.npy'):
        placeable = np.load(img_file_name + '.npy')
    else:
        placeable = np.full((1080, 1920), False)

    keyboard.press_and_release(tower.keybind)
    for region in regions:
        xi, yi, xf, yf = region
        #gx = int(16 / 2)
        #gy = int(12 / 2)
        for x in range(xi, xf):
            for y in range(yi, yf):
                #print('=====')
                if mouse.get_position() == (0, 0):
                    print('fuck')
                    return
                placeable[y, x] = tower.can_place_quick(Point(x, y), np_im, manual_delay_locations)
            np.save(img_file_name, placeable)
            Image.fromarray(placeable).save(img_file_name + '.png')

def get_map_img(a_map):
    mouse.move(1910, 1070)
    time.sleep(.3)
    im = pyscreeze.screenshot()
    im.save(f'../maps/{a_map.name}/{a_map.name}.png')


if __name__ == '__main__':
    btd6_session = Btd6Session(hooks=[MoneyHook])
    while True:
        time.sleep(1)
        print(btd6_session.money)

    '''
    time.sleep(4)

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
        #Region(30, 30, 1048, 1050),
        Region(1264, 30, 1640, 1050)
    ]
    bloody_puddles_regions = [
        Region(58, 28, 1890, 1050)
    ]
    ravine_regions = [
        Region(32, 36, 1600, 1050)
    ]
    quad_regions = [
        Region(32, 36, 1600, 1050)
    ]

    ouch_regions = [
        Region(32, 36, 1600, 1050),
        #Region(32, 36, 260, 205),
    ]

    get_np_placement_map(Ouch(), towers.SMALL[0], ouch_regions)
    '''
    # get_placement_map(towers.MEDIUM[0])
    # get_placement_map(towers.SpikeFactory)
    # get_placement_map(towers.XL[0])
    # for tower in towers.RECTANGLE:
    # get_placement_map(tower)