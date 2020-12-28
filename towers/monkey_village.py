from tower import Tower


class MonkeyVillage(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'monkey_village'
        kwargs['range'] = 215
        kwargs['width'] = 119
        kwargs['height'] = 103
        super().__init__(**kwargs)
