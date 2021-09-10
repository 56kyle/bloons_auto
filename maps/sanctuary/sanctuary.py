from map import Map


class Sanctuary(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'sanctuary'
        self.difficulty = 'expert'
        self.page = 1
        self.placement = [0, 1]

