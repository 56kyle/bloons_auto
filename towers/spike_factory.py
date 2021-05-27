from tower import Tower


class SpikeFactory(Tower):
    name = 'spike_factory'
    range = 183
    width = 87
    height = 75

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
