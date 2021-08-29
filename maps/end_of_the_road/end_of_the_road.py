from map import Map


class EndOfTheRoad(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'end_of_the_road'
        self.difficulty = 'beginner'

