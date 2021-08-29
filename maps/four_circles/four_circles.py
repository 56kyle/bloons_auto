from map import Map


class FourCircles(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'four_circles'
        self.difficulty = 'beginner'

