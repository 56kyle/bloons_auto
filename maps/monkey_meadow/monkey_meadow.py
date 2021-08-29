from map import Map


class MonkeyMeadow(Map):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'monkey_meadow'
        self.difficulty = 'beginner'

