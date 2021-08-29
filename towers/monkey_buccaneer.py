from tower import Tower
from config import keybinds


class MonkeyBuccaneer(Tower):
    name = 'monkey_buccaneer'
    range = 323
    width = 87
    height = 75
    size = 'large'
    keybind = keybinds[name]
    aquatic = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
