from map import Map


class Spillway(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'spillway'
        self.difficulty = 'advanced'

