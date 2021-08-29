from map import Map


class WinterPark(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'winter_park'
        self.difficulty = 'beginner'

