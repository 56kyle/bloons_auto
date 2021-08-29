from map import Map


class Cubism(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'cubism'
        self.difficulty = 'beginner'

