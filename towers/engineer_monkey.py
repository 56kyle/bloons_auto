from tower import Tower


class EngineerMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'engineer_monkey'
        kwargs['range'] = 215
        kwargs['width'] = 75
        kwargs['height'] = 65
        super().__init__(**kwargs)
