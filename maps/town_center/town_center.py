from map import Map


class TownCenter(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'town_center'
        self.difficulty = 'beginner'

