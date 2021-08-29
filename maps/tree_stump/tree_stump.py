from map import Map


class TreeStump(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'tree_stump'
        self.difficulty = 'beginner'

