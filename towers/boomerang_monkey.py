from tower import Tower


class BoomerangMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'boomerang_monkey'
        kwargs['range'] = 231
        kwargs['width'] = 75
        kwargs['height'] = 65
        super().__init__(**kwargs)
