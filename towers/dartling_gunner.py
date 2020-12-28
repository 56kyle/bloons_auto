from tower import Tower


class DartlingGunner(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'dartling_gunner'
        kwargs['range'] = 107
        kwargs['width'] = 75
        kwargs['height'] = 65
        super().__init__(**kwargs)
