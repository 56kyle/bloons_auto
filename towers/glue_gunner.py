from tower import Tower


class GlueGunner(Tower):
    name = 'glue_gunner'
    range = 247
    width = 65
    height = 57

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
