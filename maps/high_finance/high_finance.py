from map import Map


class HighFinance(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'high_finance'
        self.difficulty = 'advanced'

