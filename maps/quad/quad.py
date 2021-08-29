from map import Map


class Quad(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'quad'
        self.difficulty = 'expert'

