from tower import Tower


class SuperMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'super_monkey'
        kwargs['range'] = 269
        kwargs['width'] = 119
        kwargs['height'] = 103
        super().__init__(**kwargs)
