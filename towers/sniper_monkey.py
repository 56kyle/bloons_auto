from tower import Tower


class SniperMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'sniper_monkey'
        kwargs['range'] = 107
        kwargs['width'] = 65
        kwargs['height'] = 57
        super().__init__(**kwargs)
