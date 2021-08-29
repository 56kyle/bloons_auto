from tower import Tower
from config import keybinds


class SniperMonkey(Tower):
    name = 'sniper_monkey'
    range = 107
    width = 65
    height = 57
    size = 'small'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
