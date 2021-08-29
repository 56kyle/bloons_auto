from map import Map


class AlpineRun(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'alpine_run'
        self.difficulty = 'beginner'

