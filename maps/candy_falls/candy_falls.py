from map import Map


class CandyFalls(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'candy_falls'
        self.difficulty = 'beginner'

