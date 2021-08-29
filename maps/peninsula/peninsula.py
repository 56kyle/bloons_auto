from map import Map


class Peninsula(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'peninsula'
        self.difficulty = 'advanced'

