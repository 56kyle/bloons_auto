from map import Map


class Hedge(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'hedge'
        self.difficulty = 'beginner'

