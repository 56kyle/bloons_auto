from map import Map


class KartsNDarts(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'kartsndarts'
        self.difficulty = 'intermediate'

