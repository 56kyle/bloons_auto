from tower import Tower


class MonkeyAce(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'monkey_ace'
        kwargs['range'] = 118
        kwargs['width'] = 152
        kwargs['height'] = 85
        super().__init__(**kwargs)
