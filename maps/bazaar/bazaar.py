from map import Map


class Bazaar(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'bazaar'
        self.difficulty = 'intermediate'

