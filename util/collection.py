import time
import os
import psutil
from ReadWriteMemory import ReadWriteMemory

import mouse
import pyscreeze

from map import Map
from maps import *

from tower import Tower
from towers import *


class Collector:
    play_button = (820, 940)
    expert_map_button = (1340, 980)
    easy_button = (615, 420)
    standard_button = (640, 585)
    back_to_main_button = (60, 70)

    def __init__(self):
        self.current_map = None

    def click_expert(self):
        mouse.move(*self.expert_map_button)
        time.sleep(1)
        mouse.click()

    def is_map(self, map):
        os.path.join('./maps', map.name,)

    def click_ideal_map(self):
        self.click_expert()
        time.sleep(1)
        idol = pyscreeze.locateCenterOnScreen('./collection_idol.png', confidence=.6)
        print(f'Moving to idol at - {idol}')
        if not idol:
            self.click_expert()
            time.sleep(1)
            idol = pyscreeze.locateCenterOnScreen('./collection_idol.png', confidence=.6)
        print(idol)
        time.sleep(.1)
        mouse.move(*idol)
        time.sleep(.1)
        mouse.click()
        time.sleep(.1)

    def click_play(self):
        mouse.move(*self.play_button)
        time.sleep(.4)
        mouse.click()
        time.sleep(1)

    def click_easy(self):
        mouse.move(*self.easy_button)
        time.sleep(.4)
        mouse.click()
        time.sleep(1)

    def click_standard(self):
        mouse.move(*self.standard_button)
        time.sleep(.4)
        mouse.click()
        time.sleep(1)


if __name__ == '__main__':
    time.sleep(5)
    x, y = mouse.get_position()



    '''
    collector = Collector()
    collector.click_play()
    collector.click_ideal_map()
    collector.click_easy()
    collector.click_standard()
    '''