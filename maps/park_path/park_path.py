from map import Map


class ParkPath(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'park_path'
        self.difficulty = 'beginner'

