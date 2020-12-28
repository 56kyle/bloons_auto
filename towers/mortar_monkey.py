from tower import Tower


class MortarMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'mortar_monkey'
        kwargs['range'] = 161
        kwargs['width'] = 119
        kwargs['height'] = 103
        super().__init__(**kwargs)

