from tower import Tower


class TackShooter(Tower):
    name = 'tack_shooter'
    range = 123
    width = 65
    height = 57

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
