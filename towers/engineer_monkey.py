from tower import Tower


class EngineerMonkey(Tower):
    name = 'engineer_monkey'
    range = 215
    width = 75
    height = 65

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
