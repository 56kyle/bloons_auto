from map import Map


class BloodyPuddles(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'bloody_puddles'
        self.difficulty = 'expert'

