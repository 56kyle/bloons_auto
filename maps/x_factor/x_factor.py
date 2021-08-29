from map import Map


class XFactor(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'x_factor'
        self.difficulty = 'advanced'

