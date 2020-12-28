from tower import Tower


class MonkeySub(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'monkey_sub'
        kwargs['range'] = 226
        kwargs['aquatic'] = True
        kwargs['width'] = 75
        kwargs['height'] = 65
        super().__init__(**kwargs)
