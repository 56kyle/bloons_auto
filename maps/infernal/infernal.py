from map import Map


class Infernal(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'infernal'
        self.difficulty = 'expert'

