from tower import Tower


class SuperMonkey(Tower):
    name = 'super_monkey'
    range = 269
    width = 119
    height = 103

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
