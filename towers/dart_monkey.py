from tower import Tower


class DartMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'dart_monkey'
        kwargs['range'] = 172
        kwargs['width'] = 65
        kwargs['height'] = 57
        super().__init__(**kwargs)
