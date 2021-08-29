from map import Map


class FloodedValley(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'flooded_valley'
        self.difficulty = 'expert'

