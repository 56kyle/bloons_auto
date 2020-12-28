from tower import Tower


class Alchemist(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'alchemist'
        kwargs['range'] = 242
        kwargs['width'] = 65
        kwargs['height'] = 57
        super().__init__(**kwargs)
