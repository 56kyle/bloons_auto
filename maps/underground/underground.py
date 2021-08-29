from map import Map


class Underground(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'underground'
        self.difficulty = 'advanced'

