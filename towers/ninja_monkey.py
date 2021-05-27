from tower import Tower


class NinjaMonkey(Tower):
    name = 'ninja_monkey'
    range = 215
    width = 65
    height = 57

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
