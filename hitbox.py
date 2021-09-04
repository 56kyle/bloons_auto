
from maps import *
from map import Map

from towers import *
from tower import Tower

import pyscreeze
import os
from functools import cache
from PIL import Image
import numpy as np


class Hitbox:
    def __init__(self, tower: Tower):
        self.tower = tower
        self.size = tower.size
        self.width = tower.width
        self.height = tower.height
        self.file_path = os.path.join('.', 'towers', 'hitboxes', f'{self.size}')
        self.img = Image.open(self.file_path + '.png')

    @cache
    def data(self):
        return np.array(self.img)

    def save(self):
        np.save(self.file_path + '.npy', self.data())


if __name__ == '__main__':
    for size in SIZES:
        try:
            hitbox = Hitbox(size[0])
            new_img = hitbox.img.convert('1')
            hitbox.img = new_img
            new_data = []
            for val in hitbox.img.getdata():
                new_data.append(not val)
            hitbox.img.putdata(new_data)
            hitbox.img.save(hitbox.file_path + '_test.png')
            np.save(hitbox.file_path, hitbox.data())

        except FileNotFoundError:
            pass


