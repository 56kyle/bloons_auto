from map import Map


class MuddyPuddles(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'muddy_puddles'
        self.difficulty = 'expert'

