from map import Map


class Carved(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'carved'
        self.difficulty = 'beginner'

