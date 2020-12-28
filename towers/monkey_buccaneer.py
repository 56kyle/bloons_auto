from tower import Tower


class MonkeyBuccaneer(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'monkey_buccaneer'
        kwargs['range'] = 323
        kwargs['aquatic'] = True
        kwargs['width'] = 87
        kwargs['height'] = 75
        super().__init__(**kwargs)
