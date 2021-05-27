from tower import Tower


class HeliPilot(Tower):
    name = 'heli_pilot'
    range = 118
    width = 145
    height = 127

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
