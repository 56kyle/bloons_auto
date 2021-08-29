from map import Map


class InTheLoop(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'in_the_loop'
        self.difficulty = 'beginner'

