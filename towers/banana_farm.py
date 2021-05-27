from tower import Tower


class BananaFarm(Tower):
    name = 'banana_farm'
    range = 215
    width = 162
    height = 141

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
