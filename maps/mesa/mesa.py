from map import Map


class Mesa(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'mesa'
        self.difficulty = 'advanced'

