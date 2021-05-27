from tower import Tower


class MonkeyVillage(Tower):
    name = 'monkey_village'
    range = 215
    width = 119
    height = 103

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
