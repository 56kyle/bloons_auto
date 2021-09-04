
from maps import *
from map import Map

from towers import *
from tower import Tower

import exceptions

from PIL import Image

import numpy as np
import mouse
import keyboard
import pyscreeze
import random
import time


def find_range_area():
    location_i = mouse.get_position()
    mouse.move(1900, 1060)
    time.sleep(.3)
    img_i = pyscreeze.screenshot()
    mouse.move(*location_i)
    time.sleep(.3)
    keyboard.press_and_release(DartMonkey.keybind, .3)
    time.sleep(.6)
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
    diff_img.convert('1').save(f'./data/{random.randint(1, 100000)}.png')


if __name__ == '__main__':
    time.sleep(3)
    find_range_area()

