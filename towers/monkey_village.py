from tower import Tower
from config import keybinds


class MonkeyVillage(Tower):
    name = 'monkey_village'
    range = 215
    width = 119
    height = 103
    size = 'xl'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
