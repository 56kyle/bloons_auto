from .alchemist import Alchemist
from .banana_farm import BananaFarm
from .bomb_shooter import BombShooter
from .boomerang_monkey import BoomerangMonkey
from .dart_monkey import DartMonkey
from .dartling_gunner import DartlingGunner
from .druid import Druid
from .engineer_monkey import EngineerMonkey
from .glue_gunner import GlueGunner
from .heli_pilot import HeliPilot
from .ice_monkey import IceMonkey
from .monkey_ace import MonkeyAce
from .monkey_buccaneer import MonkeyBuccaneer
from .monkey_sub import MonkeySub
from .monkey_village import MonkeyVillage
from .mortar_monkey import MortarMonkey
from .ninja_monkey import NinjaMonkey
from .sniper_monkey import SniperMonkey
from .spike_factory import SpikeFactory
from .super_monkey import SuperMonkey
from .tack_shooter import TackShooter
from .wizard_monkey import WizardMonkey

ALL = [Alchemist, BananaFarm, BombShooter, BoomerangMonkey, DartMonkey, DartlingGunner, Druid, EngineerMonkey,
       GlueGunner, HeliPilot, IceMonkey, MonkeyAce, MonkeyBuccaneer, MonkeySub, MonkeyVillage, MortarMonkey,
       NinjaMonkey, SniperMonkey, SpikeFactory, SuperMonkey, TackShooter, WizardMonkey]

AQUATIC = []
for tower in ALL:
    if tower.aquatic:
        AQUATIC.append(tower)

SMALL = []
MEDIUM = []
LARGE = []
XL = []
RECTANGLE = []

for tower in ALL:
    if tower.width == 65 and tower.height == 57:
        SMALL.append(tower)
    elif tower.width == 75 and tower.height == 65:
        MEDIUM.append(tower)
    elif tower.width == 87 and tower.height == 75:
        LARGE.append(tower)
    elif tower.width == 119 and tower.height == 103:
        XL.append(tower)
    else:
        RECTANGLE.append(tower)




