from map import Map


class PatsPond(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'pats_pond'
        self.difficulty = 'advanced'

