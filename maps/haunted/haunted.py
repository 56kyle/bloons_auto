from map import Map


class Haunted(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'haunted'
        self.difficulty = 'intermediate'

