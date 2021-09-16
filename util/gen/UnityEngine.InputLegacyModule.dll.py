


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class HitInfo:

    offsets = {'target': 16, 'camera': 24}    
    def __init__(self, target: UnityEngine.GameObject, camera: UnityEngine.Camera, **kwargs):
        super().__init__(self, **kwargs)
		self.target = target
		self.camera = camera


class CameraRaycastHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IMECompositionMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Input:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SendMouseEvents:
	s_MouseUsed: System.Boolean
    offsets = {'s_MouseUsed': 0}    
    def __init__(self, s_MouseUsed: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.s_MouseUsed = s_MouseUsed


class Touch:

    offsets = {'m_FingerId': 16, 'm_Position': 20, 'm_RawPosition': 28, 'm_PositionDelta': 36, 'm_TimeDelta': 44, 'm_TapCount': 48, 'm_Phase': 52, 'm_Type': 56, 'm_Pressure': 60, 'm_maximumPossiblePressure': 64, 'm_Radius': 68, 'm_RadiusVariance': 72, 'm_AltitudeAngle': 76, 'm_AzimuthAngle': 80}    
    def __init__(self, m_FingerId: System.Int32, m_Position: UnityEngine.Vector2, m_RawPosition: UnityEngine.Vector2, m_PositionDelta: UnityEngine.Vector2, m_TimeDelta: System.Single, m_TapCount: System.Int32, m_Phase: UnityEngine.TouchPhase, m_Type: UnityEngine.TouchType, m_Pressure: System.Single, m_maximumPossiblePressure: System.Single, m_Radius: System.Single, m_RadiusVariance: System.Single, m_AltitudeAngle: System.Single, m_AzimuthAngle: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_FingerId = m_FingerId
		self.m_Position = m_Position
		self.m_RawPosition = m_RawPosition
		self.m_PositionDelta = m_PositionDelta
		self.m_TimeDelta = m_TimeDelta
		self.m_TapCount = m_TapCount
		self.m_Phase = m_Phase
		self.m_Type = m_Type
		self.m_Pressure = m_Pressure
		self.m_maximumPossiblePressure = m_maximumPossiblePressure
		self.m_Radius = m_Radius
		self.m_RadiusVariance = m_RadiusVariance
		self.m_AltitudeAngle = m_AltitudeAngle
		self.m_AzimuthAngle = m_AzimuthAngle


class TouchPhase:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TouchType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__