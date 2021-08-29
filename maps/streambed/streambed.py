from map import Map


class Streambed(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'streambed'
        self.difficulty = 'intermediate'

