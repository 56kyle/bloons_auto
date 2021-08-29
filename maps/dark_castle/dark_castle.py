from map import Map


class DarkCastle(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'dark_castle'
        self.difficulty = 'expert'

