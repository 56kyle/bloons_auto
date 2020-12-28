from tower import Tower


class Druid(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'druid'
        kwargs['range'] = 188
        kwargs['width'] = 75
        kwargs['height'] = 65
        super().__init__(**kwargs)
