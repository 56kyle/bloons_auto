from map import Map


class Cornfield(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'cornfield'
        self.difficulty = 'advanced'

