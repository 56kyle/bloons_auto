from tower import Tower


class TackShooter(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'tack_shooter'
        kwargs['range'] = 123
        kwargs['width'] = 65
        kwargs['height'] = 57
        super().__init__(**kwargs)
