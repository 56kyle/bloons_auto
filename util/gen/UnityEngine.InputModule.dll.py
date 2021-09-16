


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeInputEventBuffer:

    offsets = {'eventCount': 24, 'sizeInBytes': 28, 'capacityInBytes': 32}    
    def __init__(self, eventCount: System.Int32, sizeInBytes: System.Int32, capacityInBytes: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.eventCount = eventCount
		self.sizeInBytes = sizeInBytes
		self.capacityInBytes = capacityInBytes


class NativeInputSystem:
	onUpdate: UnityEngineInternal.Input.NativeUpdateCallback
    offsets = {'onUpdate': 0, 'onBeforeUpdate': 8, 'onShouldRunUpdate': 16, 's_OnDeviceDiscoveredCallback': 24}    
    def __init__(self, onUpdate: UnityEngineInternal.Input.NativeUpdateCallback, onBeforeUpdate: System.Action<UnityEngineInternal.Input.NativeInputUpdateType>, onShouldRunUpdate: System.Func<UnityEngineInternal.Input.NativeInputUpdateType,System.Boolean>, s_OnDeviceDiscoveredCallback: System.Action<System.Int32,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.onUpdate = onUpdate
		self.onBeforeUpdate = onBeforeUpdate
		self.onShouldRunUpdate = onShouldRunUpdate
		self.s_OnDeviceDiscoveredCallback = s_OnDeviceDiscoveredCallback


class NativeInputUpdateType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class NativeUpdateCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
