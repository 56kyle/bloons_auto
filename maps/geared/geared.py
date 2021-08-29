from map import Map


class Geared(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'geared'
        self.difficulty = 'advanced'

