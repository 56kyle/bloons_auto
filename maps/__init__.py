from .monkey_meadow import MonkeyMeadow
from .tree_stump import TreeStump
from .town_center import TownCenter
from .resort import Resort
from .skates import Skates
from .lotus_island import LotusIsland
from .candy_falls import CandyFalls
from .winter_park import WinterPark
from .carved import Carved
from .park_path import ParkPath
from .alpine_run import AlpineRun
from .frozen_over import FrozenOver
from .in_the_loop import InTheLoop
from .cubism import Cubism
from .four_circles import FourCircles
from .hedge import Hedge
from .end_of_the_road import EndOfTheRoad
from .logs import Logs
from .balance import Balance
from .encrypted import Encrypted
from .bazaar import Bazaar
from .adoras_temple import AdorasTemple
from .spring_spring import SpringSpring
from .kartsndarts import KartsNDarts
from .moon_landing import MoonLanding
from .haunted import Haunted
from .downstream import Downstream
from .firing_range import FiringRange
from .cracked import Cracked
from .streambed import Streambed
from .chutes import Chutes
from .rake import Rake
from .spice_islands import SpiceIslands
from .bloonarius_prime import BloonariusPrime
from .x_factor import XFactor
from .mesa import Mesa
from .geared import Geared
from .spillway import Spillway
from .cargo import Cargo
from .pats_pond import PatsPond
from .peninsula import Peninsula
from .high_finance import HighFinance
from .another_brick import AnotherBrick
from .off_the_coast import OffTheCoast
from .cornfield import Cornfield
from .underground import Underground
from .sanctuary import Sanctuary
from .ravine import Ravine
from .flooded_valley import FloodedValley
from .infernal import Infernal
from .bloody_puddles import BloodyPuddles
from .workshop import Workshop
from .quad import Quad
from .dark_castle import DarkCastle
from .muddy_puddles import MuddyPuddles
from .ouch import Ouch


ALL = [
    MonkeyMeadow,
    TreeStump,
    TownCenter,
    Resort,
    Skates,
    LotusIsland,
    CandyFalls,
    WinterPark,
    Carved,
    ParkPath,
    AlpineRun,
    FrozenOver,
    InTheLoop,
    Cubism,
    FourCircles,
    Hedge,
    EndOfTheRoad,
    Logs,
    Balance,
    Encrypted,
    Bazaar,
    AdorasTemple,
    SpringSpring,
    KartsNDarts,
    MoonLanding,
    Haunted,
    Downstream,
    FiringRange,
    Cracked,
    Streambed,
    Chutes,
    Rake,
    SpiceIslands,
    BloonariusPrime,
    XFactor,
    Mesa,
    Geared,
    Spillway,
    Cargo,
    PatsPond,
    Peninsula,
    HighFinance,
    AnotherBrick,
    OffTheCoast,
    Cornfield,
    Underground,
    Sanctuary,
    Ravine,
    FloodedValley,
    Infernal,
    BloodyPuddles,
    Workshop,
    Quad,
    DarkCastle,
    MuddyPuddles,
    Ouch,
]

BEGINNER = [
    MonkeyMeadow,
    TreeStump,
    TownCenter,
    Resort,
    Skates,
    LotusIsland,
    CandyFalls,
    WinterPark,
    Carved,
    ParkPath,
    AlpineRun,
    FrozenOver,
    InTheLoop,
    Cubism,
    FourCircles,
    Hedge,
    EndOfTheRoad,
    Logs,
]

INTERMEDIATE = [
    Balance,
    Encrypted,
    Bazaar,
    AdorasTemple,
    SpringSpring,
    KartsNDarts,
    MoonLanding,
    Haunted,
    Downstream,
    FiringRange,
    Cracked,
    Streambed,
    Chutes,
    Rake,
    SpiceIslands,
    BloonariusPrime,
]

ADVANCED = [
    XFactor,
    Mesa,
    Geared,
    Spillway,
    Cargo,
    PatsPond,
    Peninsula,
    HighFinance,
    AnotherBrick,
    OffTheCoast,
    Cornfield,
    Underground,
]

EXPERT = [
    Sanctuary,
    Ravine,
    FloodedValley,
    Infernal,
    BloodyPuddles,
    Workshop,
    Quad,
    DarkCastle,
    MuddyPuddles,
    Ouch,
]

DIFFICULTIES = [
    BEGINNER,
    INTERMEDIATE,
    ADVANCED,
    EXPERT,
]

for map in ALL:
    map.ALL = ALL
    map.DIFFICULTIES = DIFFICULTIES
    map.BEGINNER = BEGINNER
    map.INTERMEDIATE = INTERMEDIATE
    map.ADVANCED = ADVANCED
    map.EXPERT = EXPERT
