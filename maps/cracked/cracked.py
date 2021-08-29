from map import Map


class Cracked(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'cracked'
        self.difficulty = 'intermediate'

