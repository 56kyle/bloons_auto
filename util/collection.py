import time
import os
import psutil
from ReadWriteMemory import ReadWriteMemory

import mouse
import pyscreeze

import maps
from map import Map
from maps import *

from tower import Tower, Point
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
        page = 1
        time.sleep(1)
        idol = pyscreeze.locateCenterOnScreen('./collection_idol.png', confidence=.6)
        print(f'Moving to idol at - {idol}')
        if not idol:
            self.click_expert()
            page = 2
            time.sleep(1)
            idol = pyscreeze.locateCenterOnScreen('./collection_idol.png', confidence=.6)
        print(idol)
        time.sleep(.1)
        mouse.move(*idol)
        time.sleep(.1)
        mouse.click()
        time.sleep(.1)
        return page, idol

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

    collector = Collector()
    while True:
        collector.click_play()
        time.sleep(1)
        collector.click_expert()
        time.sleep(1)
        #page, point_chosen = collector.click_ideal_map()
        page = 1
        point_chosen = Point(1400, 570)
        mouse.move(*point_chosen)
        time.sleep(.2)
        mouse.click()
        time.sleep(1)
        collector.click_easy()
        time.sleep(1)
        collector.click_standard()
        time.sleep(5)
        '''
        x, y = Map.point_to_map(point_chosen)
        for map_class in maps.ALL:
            if map_class.difficulty == 'Expert':
                if map_class.page == page and map_class.placement == [x, y]:
                    map = map_class()
                    break
        '''
        collector.current_map = Workshop()
        collector.current_map.play_collection()





