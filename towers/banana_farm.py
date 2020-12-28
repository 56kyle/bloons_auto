from tower import Tower


class BananaFarm(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'banana_farm'
        kwargs['range'] = 215
        kwargs['width'] = 162
        kwargs['height'] = 141
        super().__init__(**kwargs)
