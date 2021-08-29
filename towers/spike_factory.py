from tower import Tower
from config import keybinds


class SpikeFactory(Tower):
    name = 'spike_factory'
    range = 183
    width = 87
    height = 75
    size = 'large'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
