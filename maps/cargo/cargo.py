from map import Map


class Cargo(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'cargo'
        self.difficulty = 'advanced'

