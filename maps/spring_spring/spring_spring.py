from map import Map


class SpringSpring(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'spring_spring'
        self.difficulty = 'intermediate'

