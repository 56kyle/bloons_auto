from map import Map


class BloonariusPrime(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'bloonarius_prime'
        self.difficulty = 'intermediate'

