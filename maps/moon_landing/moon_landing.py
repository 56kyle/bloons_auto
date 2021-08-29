from map import Map


class MoonLanding(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'moon_landing'
        self.difficulty = 'intermediate'

