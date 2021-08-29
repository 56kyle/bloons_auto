from tower import Tower
from config import keybinds


class MonkeySub(Tower):
    name = 'monkey_sub'
    range = 226
    width = 75
    height = 65
    size = 'medium'
    keybind = keybinds[name]
    aquatic = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
