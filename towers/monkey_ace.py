from tower import Tower


class MonkeyAce(Tower):
    name = 'monkey_ace'
    range = 118
    width = 152
    height = 85

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
