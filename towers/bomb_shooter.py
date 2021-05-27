from tower import Tower


class BombShooter(Tower):
    name = 'bomb_shooter'
    range = 215
    width = 75
    height = 65

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
