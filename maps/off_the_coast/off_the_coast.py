from map import Map


class OffTheCoast(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'off_the_coast'
        self.difficulty = 'advanced'

