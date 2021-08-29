from map import Map


class Resort(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'resort'
        self.difficulty = 'beginner'

