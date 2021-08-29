from map import Map


class Rake(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'rake'
        self.difficulty = 'intermediate'

