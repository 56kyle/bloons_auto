import keyboard
import mouse
import time

from map import Map
from towers import *
from tower import Point
from config import keybinds


class Workshop(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'workshop'
        self.difficulty = 'expert'
        self.page = 1
        self.placement = [2, 0]

    def play_collection(self):
        dart = DartMonkey(location=Point(1016, 501))
        self.start()
        self.toggle_fast_forward()

        # Wait for round one to end
        time.sleep(10)

        # Place Ben
        keyboard.press_and_release(keybinds['heroes'], .2)
        time.sleep(.3)
        mouse.move(1518, 987)
        time.sleep(.2)
        mouse.click()

        # Wait to buy wiz
        time.sleep(15)
        wiz = WizardMonkey(location=Point(1016, 437))

        # Upgrade wiz
        time.sleep(15)
        wiz.assign_upgrades([0, 1, 0])
        time.sleep(15)
        wiz.assign_upgrades([0, 2, 0])

        # Wait to buy spike factory
        time.sleep(20)
        spike = SpikeFactory(location=Point(1580, 685))

        # Upgrade spike factory.
        time.sleep(20)
        spike.assign_upgrades([1, 0, 0])
        time.sleep(15)
        spike.assign_upgrades([1, 1, 0])
        time.sleep(15)
        spike.assign_upgrades([1, 2, 0])
        time.sleep(15)
        spike.assign_upgrades([2, 2, 0])

        # Waut to buy a

        # Wait for round to finish out
        time.sleep(144)







