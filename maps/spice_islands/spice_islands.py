from map import Map


class SpiceIslands(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'spice_islands'
        self.difficulty = 'intermediate'

