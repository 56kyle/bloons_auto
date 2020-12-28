from tower import Tower


class BombShooter(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'bomb_shooter'
        kwargs['range'] = 215
        kwargs['width'] = 75
        kwargs['height'] = 65
        super().__init__(**kwargs)
