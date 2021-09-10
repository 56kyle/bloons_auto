from map import Map


class Ouch(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'ouch'
        self.difficulty = 'expert'
        self.page = 2
        self.placement = [0, 0]

