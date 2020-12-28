from tower import Tower


class HeliPilot(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'heli_pilot'
        kwargs['range'] = 118
        kwargs['width'] = 145
        kwargs['height'] = 125
        super().__init__(**kwargs)
