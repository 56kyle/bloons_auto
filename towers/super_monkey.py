from tower import Tower
from config import keybinds


class SuperMonkey(Tower):
    name = 'super_monkey'
    range = 269
    width = 119
    height = 103
    size = 'xl'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
