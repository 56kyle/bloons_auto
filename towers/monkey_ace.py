from tower import Tower
from config import keybinds


class MonkeyAce(Tower):
    name = 'monkey_ace'
    range = 118
    width = 152
    height = 85
    size = 'rectangle'
    keybind = keybinds[name]
    aquatic = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
