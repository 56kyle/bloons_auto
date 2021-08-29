from tower import Tower
from config import keybinds


class BananaFarm(Tower):
    name = 'banana_farm'
    range = 215
    width = 162
    height = 141
    size = 'rectangle'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
