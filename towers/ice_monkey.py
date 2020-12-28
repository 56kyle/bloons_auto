from tower import Tower


class IceMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'ice_monkey'
        kwargs['range'] = 123
        kwargs['width'] = 65
        kwargs['height'] = 57
        super().__init__(**kwargs)
