from tower import Tower


class BoomerangMonkey(Tower):
    name = 'boomerang_monkey'
    range = 231
    width = 75
    height = 65

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
