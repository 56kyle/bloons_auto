from map import Map


class Skates(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'skates'
        self.difficulty = 'beginner'

