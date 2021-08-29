from map import Map


class AnotherBrick(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'another_brick'
        self.difficulty = 'advanced'

