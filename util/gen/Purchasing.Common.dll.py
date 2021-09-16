


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Parser:

    offsets = {'json': 16}    
    def __init__(self, json: System.IO.StringReader, **kwargs):
        super().__init__(self, **kwargs)
		self.json = json


class TOKEN:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Serializer:

    offsets = {'builder': 16}    
    def __init__(self, builder: System.Text.StringBuilder, **kwargs):
        super().__init__(self, **kwargs)
		self.builder = builder


class INativeStore:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MiniJson:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Json:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
