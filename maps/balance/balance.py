from map import Map


class Balance(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'balance'
        self.difficulty = 'intermediate'

