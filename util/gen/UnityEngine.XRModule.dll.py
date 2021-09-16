


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TrackingStateEventType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class XRMirrorViewBlitDesc:

    offsets = {'displaySubsystemInstance': 16, 'nativeBlitAvailable': 24, 'nativeBlitInvalidStates': 25, 'blitParamsCount': 28}    
    def __init__(self, displaySubsystemInstance: System.IntPtr, nativeBlitAvailable: System.Boolean, nativeBlitInvalidStates: System.Boolean, blitParamsCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.displaySubsystemInstance = displaySubsystemInstance
		self.nativeBlitAvailable = nativeBlitAvailable
		self.nativeBlitInvalidStates = nativeBlitInvalidStates
		self.blitParamsCount = blitParamsCount


class XRRenderPass:

    offsets = {'displaySubsystemInstance': 16, 'renderPassIndex': 24, 'renderTarget': 32, 'renderTargetDesc': 72, 'shouldFillOutDepth': 124, 'cullingPassIndex': 128}    
    def __init__(self, displaySubsystemInstance: System.IntPtr, renderPassIndex: System.Int32, renderTarget: UnityEngine.Rendering.RenderTargetIdentifier, renderTargetDesc: UnityEngine.RenderTextureDescriptor, shouldFillOutDepth: System.Boolean, cullingPassIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.displaySubsystemInstance = displaySubsystemInstance
		self.renderPassIndex = renderPassIndex
		self.renderTarget = renderTarget
		self.renderTargetDesc = renderTargetDesc
		self.shouldFillOutDepth = shouldFillOutDepth
		self.cullingPassIndex = cullingPassIndex


class AvailableTrackingData:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Bone:

    offsets = {'m_DeviceId': 16, 'm_FeatureIndex': 24}    
    def __init__(self, m_DeviceId: System.UInt64, m_FeatureIndex: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DeviceId = m_DeviceId
		self.m_FeatureIndex = m_FeatureIndex


class ConnectionChangeType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Eyes:

    offsets = {'m_DeviceId': 16, 'm_FeatureIndex': 24}    
    def __init__(self, m_DeviceId: System.UInt64, m_FeatureIndex: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DeviceId = m_DeviceId
		self.m_FeatureIndex = m_FeatureIndex


class Hand:

    offsets = {'m_DeviceId': 16, 'm_FeatureIndex': 24}    
    def __init__(self, m_DeviceId: System.UInt64, m_FeatureIndex: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DeviceId = m_DeviceId
		self.m_FeatureIndex = m_FeatureIndex


class HashCodeHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class InputDevice:

    offsets = {'m_DeviceId': 16, 'm_Initialized': 24}    
    def __init__(self, m_DeviceId: System.UInt64, m_Initialized: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DeviceId = m_DeviceId
		self.m_Initialized = m_Initialized


class InputDevices:
	deviceConnected: System.Action<UnityEngine.XR.InputDevice>
    offsets = {'deviceConnected': 0, 'deviceDisconnected': 8, 'deviceConfigChanged': 16}    
    def __init__(self, deviceConnected: System.Action<UnityEngine.XR.InputDevice>, deviceDisconnected: System.Action<UnityEngine.XR.InputDevice>, deviceConfigChanged: System.Action<UnityEngine.XR.InputDevice>, **kwargs):
        super().__init__(self, **kwargs)
		self.deviceConnected = deviceConnected
		self.deviceDisconnected = deviceDisconnected
		self.deviceConfigChanged = deviceConfigChanged


class InputFeatureType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class InputFeatureUsage:

    offsets = {'m_Name': 16, 'm_InternalType': 24}    
    def __init__(self, m_Name: System.String, m_InternalType: UnityEngine.XR.InputFeatureType, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Name = m_Name
		self.m_InternalType = m_InternalType


class InputTracking:
	trackingAcquired: System.Action<UnityEngine.XR.XRNodeState>
    offsets = {'trackingAcquired': 0, 'trackingLost': 8, 'nodeAdded': 16, 'nodeRemoved': 24}    
    def __init__(self, trackingAcquired: System.Action<UnityEngine.XR.XRNodeState>, trackingLost: System.Action<UnityEngine.XR.XRNodeState>, nodeAdded: System.Action<UnityEngine.XR.XRNodeState>, nodeRemoved: System.Action<UnityEngine.XR.XRNodeState>, **kwargs):
        super().__init__(self, **kwargs)
		self.trackingAcquired = trackingAcquired
		self.trackingLost = trackingLost
		self.nodeAdded = nodeAdded
		self.nodeRemoved = nodeRemoved


class MeshGenerationResult:

    offsets = {'<MeshId>k__BackingField': 16, '<Mesh>k__BackingField': 32, '<MeshCollider>k__BackingField': 40, '<Status>k__BackingField': 48, '<Attributes>k__BackingField': 52}    
    def __init__(self, <MeshId>k__BackingField: UnityEngine.XR.MeshId, <Mesh>k__BackingField: UnityEngine.Mesh, <MeshCollider>k__BackingField: UnityEngine.MeshCollider, <Status>k__BackingField: UnityEngine.XR.MeshGenerationStatus, <Attributes>k__BackingField: UnityEngine.XR.MeshVertexAttributes, **kwargs):
        super().__init__(self, **kwargs)
		self.<MeshId>k__BackingField = <MeshId>k__BackingField
		self.<Mesh>k__BackingField = <Mesh>k__BackingField
		self.<MeshCollider>k__BackingField = <MeshCollider>k__BackingField
		self.<Status>k__BackingField = <Status>k__BackingField
		self.<Attributes>k__BackingField = <Attributes>k__BackingField


class MeshGenerationStatus:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class MeshId:
	s_InvalidId: UnityEngine.XR.MeshId
    offsets = {'s_InvalidId': 0, 'm_SubId1': 16, 'm_SubId2': 24}    
    def __init__(self, s_InvalidId: UnityEngine.XR.MeshId, m_SubId1: System.UInt64, m_SubId2: System.UInt64, **kwargs):
        super().__init__(self, **kwargs)
		self.s_InvalidId = s_InvalidId
		self.m_SubId1 = m_SubId1
		self.m_SubId2 = m_SubId2


class MeshVertexAttributes:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class XRDisplaySubsystem:
	displayFocusChanged: System.Action<System.Boolean>
    offsets = {'displayFocusChanged': 0}    
    def __init__(self, displayFocusChanged: System.Action<System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.displayFocusChanged = displayFocusChanged


class XRDisplaySubsystemDescriptor:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XRInputSubsystem:

    offsets = {'trackingOriginUpdated': 32, 'boundaryChanged': 40}    
    def __init__(self, trackingOriginUpdated: System.Action<UnityEngine.XR.XRInputSubsystem>, boundaryChanged: System.Action<UnityEngine.XR.XRInputSubsystem>, **kwargs):
        super().__init__(self, **kwargs)
		self.trackingOriginUpdated = trackingOriginUpdated
		self.boundaryChanged = boundaryChanged


class XRInputSubsystemDescriptor:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XRMeshSubsystem:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XRMeshSubsystemDescriptor:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XRNode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class XRNodeState:

    offsets = {'m_Type': 16, 'm_AvailableFields': 20, 'm_Position': 24, 'm_Rotation': 36, 'm_Velocity': 52, 'm_AngularVelocity': 64, 'm_Acceleration': 76, 'm_AngularAcceleration': 88, 'm_Tracked': 100, 'm_UniqueID': 104}    
    def __init__(self, m_Type: UnityEngine.XR.XRNode, m_AvailableFields: UnityEngine.XR.AvailableTrackingData, m_Position: UnityEngine.Vector3, m_Rotation: UnityEngine.Quaternion, m_Velocity: UnityEngine.Vector3, m_AngularVelocity: UnityEngine.Vector3, m_Acceleration: UnityEngine.Vector3, m_AngularAcceleration: UnityEngine.Vector3, m_Tracked: System.Int32, m_UniqueID: System.UInt64, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Type = m_Type
		self.m_AvailableFields = m_AvailableFields
		self.m_Position = m_Position
		self.m_Rotation = m_Rotation
		self.m_Velocity = m_Velocity
		self.m_AngularVelocity = m_AngularVelocity
		self.m_Acceleration = m_Acceleration
		self.m_AngularAcceleration = m_AngularAcceleration
		self.m_Tracked = m_Tracked
		self.m_UniqueID = m_UniqueID