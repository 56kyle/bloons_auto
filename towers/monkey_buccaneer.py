from tower import Tower


class MonkeyBuccaneer(Tower):
    name = 'monkey_buccaneer'
    range = 323
    aquatic = True
    width = 87
    height = 75

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
