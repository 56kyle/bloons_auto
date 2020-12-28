from tower import Tower


class GlueGunner(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'glue_gunner'
        kwargs['range'] = 247
        kwargs['width'] = 65
        kwargs['height'] = 57
        super().__init__(**kwargs)
