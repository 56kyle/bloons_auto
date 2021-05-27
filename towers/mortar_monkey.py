from tower import Tower


class MortarMonkey(Tower):
    name = 'mortar_monkey'
    range = 161
    width = 119
    height = 103

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

