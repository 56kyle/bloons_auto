from map import Map


class Chutes(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'chutes'
        self.difficulty = 'intermediate'

