


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WindZone:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WindZoneMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__