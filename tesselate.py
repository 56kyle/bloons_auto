import time
import mouse
import collections
from tower import Tower
from towers.alchemist import Alchemist
from towers.banana_farm import BananaFarm
from towers.bomb_shooter import BombShooter
from towers.boomerang_monkey import BoomerangMonkey
from towers.dart_monkey import DartMonkey
from towers.dartling_gunner import DartlingGunner
from towers.druid import Druid
from towers.engineer_monkey import EngineerMonkey
from towers.glue_gunner import GlueGunner
from towers.heli_pilot import HeliPilot
from towers.ice_monkey import IceMonkey
from towers.monkey_ace import MonkeyAce
from towers.monkey_buccaneer import MonkeyBuccaneer
from towers.monkey_sub import MonkeySub
from towers.monkey_village import MonkeyVillage
from towers.mortar_monkey import MortarMonkey
from towers.ninja_monkey import NinjaMonkey
from towers.sniper_monkey import SniperMonkey
from towers.spike_factory import SpikeFactory
from towers.super_monkey import SuperMonkey
from towers.tack_shooter import TackShooter
from towers.wizard_monkey import WizardMonkey
import collections
import random
from PIL import Image

TOWERS = [
    Alchemist,
    BananaFarm,
    BombShooter,
    BoomerangMonkey,
    DartMonkey,
    DartlingGunner,
    Druid,
    EngineerMonkey,
    GlueGunner,
    HeliPilot,
    IceMonkey,
    MonkeyAce,
    MonkeyBuccaneer,
    MonkeySub,
    MonkeyVillage,
    MortarMonkey,
    SniperMonkey,
    SpikeFactory,
    SuperMonkey,
    TackShooter,
    WizardMonkey
]

Point = collections.namedtuple('Point', 'x y')


class Formation:
    def __init__(self, monkeys, start):
        self.monkeys = []
        if not start:
            start = mouse.get_position()
        self.start = start
        last_placement = [0, 0]
        last_placement[1] = start[1] - monkeys[0][0].height
        for row in monkeys:
            last_placement[0] = start[0] - (monkeys[0][0].width + 1)
            last_placement[1] = last_placement[1] + row[0].height
            for monkey in row:
                last_placement = [last_placement[0] + monkey.width + 1, last_placement[1]]
                self.monkeys.append(monkey(location=last_placement))
        time.sleep(2)
        del self.monkeys


def scan(cls):
    center = Point(1130, 860)
    reference_farm = BananaFarm(location=center)
    hitbox_scan = Image.new('RGB', (BananaFarm.width, BananaFarm.height))
    for x in range(center.x - int(.5*BananaFarm.width + .5*cls.width), center.x + int(.5*BananaFarm.width + .5*cls.width)):
        for y in range(center.y - int(.5*BananaFarm.height + .5*cls.height), center.y + int(.5*BananaFarm.height + .5*cls.height)):
            if Tower.can_place(cls, Point(x, y)):
                hitbox_scan.putpixel(Point(x-center.x, y-center.y), (255, 255, 255))
            else:
                break
    hitbox_scan.save('./towers/hitboxes/{}.png'.format(cls.name))


def main():
    time.sleep(5)
    scan(DartMonkey)


if __name__ == '__main__':
    main()
