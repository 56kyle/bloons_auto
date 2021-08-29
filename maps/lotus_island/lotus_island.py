from map import Map


class LotusIsland(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'lotus_island'
        self.difficulty = 'beginner'

