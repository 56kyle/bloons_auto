from map import Map


class Ravine(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'ravine'
        self.difficulty = 'expert'

