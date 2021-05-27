from tower import Tower


class MonkeySub(Tower):
    name = 'monkey_sub'
    range = 226
    aquatic = True
    width = 75
    height = 65

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
