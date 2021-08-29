from map import Map


class Encrypted(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'encrypted'
        self.difficulty = 'intermediate'

