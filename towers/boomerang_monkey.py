from tower import Tower
from config import keybinds


class BoomerangMonkey(Tower):
    name = 'boomerang_monkey'
    range = 231
    width = 75
    height = 65
    size = 'medium'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
