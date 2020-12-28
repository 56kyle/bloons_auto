import time
import mouse
import collections
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


Point = collections.namedtuple('Point', 'x y')


if __name__ == '__main__':
    time.sleep(5)
    d = DartMonkey(upgrades=[5, 0, 2], location=Point(900, 900))
    b = BananaFarm(upgrades=[3, 0, 2], location=Point(500, 900))
    i = IceMonkey(upgrades=[1, 2, 2], location=Point(500, 600))
    del d, b, i





