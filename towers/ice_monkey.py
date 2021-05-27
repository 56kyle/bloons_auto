from tower import Tower


class IceMonkey(Tower):
    name = 'ice_monkey'
    range = 123
    width = 65
    height = 57

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
