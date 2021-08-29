from map import Map


class Workshop(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'workshop'
        self.difficulty = 'expert'

