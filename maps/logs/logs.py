from map import Map


class Logs(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'logs'
        self.difficulty = 'beginner'

