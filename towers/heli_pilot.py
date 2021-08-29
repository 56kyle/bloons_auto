from tower import Tower
from config import keybinds


class HeliPilot(Tower):
    name = 'heli_pilot'
    range = 118
    width = 145
    height = 127
    size = 'rectangle'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
