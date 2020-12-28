from tower import Tower


class NinjaMonkey(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'ninja_monkey'
        kwargs['range'] = 215
        kwargs['width'] = 65
        kwargs['height'] = 57
        super().__init__(**kwargs)
