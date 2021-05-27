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


def get_hitbox(klass):
    time.sleep(5)
    tower = klass()


if __name__ == '__main__':
    time.sleep(5)
    dart = DartMonkey(upgrades=[3, 2, 0])
    time.sleep(3)
    del dart




