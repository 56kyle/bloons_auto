


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AppInfo:

    offsets = {'<appId>k__BackingField': 16, '<appKey>k__BackingField': 24, '<clientId>k__BackingField': 32, '<clientKey>k__BackingField': 40, '<debug>k__BackingField': 48}    
    def __init__(self, <appId>k__BackingField: System.String, <appKey>k__BackingField: System.String, <clientId>k__BackingField: System.String, <clientKey>k__BackingField: System.String, <debug>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<appId>k__BackingField = <appId>k__BackingField
		self.<appKey>k__BackingField = <appKey>k__BackingField
		self.<clientId>k__BackingField = <clientId>k__BackingField
		self.<clientKey>k__BackingField = <clientKey>k__BackingField
		self.<debug>k__BackingField = <debug>k__BackingField


class MainThreadDispatcher:
	OBJECT_NAME: System.String
    offsets = {'OBJECT_NAME': 0, 's_Callbacks': 8, 's_CallbacksPending': 16}    
    def __init__(self, OBJECT_NAME: System.String, s_Callbacks: System.Collections.Generic.List<System.Action>, s_CallbacksPending: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.OBJECT_NAME = OBJECT_NAME
		self.s_Callbacks = s_Callbacks
		self.s_CallbacksPending = s_CallbacksPending