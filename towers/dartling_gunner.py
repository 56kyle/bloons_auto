from tower import Tower


class DartlingGunner(Tower):
    name = 'dartling_gunner'
    range = 107
    width = 75
    height = 65

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
