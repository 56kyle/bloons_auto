from tower import Tower


class SniperMonkey(Tower):
    name = 'sniper_monkey'
    range = 107
    width = 65
    height = 57

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
