from map import Map


class FiringRange(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'firing_range'
        self.difficulty = 'intermediate'

