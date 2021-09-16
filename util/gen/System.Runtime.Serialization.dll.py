


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DataContractAttribute:

    offsets = {'isReference': 16}    
    def __init__(self, isReference: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.isReference = isReference


class DataMemberAttribute:

    offsets = {'name': 16, 'isNameSetExplicitly': 24, 'order': 28, 'isRequired': 32, 'emitDefaultValue': 33}    
    def __init__(self, name: System.String, isNameSetExplicitly: System.Boolean, order: System.Int32, isRequired: System.Boolean, emitDefaultValue: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.name = name
		self.isNameSetExplicitly = isNameSetExplicitly
		self.order = order
		self.isRequired = isRequired
		self.emitDefaultValue = emitDefaultValue


class EnumMemberAttribute:

    offsets = {'value': 16}    
    def __init__(self, value: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value


class KnownTypeAttribute:

    offsets = {'type': 16}    
    def __init__(self, type: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.type = type