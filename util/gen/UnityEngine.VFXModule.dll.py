


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VFXEventAttribute:

    offsets = {'m_Ptr': 16, 'm_Owner': 24, 'm_VfxAsset': 32}    
    def __init__(self, m_Ptr: System.IntPtr, m_Owner: System.Boolean, m_VfxAsset: UnityEngine.VFX.VisualEffectAsset, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_Owner = m_Owner
		self.m_VfxAsset = m_VfxAsset


class VFXExpressionMesh:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VFXExpressionNoise:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VFXExpressionValues:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class VFXManager:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VFXSpawnerCallbacks:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VFXSpawnerState:

    offsets = {'m_Ptr': 16, 'm_Owner': 24}    
    def __init__(self, m_Ptr: System.IntPtr, m_Owner: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_Owner = m_Owner


class VisualEffect:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VisualEffectAsset:
	PlayEventID: System.Int32
    offsets = {'PlayEventID': 0, 'StopEventID': 4}    
    def __init__(self, PlayEventID: System.Int32, StopEventID: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.PlayEventID = PlayEventID
		self.StopEventID = StopEventID


class VisualEffectObject:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
