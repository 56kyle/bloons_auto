from tower import Tower
from config import keybinds


class MortarMonkey(Tower):
    name = 'mortar_monkey'
    range = 161
    width = 119
    height = 103
    size = 'xl'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
