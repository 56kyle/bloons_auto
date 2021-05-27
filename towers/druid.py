from tower import Tower


class Druid(Tower):
    name = 'druid'
    range = 188
    width = 75
    height = 65

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
