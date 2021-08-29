from map import Map


class Downstream(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'downstream'
        self.difficulty = 'intermediate'

