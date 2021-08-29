from map import Map


class AdorasTemple(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'adoras_temple'
        self.difficulty = 'intermediate'

