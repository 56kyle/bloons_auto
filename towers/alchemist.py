from tower import Tower


class Alchemist(Tower):
    name = 'alchemist'
    range = 242
    width = 65
    height = 57

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
