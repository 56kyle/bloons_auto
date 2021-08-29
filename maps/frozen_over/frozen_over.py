from map import Map


class FrozenOver(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'frozen_over'
        self.difficulty = 'beginner'

