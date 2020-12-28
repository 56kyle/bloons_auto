from tower import Tower


class SpikeFactory(Tower):
    def __init__(self, **kwargs):
        kwargs['name'] = 'spike_factory'
        kwargs['range'] = 183
        kwargs['width'] = 87
        kwargs['height'] = 75
        super().__init__(**kwargs)
