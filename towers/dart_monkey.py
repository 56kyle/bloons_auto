from tower import Tower


class DartMonkey(Tower):
    name = 'dart_monkey'
    range = 172
    width = 65
    height = 57

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
