


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AlignOfHelper<T>:

    offsets = {'dummy': 0, 'data': 0}    
    def __init__(self, dummy: System.Byte, data: T, **kwargs):
        super().__init__(self, **kwargs)
		self.dummy = dummy
		self.data = data


class Enumerator<T>:

    offsets = {'m_Array': 0, 'm_Index': 0}    
    def __init__(self, m_Array: Unity.Collections.NativeArray<T>, m_Index: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Array = m_Array
		self.m_Index = m_Index


class Enumerator<T>:

    offsets = {'m_Array': 0, 'm_Index': 0}    
    def __init__(self, m_Array: Unity.Collections.NativeSlice<T>, m_Index: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Array = m_Array
		self.m_Index = m_Index


class JobScheduleParameters:

    offsets = {'Dependency': 16, 'ScheduleMode': 32, 'ReflectionData': 40, 'JobDataPtr': 48}    
    def __init__(self, Dependency: Unity.Jobs.JobHandle, ScheduleMode: System.Int32, ReflectionData: System.IntPtr, JobDataPtr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.Dependency = Dependency
		self.ScheduleMode = ScheduleMode
		self.ReflectionData = ReflectionData
		self.JobDataPtr = JobDataPtr


class AutoScope:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class LogCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LowMemoryCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OrderBlock:

    offsets = {'order': 16, 'callback': 24}    
    def __init__(self, order: System.Int32, callback: UnityEngine.Events.UnityAction, **kwargs):
        super().__init__(self, **kwargs)
		self.order = order
		self.callback = callback


class CameraCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GateFitMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GateFitParameters:

    offsets = {'<mode>k__BackingField': 16, '<aspect>k__BackingField': 20}    
    def __init__(self, <mode>k__BackingField: UnityEngine.Camera.GateFitMode, <aspect>k__BackingField: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.<mode>k__BackingField = <mode>k__BackingField
		self.<aspect>k__BackingField = <aspect>k__BackingField


class MonoOrStereoscopicEye:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ProjectionMatrixMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class StereoscopicEye:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class StateChanged:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DisplaysUpdatedDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c:
	<>9: UnityEngine.Experimental.GlobalIllumination.Lightmapping.<>c
    offsets = {'<>9': 0}    
    def __init__(self, <>9: UnityEngine.Experimental.GlobalIllumination.Lightmapping.<>c, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9


class RequestLightsDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateFunction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c__DisplayClass12_0:

    offsets = {'messageId': 16}    
    def __init__(self, messageId: System.Guid, **kwargs):
        super().__init__(self, **kwargs)
		self.messageId = messageId


class <>c__DisplayClass13_0:

    offsets = {'messageId': 16}    
    def __init__(self, messageId: System.Guid, **kwargs):
        super().__init__(self, **kwargs)
		self.messageId = messageId


class <>c__DisplayClass20_0:

    offsets = {'msgReceived': 16}    
    def __init__(self, msgReceived: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.msgReceived = msgReceived


class <>c__DisplayClass6_0:

    offsets = {'messageId': 16}    
    def __init__(self, messageId: System.Guid, **kwargs):
        super().__init__(self, **kwargs)
		self.messageId = messageId


class <>c__DisplayClass7_0:

    offsets = {'messageId': 16}    
    def __init__(self, messageId: System.Guid, **kwargs):
        super().__init__(self, **kwargs)
		self.messageId = messageId


class <>c__DisplayClass8_0:

    offsets = {'messageId': 16}    
    def __init__(self, messageId: System.Guid, **kwargs):
        super().__init__(self, **kwargs)
		self.messageId = messageId


class ConnectionChangeEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MessageEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MessageTypeSubscribers:

    offsets = {'m_messageTypeId': 16, 'subscriberCount': 24, 'messageCallback': 32}    
    def __init__(self, m_messageTypeId: System.String, subscriberCount: System.Int32, messageCallback: UnityEngine.Networking.PlayerConnection.PlayerEditorConnectionEvents.MessageEvent, **kwargs):
        super().__init__(self, **kwargs)
		self.m_messageTypeId = m_messageTypeId
		self.subscriberCount = subscriberCount
		self.messageCallback = messageCallback


class Flags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CreateOutputMethod:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AnalyticsCoreStatsUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ClearIntermediateRenderers:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ClearLines:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DeliverIosPlatformEvents:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DispatchEventQueueEvents:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ExecuteMainThreadJobs:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GpuTimestamp:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PerformanceAnalyticsUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhysicsResetInterpolatedTransformPosition:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerCleanupCachedData:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PollHtcsPlayerConnection:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PollPlayerConnection:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PresentBeforeUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProcessMouseInWindow:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProcessRemoteInput:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProfilerStartFrame:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RendererNotifyInvisible:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ResetFrameStatsAfterPresent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptRunDelayedStartupFrame:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SpriteAtlasManagerUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TangoUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityWebRequestUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateAsyncReadbackManager:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateCanvasRectTransform:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateInputManager:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateKinect:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateMainGameViewRect:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdatePreloading:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateStreamingManager:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateTextureStreamingManager:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XRUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ClearLines:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorFixedSampleTime:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorFixedUpdatePostPhysics:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LegacyFixedAnimationUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NewInputFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Physics2DFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhysicsClothFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhysicsFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptRunBehaviourFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptRunDelayedFixedFrameRate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XRFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AsyncUploadTimeSlicedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorSampleTime:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerUpdateTime:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SynchronizeInputs:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SynchronizeState:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XREarlyUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class BatchModeUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ClearImmediateRenderers:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorLateUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorRenderImage:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EndGraphicsJobsAfterScriptLateUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EnlightenRuntimeUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ExecuteGameCenterCallbacks:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FinishFrameRendering:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GUIClearEvents:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class InputEndFrame:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MemoryFrameMaintenance:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ParticleSystemEndUpdateAll:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhysicsSkinnedClothBeginUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhysicsSkinnedClothFinishUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerEmitCanvasGeometry:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerSendFrameComplete:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerSendFramePostPresent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerSendFrameStarted:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerUpdateCanvases:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PresentAfterDraw:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProcessWebSendMessages:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProfilerEndFrame:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProfilerSynchronizeStats:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ResetInputAxis:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptRunDelayedDynamicFrameRate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ShaderHandleErrors:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SortingGroupsUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ThreadedLoadingDebug:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TriggerEndOfFrameCallbacks:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateAllRenderers:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateAllSkinnedMeshes:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateAudio:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateCanvasRectTransform:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateCaptureScreenshot:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateCustomRenderTextures:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateRectTransform:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateResolution:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateSubstance:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateVideo:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateVideoTextures:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VFXUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XRPostPresent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AIUpdatePostScript:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ConstraintManagerUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorDeferredEvaluate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorUpdateAnimationBegin:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorUpdateAnimationEnd:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EndGraphicsJobsAfterScriptUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LegacyAnimationUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ParticleSystemBeginUpdateAll:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptRunBehaviourLateUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UNetUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateMasterServerInterface:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateNetworkManager:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AIUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CheckTexFieldInput:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IMGUISendQueuedEvents:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NewInputUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Physics2DUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhysicsUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SendMouseEvents:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UpdateVideo:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WindUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DirectorUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptRunBehaviourUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptRunDelayedDynamicFrameRate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptRunDelayedTasks:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Axis:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Edge:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ReapplyDrivenProperties:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ReflectionProbeEvent:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class OnPerformCulling:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <layerCullDistances>e__FixedBuffer:

    offsets = {'FixedElementField': 16}    
    def __init__(self, FixedElementField: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.FixedElementField = FixedElementField


class <m_CameraCullPlanes>e__FixedBuffer:

    offsets = {'FixedElementField': 16}    
    def __init__(self, FixedElementField: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.FixedElementField = FixedElementField


class <m_ShadowCullPlanes>e__FixedBuffer:

    offsets = {'FixedElementField': 16}    
    def __init__(self, FixedElementField: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.FixedElementField = FixedElementField


class <m_CullingPlanes>e__FixedBuffer:

    offsets = {'FixedElementField': 16}    
    def __init__(self, FixedElementField: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.FixedElementField = FixedElementField


class <m_LayerFarCullDistances>e__FixedBuffer:

    offsets = {'FixedElementField': 16}    
    def __init__(self, FixedElementField: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.FixedElementField = FixedElementField


class LightmapMixedBakeModes:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ReflectionProbeModes:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TestClass:

    offsets = {'value': 16}    
    def __init__(self, value: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value


class CreateOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Status:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Enumerator:

    offsets = {'outer': 16, 'currentIndex': 24}    
    def __init__(self, outer: UnityEngine.Transform, currentIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.outer = outer
		self.currentIndex = currentIndex


class <>c:
	<>9: UnityEngine.UnhandledExceptionHandler.<>c
    offsets = {'<>9': 0, '<>9__0_0': 8}    
    def __init__(self, <>9: UnityEngine.UnhandledExceptionHandler.<>c, <>9__0_0: System.UnhandledExceptionEventHandler, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__0_0 = <>9__0_0


class WorkRequest:

    offsets = {'m_DelagateCallback': 16, 'm_DelagateState': 24, 'm_WaitHandle': 32}    
    def __init__(self, m_DelagateCallback: System.Threading.SendOrPostCallback, m_DelagateState: System.Object, m_WaitHandle: System.Threading.ManualResetEvent, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DelagateCallback = m_DelagateCallback
		self.m_DelagateState = m_DelagateState
		self.m_WaitHandle = m_WaitHandle


class DictationCompletedDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DictationErrorHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DictationHypothesisDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DictationResultDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ErrorDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class StatusDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhraseRecognizedDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CaptureResultType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class OnCaptureResourceCreatedCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnCapturedToDiskCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnCapturedToMemoryCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnPhotoModeStartedCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnPhotoModeStoppedCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhotoCaptureResult:

    offsets = {'resultType': 16, 'hResult': 24}    
    def __init__(self, resultType: UnityEngine.Windows.WebCam.PhotoCapture.CaptureResultType, hResult: System.Int64, **kwargs):
        super().__init__(self, **kwargs)
		self.resultType = resultType
		self.hResult = hResult


class CaptureResultType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class OnStartedRecordingVideoCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnStoppedRecordingVideoCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnVideoCaptureResourceCreatedCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnVideoModeStartedCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnVideoModeStoppedCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VideoCaptureResult:

    offsets = {'resultType': 16, 'hResult': 24}    
    def __init__(self, resultType: UnityEngine.Windows.WebCam.VideoCapture.CaptureResultType, hResult: System.Int64, **kwargs):
        super().__init__(self, **kwargs)
		self.resultType = resultType
		self.hResult = hResult


class MonoPInvokeCallbackAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Allocator:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DeallocateOnJobCompletionAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeArray<T>:

    offsets = {'m_Length': 0, 'm_AllocatorLabel': 0}    
    def __init__(self, m_Length: System.Int32, m_AllocatorLabel: Unity.Collections.Allocator, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Length = m_Length
		self.m_AllocatorLabel = m_AllocatorLabel


class NativeArrayDebugView<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeArrayOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class NativeDisableParallelForRestrictionAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeFixedLengthAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeLeakDetection:
	s_NativeLeakDetectionMode: System.Int32
    offsets = {'s_NativeLeakDetectionMode': 0}    
    def __init__(self, s_NativeLeakDetectionMode: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.s_NativeLeakDetectionMode = s_NativeLeakDetectionMode


class NativeMatchesParallelForLengthAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeSlice<T>:

    offsets = {'m_Stride': 0, 'm_Length': 0}    
    def __init__(self, m_Stride: System.Int32, m_Length: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Stride = m_Stride
		self.m_Length = m_Length


class NativeSliceDebugView<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ReadOnlyAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WriteOnlyAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeArrayUnsafeUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeContainerAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeContainerIsAtomicWriteOnlyAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeContainerIsReadOnlyAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeContainerNeedsThreadIndexAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeContainerSupportsDeallocateOnJobCompletionAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeContainerSupportsDeferredConvertListToArray:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeContainerSupportsMinMaxWriteRestrictionAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeDisableContainerSafetyRestrictionAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeDisableUnsafePtrRestrictionAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeSetClassTypeToNullOnScheduleAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeSetThreadIndexAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeSliceUnsafeUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnsafeUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WriteAccessRequiredAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class JobHandle:

    offsets = {'jobGroup': 16, 'version': 24}    
    def __init__(self, jobGroup: System.IntPtr, version: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.jobGroup = jobGroup
		self.version = version


class JobsUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProfilerMarker:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class AddComponentMenu:

    offsets = {'m_AddComponentMenu': 16, 'm_Ordering': 24}    
    def __init__(self, m_AddComponentMenu: System.String, m_Ordering: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_AddComponentMenu = m_AddComponentMenu
		self.m_Ordering = m_Ordering


class AnimationCurve:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class Application:
	lowMemory: UnityEngine.Application.LowMemoryCallback
    offsets = {'lowMemory': 0, 's_LogCallbackHandler': 8, 's_LogCallbackHandlerThreaded': 16, 'focusChanged': 24, 'deepLinkActivated': 32, 'wantsToQuit': 40, 'quitting': 48}    
    def __init__(self, lowMemory: UnityEngine.Application.LowMemoryCallback, s_LogCallbackHandler: UnityEngine.Application.LogCallback, s_LogCallbackHandlerThreaded: UnityEngine.Application.LogCallback, focusChanged: System.Action<System.Boolean>, deepLinkActivated: System.Action<System.String>, wantsToQuit: System.Func<System.Boolean>, quitting: System.Action, **kwargs):
        super().__init__(self, **kwargs)
		self.lowMemory = lowMemory
		self.s_LogCallbackHandler = s_LogCallbackHandler
		self.s_LogCallbackHandlerThreaded = s_LogCallbackHandlerThreaded
		self.focusChanged = focusChanged
		self.deepLinkActivated = deepLinkActivated
		self.wantsToQuit = wantsToQuit
		self.quitting = quitting


class AssemblyIsEditorAssembly:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AsyncOperation:

    offsets = {'m_Ptr': 16, 'm_completeCallback': 24}    
    def __init__(self, m_Ptr: System.IntPtr, m_completeCallback: System.Action<UnityEngine.AsyncOperation>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_completeCallback = m_completeCallback


class AttributeHelperEngine:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class BeforeRenderHelper:
	s_OrderBlocks: System.Collections.Generic.List<UnityEngine.BeforeRenderHelper.OrderBlock>
    offsets = {'s_OrderBlocks': 0}    
    def __init__(self, s_OrderBlocks: System.Collections.Generic.List<UnityEngine.BeforeRenderHelper.OrderBlock>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_OrderBlocks = s_OrderBlocks


class Behaviour:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class BoneWeight:

    offsets = {'m_Weight0': 16, 'm_Weight1': 20, 'm_Weight2': 24, 'm_Weight3': 28, 'm_BoneIndex0': 32, 'm_BoneIndex1': 36, 'm_BoneIndex2': 40, 'm_BoneIndex3': 44}    
    def __init__(self, m_Weight0: System.Single, m_Weight1: System.Single, m_Weight2: System.Single, m_Weight3: System.Single, m_BoneIndex0: System.Int32, m_BoneIndex1: System.Int32, m_BoneIndex2: System.Int32, m_BoneIndex3: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Weight0 = m_Weight0
		self.m_Weight1 = m_Weight1
		self.m_Weight2 = m_Weight2
		self.m_Weight3 = m_Weight3
		self.m_BoneIndex0 = m_BoneIndex0
		self.m_BoneIndex1 = m_BoneIndex1
		self.m_BoneIndex2 = m_BoneIndex2
		self.m_BoneIndex3 = m_BoneIndex3


class BoneWeight1:

    offsets = {'m_Weight': 16, 'm_BoneIndex': 20}    
    def __init__(self, m_Weight: System.Single, m_BoneIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Weight = m_Weight
		self.m_BoneIndex = m_BoneIndex


class BootConfigData:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class Bounds:

    offsets = {'m_Center': 16, 'm_Extents': 28}    
    def __init__(self, m_Center: UnityEngine.Vector3, m_Extents: UnityEngine.Vector3, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Center = m_Center
		self.m_Extents = m_Extents


class Cache:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class CachedAssetBundle:

    offsets = {'m_Name': 16, 'm_Hash': 24}    
    def __init__(self, m_Name: System.String, m_Hash: UnityEngine.Hash128, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Name = m_Name
		self.m_Hash = m_Hash


class Caching:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Camera:
	onPreCull: UnityEngine.Camera.CameraCallback
    offsets = {'onPreCull': 0, 'onPreRender': 8, 'onPostRender': 16}    
    def __init__(self, onPreCull: UnityEngine.Camera.CameraCallback, onPreRender: UnityEngine.Camera.CameraCallback, onPostRender: UnityEngine.Camera.CameraCallback, **kwargs):
        super().__init__(self, **kwargs)
		self.onPreCull = onPreCull
		self.onPreRender = onPreRender
		self.onPostRender = onPostRender


class CameraClearFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CameraType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CastHelper<T>:

    offsets = {'t': 0, 'onePointerFurtherThanT': 0}    
    def __init__(self, t: T, onePointerFurtherThanT: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.t = t
		self.onePointerFurtherThanT = onePointerFurtherThanT


class ClassLibraryInitializer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Color:

    offsets = {'r': 16, 'g': 20, 'b': 24, 'a': 28}    
    def __init__(self, r: System.Single, g: System.Single, b: System.Single, a: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.r = r
		self.g = g
		self.b = b
		self.a = a


class Color32:

    offsets = {'rgba': 16, 'r': 16, 'g': 17, 'b': 18, 'a': 19}    
    def __init__(self, rgba: System.Int32, r: System.Byte, g: System.Byte, b: System.Byte, a: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.rgba = rgba
		self.r = r
		self.g = g
		self.b = b
		self.a = a


class ColorSpace:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ColorUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CombineInstance:

    offsets = {'m_MeshInstanceID': 16, 'm_SubMeshIndex': 20, 'm_Transform': 24, 'm_LightmapScaleOffset': 88, 'm_RealtimeLightmapScaleOffset': 104}    
    def __init__(self, m_MeshInstanceID: System.Int32, m_SubMeshIndex: System.Int32, m_Transform: UnityEngine.Matrix4x4, m_LightmapScaleOffset: UnityEngine.Vector4, m_RealtimeLightmapScaleOffset: UnityEngine.Vector4, **kwargs):
        super().__init__(self, **kwargs)
		self.m_MeshInstanceID = m_MeshInstanceID
		self.m_SubMeshIndex = m_SubMeshIndex
		self.m_Transform = m_Transform
		self.m_LightmapScaleOffset = m_LightmapScaleOffset
		self.m_RealtimeLightmapScaleOffset = m_RealtimeLightmapScaleOffset


class Component:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ComputeBuffer:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class ComputeShader:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ContextMenu:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Coroutine:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class CreateAssetMenuAttribute:

    offsets = {'<menuName>k__BackingField': 16}    
    def __init__(self, <menuName>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<menuName>k__BackingField = <menuName>k__BackingField


class Cubemap:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CubemapArray:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CubemapFace:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CullingGroup:

    offsets = {'m_Ptr': 16, 'm_OnStateChanged': 24}    
    def __init__(self, m_Ptr: System.IntPtr, m_OnStateChanged: UnityEngine.CullingGroup.StateChanged, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_OnStateChanged = m_OnStateChanged


class CullingGroupEvent:

    offsets = {'m_Index': 16, 'm_PrevState': 20, 'm_ThisState': 21}    
    def __init__(self, m_Index: System.Int32, m_PrevState: System.Byte, m_ThisState: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Index = m_Index
		self.m_PrevState = m_PrevState
		self.m_ThisState = m_ThisState


class Cursor:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CursorLockMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CursorMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CustomYieldInstruction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Debug:
	s_Logger: UnityEngine.ILogger
    offsets = {'s_Logger': 0}    
    def __init__(self, s_Logger: UnityEngine.ILogger, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Logger = s_Logger


class DebugLogHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DefaultExecutionOrder:

    offsets = {'m_Order': 16}    
    def __init__(self, m_Order: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Order = m_Order


class DepthTextureMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DeviceType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DisableBatchingType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DisallowMultipleComponent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Display:

    offsets = {'_mainDisplay': 8, 'onDisplaysUpdated': 16, 'nativeDisplay': 16}    
    def __init__(self, _mainDisplay: UnityEngine.Display, onDisplaysUpdated: UnityEngine.Display.DisplaysUpdatedDelegate, nativeDisplay: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self._mainDisplay = _mainDisplay
		self.onDisplaysUpdated = onDisplaysUpdated
		self.nativeDisplay = nativeDisplay


class DrivenRectTransformTracker:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DrivenTransformProperties:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ExcludeFromObjectFactoryAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ExcludeFromPresetAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ExecuteAlways:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ExecuteInEditMode:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ExtensionOfNativeClassAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FailedToLoadScriptObject:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FogMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class FullScreenMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GameObject:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Gradient:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class Graphics:
	kMaxDrawMeshInstanceCount: System.Int32
    offsets = {'kMaxDrawMeshInstanceCount': 0}    
    def __init__(self, kMaxDrawMeshInstanceCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.kMaxDrawMeshInstanceCount = kMaxDrawMeshInstanceCount


class Hash128:

    offsets = {'m_u32_0': 16, 'm_u32_1': 20, 'm_u32_2': 24, 'm_u32_3': 28}    
    def __init__(self, m_u32_0: System.UInt32, m_u32_1: System.UInt32, m_u32_2: System.UInt32, m_u32_3: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_u32_0 = m_u32_0
		self.m_u32_1 = m_u32_1
		self.m_u32_2 = m_u32_2
		self.m_u32_3 = m_u32_3


class HeaderAttribute:

    offsets = {'header': 16}    
    def __init__(self, header: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.header = header


class HelpURLAttribute:

    offsets = {'m_Url': 16}    
    def __init__(self, m_Url: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Url = m_Url


class HideFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class HideInInspector:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ILogHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ILogger:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPlayerEditorConnectionNative:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ISerializationCallbackReceiver:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Internal_DrawTextureArguments:

    offsets = {'screenRect': 16, 'sourceRect': 32, 'leftBorder': 48, 'rightBorder': 52, 'topBorder': 56, 'bottomBorder': 60, 'leftBorderColor': 64, 'rightBorderColor': 80, 'topBorderColor': 96, 'bottomBorderColor': 112, 'color': 128, 'borderWidths': 144, 'cornerRadiuses': 160, 'smoothCorners': 176, 'pass': 180, 'texture': 184, 'mat': 192}    
    def __init__(self, screenRect: UnityEngine.Rect, sourceRect: UnityEngine.Rect, leftBorder: System.Int32, rightBorder: System.Int32, topBorder: System.Int32, bottomBorder: System.Int32, leftBorderColor: UnityEngine.Color, rightBorderColor: UnityEngine.Color, topBorderColor: UnityEngine.Color, bottomBorderColor: UnityEngine.Color, color: UnityEngine.Color, borderWidths: UnityEngine.Vector4, cornerRadiuses: UnityEngine.Vector4, smoothCorners: System.Boolean, pass: System.Int32, texture: UnityEngine.Texture, mat: UnityEngine.Material, **kwargs):
        super().__init__(self, **kwargs)
		self.screenRect = screenRect
		self.sourceRect = sourceRect
		self.leftBorder = leftBorder
		self.rightBorder = rightBorder
		self.topBorder = topBorder
		self.bottomBorder = bottomBorder
		self.leftBorderColor = leftBorderColor
		self.rightBorderColor = rightBorderColor
		self.topBorderColor = topBorderColor
		self.bottomBorderColor = bottomBorderColor
		self.color = color
		self.borderWidths = borderWidths
		self.cornerRadiuses = cornerRadiuses
		self.smoothCorners = smoothCorners
		self.pass = pass
		self.texture = texture
		self.mat = mat


class KeyCode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Keyframe:

    offsets = {'m_Time': 16, 'm_Value': 20, 'm_InTangent': 24, 'm_OutTangent': 28, 'm_WeightedMode': 32, 'm_InWeight': 36, 'm_OutWeight': 40}    
    def __init__(self, m_Time: System.Single, m_Value: System.Single, m_InTangent: System.Single, m_OutTangent: System.Single, m_WeightedMode: System.Int32, m_InWeight: System.Single, m_OutWeight: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Time = m_Time
		self.m_Value = m_Value
		self.m_InTangent = m_InTangent
		self.m_OutTangent = m_OutTangent
		self.m_WeightedMode = m_WeightedMode
		self.m_InWeight = m_InWeight
		self.m_OutWeight = m_OutWeight


class LayerMask:

    offsets = {'m_Mask': 16}    
    def __init__(self, m_Mask: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Mask = m_Mask


class Light:

    offsets = {'m_BakedIndex': 24}    
    def __init__(self, m_BakedIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_BakedIndex = m_BakedIndex


class LightProbeProxyVolume:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LightProbes:
	tetrahedralizationCompleted: System.Action
    offsets = {'tetrahedralizationCompleted': 0, 'needsRetetrahedralization': 8}    
    def __init__(self, tetrahedralizationCompleted: System.Action, needsRetetrahedralization: System.Action, **kwargs):
        super().__init__(self, **kwargs)
		self.tetrahedralizationCompleted = tetrahedralizationCompleted
		self.needsRetetrahedralization = needsRetetrahedralization


class LightShadows:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LightType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LightmapBakeType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LightmapData:

    offsets = {'m_Light': 16, 'm_Dir': 24, 'm_ShadowMask': 32}    
    def __init__(self, m_Light: UnityEngine.Texture2D, m_Dir: UnityEngine.Texture2D, m_ShadowMask: UnityEngine.Texture2D, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Light = m_Light
		self.m_Dir = m_Dir
		self.m_ShadowMask = m_ShadowMask


class LightmapSettings:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LightmapsMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LightmapsModeLegacy:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LineAlignment:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LineRenderer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LineTextureMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LogOption:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LogType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Logger:

    offsets = {'<logHandler>k__BackingField': 16, '<logEnabled>k__BackingField': 24, '<filterLogType>k__BackingField': 28}    
    def __init__(self, <logHandler>k__BackingField: UnityEngine.ILogHandler, <logEnabled>k__BackingField: System.Boolean, <filterLogType>k__BackingField: UnityEngine.LogType, **kwargs):
        super().__init__(self, **kwargs)
		self.<logHandler>k__BackingField = <logHandler>k__BackingField
		self.<logEnabled>k__BackingField = <logEnabled>k__BackingField
		self.<filterLogType>k__BackingField = <filterLogType>k__BackingField


class LowerResBlitTexture:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ManagedStreamHelpers:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Material:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MaterialGlobalIlluminationFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class MaterialPropertyBlock:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class Mathf:
	Epsilon: System.Single
    offsets = {'Epsilon': 0}    
    def __init__(self, Epsilon: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.Epsilon = Epsilon


class Matrix4x4:
	zeroMatrix: UnityEngine.Matrix4x4
    offsets = {'zeroMatrix': 0, 'identityMatrix': 64, 'm00': 16, 'm10': 20, 'm20': 24, 'm30': 28, 'm01': 32, 'm11': 36, 'm21': 40, 'm31': 44, 'm02': 48, 'm12': 52, 'm22': 56, 'm32': 60, 'm03': 64, 'm13': 68, 'm23': 72, 'm33': 76}    
    def __init__(self, zeroMatrix: UnityEngine.Matrix4x4, identityMatrix: UnityEngine.Matrix4x4, m00: System.Single, m10: System.Single, m20: System.Single, m30: System.Single, m01: System.Single, m11: System.Single, m21: System.Single, m31: System.Single, m02: System.Single, m12: System.Single, m22: System.Single, m32: System.Single, m03: System.Single, m13: System.Single, m23: System.Single, m33: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.zeroMatrix = zeroMatrix
		self.identityMatrix = identityMatrix
		self.m00 = m00
		self.m10 = m10
		self.m20 = m20
		self.m30 = m30
		self.m01 = m01
		self.m11 = m11
		self.m21 = m21
		self.m31 = m31
		self.m02 = m02
		self.m12 = m12
		self.m22 = m22
		self.m32 = m32
		self.m03 = m03
		self.m13 = m13
		self.m23 = m23
		self.m33 = m33


class Mesh:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MeshFilter:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MeshRenderer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MeshTopology:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class MixedLightingMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class MonoBehaviour:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MotionVectorGenerationMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class NetworkReachability:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class NoAllocHelpers:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Object:
	OffsetOfInstanceIDInCPlusPlusObject: System.Int32
    offsets = {'OffsetOfInstanceIDInCPlusPlusObject': 0, 'm_CachedPtr': 16}    
    def __init__(self, OffsetOfInstanceIDInCPlusPlusObject: System.Int32, m_CachedPtr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.OffsetOfInstanceIDInCPlusPlusObject = OffsetOfInstanceIDInCPlusPlusObject
		self.m_CachedPtr = m_CachedPtr


class OperatingSystemFamily:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Ping:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class Plane:

    offsets = {'m_Normal': 16, 'm_Distance': 28}    
    def __init__(self, m_Normal: UnityEngine.Vector3, m_Distance: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Normal = m_Normal
		self.m_Distance = m_Distance


class PlayerConnectionInternal:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerPrefs:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerPrefsException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PreferBinarySerialization:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PreloadData:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PrimitiveType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PropertyAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PropertyName:

    offsets = {'id': 16}    
    def __init__(self, id: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.id = id


class PropertyNameUtils:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class QualitySettings:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Quaternion:
	identityQuaternion: UnityEngine.Quaternion
    offsets = {'identityQuaternion': 0, 'x': 16, 'y': 20, 'z': 24, 'w': 28}    
    def __init__(self, identityQuaternion: UnityEngine.Quaternion, x: System.Single, y: System.Single, z: System.Single, w: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.identityQuaternion = identityQuaternion
		self.x = x
		self.y = y
		self.z = z
		self.w = w


class Random:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RangeAttribute:

    offsets = {'min': 16, 'max': 20}    
    def __init__(self, min: System.Single, max: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.min = min
		self.max = max


class RangeInt:

    offsets = {'start': 16, 'length': 20}    
    def __init__(self, start: System.Int32, length: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.start = start
		self.length = length


class Ray:

    offsets = {'m_Origin': 16, 'm_Direction': 28}    
    def __init__(self, m_Origin: UnityEngine.Vector3, m_Direction: UnityEngine.Vector3, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Origin = m_Origin
		self.m_Direction = m_Direction


class Rect:

    offsets = {'m_XMin': 16, 'm_YMin': 20, 'm_Width': 24, 'm_Height': 28}    
    def __init__(self, m_XMin: System.Single, m_YMin: System.Single, m_Width: System.Single, m_Height: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_XMin = m_XMin
		self.m_YMin = m_YMin
		self.m_Width = m_Width
		self.m_Height = m_Height


class RectInt:

    offsets = {'m_XMin': 16, 'm_YMin': 20, 'm_Width': 24, 'm_Height': 28}    
    def __init__(self, m_XMin: System.Int32, m_YMin: System.Int32, m_Width: System.Int32, m_Height: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_XMin = m_XMin
		self.m_YMin = m_YMin
		self.m_Width = m_Width
		self.m_Height = m_Height


class RectOffset:

    offsets = {'m_Ptr': 16, 'm_SourceStyle': 24}    
    def __init__(self, m_Ptr: System.IntPtr, m_SourceStyle: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_SourceStyle = m_SourceStyle


class RectTransform:
	reapplyDrivenProperties: UnityEngine.RectTransform.ReapplyDrivenProperties
    offsets = {'reapplyDrivenProperties': 0}    
    def __init__(self, reapplyDrivenProperties: UnityEngine.RectTransform.ReapplyDrivenProperties, **kwargs):
        super().__init__(self, **kwargs)
		self.reapplyDrivenProperties = reapplyDrivenProperties


class ReflectionProbe:
	reflectionProbeChanged: System.Action<UnityEngine.ReflectionProbe,UnityEngine.ReflectionProbe.ReflectionProbeEvent>
    offsets = {'reflectionProbeChanged': 0, 'defaultReflectionSet': 8}    
    def __init__(self, reflectionProbeChanged: System.Action<UnityEngine.ReflectionProbe,UnityEngine.ReflectionProbe.ReflectionProbeEvent>, defaultReflectionSet: System.Action<UnityEngine.Cubemap>, **kwargs):
        super().__init__(self, **kwargs)
		self.reflectionProbeChanged = reflectionProbeChanged
		self.defaultReflectionSet = defaultReflectionSet


class RenderBuffer:

    offsets = {'m_RenderTextureInstanceID': 16, 'm_BufferPtr': 24}    
    def __init__(self, m_RenderTextureInstanceID: System.Int32, m_BufferPtr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_RenderTextureInstanceID = m_RenderTextureInstanceID
		self.m_BufferPtr = m_BufferPtr


class RenderSettings:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RenderTexture:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RenderTextureCreationFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RenderTextureDescriptor:

    offsets = {'<width>k__BackingField': 16, '<height>k__BackingField': 20, '<msaaSamples>k__BackingField': 24, '<volumeDepth>k__BackingField': 28, '<mipCount>k__BackingField': 32, '_graphicsFormat': 36, '<stencilFormat>k__BackingField': 40, '_depthBufferBits': 44, '<dimension>k__BackingField': 48, '<shadowSamplingMode>k__BackingField': 52, '<vrUsage>k__BackingField': 56, '_flags': 60, '<memoryless>k__BackingField': 64}    
    def __init__(self, <width>k__BackingField: System.Int32, <height>k__BackingField: System.Int32, <msaaSamples>k__BackingField: System.Int32, <volumeDepth>k__BackingField: System.Int32, <mipCount>k__BackingField: System.Int32, _graphicsFormat: UnityEngine.Experimental.Rendering.GraphicsFormat, <stencilFormat>k__BackingField: UnityEngine.Experimental.Rendering.GraphicsFormat, _depthBufferBits: System.Int32, <dimension>k__BackingField: UnityEngine.Rendering.TextureDimension, <shadowSamplingMode>k__BackingField: UnityEngine.Rendering.ShadowSamplingMode, <vrUsage>k__BackingField: UnityEngine.VRTextureUsage, _flags: UnityEngine.RenderTextureCreationFlags, <memoryless>k__BackingField: UnityEngine.RenderTextureMemoryless, **kwargs):
        super().__init__(self, **kwargs)
		self.<width>k__BackingField = <width>k__BackingField
		self.<height>k__BackingField = <height>k__BackingField
		self.<msaaSamples>k__BackingField = <msaaSamples>k__BackingField
		self.<volumeDepth>k__BackingField = <volumeDepth>k__BackingField
		self.<mipCount>k__BackingField = <mipCount>k__BackingField
		self._graphicsFormat = _graphicsFormat
		self.<stencilFormat>k__BackingField = <stencilFormat>k__BackingField
		self._depthBufferBits = _depthBufferBits
		self.<dimension>k__BackingField = <dimension>k__BackingField
		self.<shadowSamplingMode>k__BackingField = <shadowSamplingMode>k__BackingField
		self.<vrUsage>k__BackingField = <vrUsage>k__BackingField
		self._flags = _flags
		self.<memoryless>k__BackingField = <memoryless>k__BackingField


class RenderTextureFormat:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RenderTextureMemoryless:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RenderTextureReadWrite:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Renderer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RenderingPath:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RequireComponent:

    offsets = {'m_Type0': 16, 'm_Type1': 24, 'm_Type2': 32}    
    def __init__(self, m_Type0: System.Type, m_Type1: System.Type, m_Type2: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Type0 = m_Type0
		self.m_Type1 = m_Type1
		self.m_Type2 = m_Type2


class Resolution:

    offsets = {'m_Width': 16, 'm_Height': 20, 'm_RefreshRate': 24}    
    def __init__(self, m_Width: System.Int32, m_Height: System.Int32, m_RefreshRate: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Width = m_Width
		self.m_Height = m_Height
		self.m_RefreshRate = m_RefreshRate


class ResourceRequest:

    offsets = {'m_Path': 32, 'm_Type': 40}    
    def __init__(self, m_Path: System.String, m_Type: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Path = m_Path
		self.m_Type = m_Type


class Resources:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RotationOrder:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RuntimeInitializeLoadType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RuntimeInitializeOnLoadMethodAttribute:

    offsets = {'m_LoadType': 16}    
    def __init__(self, m_LoadType: UnityEngine.RuntimeInitializeLoadType, **kwargs):
        super().__init__(self, **kwargs)
		self.m_LoadType = m_LoadType


class RuntimePlatform:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Screen:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScreenOrientation:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ScriptableObject:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptingUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SelectionBaseAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SendMessageOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SerializeField:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SerializePrivateVariables:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SerializeReference:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SetupCoroutine:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Shader:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SkinQuality:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SkinnedMeshRenderer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SortingLayer:

    offsets = {'m_Id': 16}    
    def __init__(self, m_Id: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Id = m_Id


class Space:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpaceAttribute:

    offsets = {'height': 16}    
    def __init__(self, height: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.height = height


class Sprite:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SpriteDrawMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpriteMaskInteraction:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpriteMeshType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpritePackingMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpritePackingRotation:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpriteRenderer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SpriteSortPoint:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpriteTileMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class StackTraceUtility:
	projectFolder: System.String
    offsets = {'projectFolder': 0}    
    def __init__(self, projectFolder: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.projectFolder = projectFolder


class StereoTargetEyeMask:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SystemClock:
	s_Epoch: System.DateTime
    offsets = {'s_Epoch': 0}    
    def __init__(self, s_Epoch: System.DateTime, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Epoch = s_Epoch


class SystemInfo:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SystemLanguage:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TextAreaAttribute:

    offsets = {'minLines': 16, 'maxLines': 20}    
    def __init__(self, minLines: System.Int32, maxLines: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.minLines = minLines
		self.maxLines = maxLines


class TextAsset:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Texture:
	GenerateAllMips: System.Int32
    offsets = {'GenerateAllMips': 0}    
    def __init__(self, GenerateAllMips: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.GenerateAllMips = GenerateAllMips


class Texture2D:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Texture2DArray:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Texture3D:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TextureFormat:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TextureWrapMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Time:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TooltipAttribute:

    offsets = {'tooltip': 16}    
    def __init__(self, tooltip: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.tooltip = tooltip


class TouchScreenKeyboard:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class TouchScreenKeyboardType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TouchScreenKeyboard_InternalConstructorHelperArguments:

    offsets = {'keyboardType': 16, 'autocorrection': 20, 'multiline': 24, 'secure': 28, 'alert': 32, 'characterLimit': 36}    
    def __init__(self, keyboardType: System.UInt32, autocorrection: System.UInt32, multiline: System.UInt32, secure: System.UInt32, alert: System.UInt32, characterLimit: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.keyboardType = keyboardType
		self.autocorrection = autocorrection
		self.multiline = multiline
		self.secure = secure
		self.alert = alert
		self.characterLimit = characterLimit


class TrackedReference:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class TrailRenderer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Transform:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TransparencySortMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class UnhandledExceptionHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityLogWriter:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnitySynchronizationContext:

    offsets = {'m_AsyncWorkQueue': 24, 'm_CurrentFrameWork': 32, 'm_MainThreadID': 40, 'm_TrackedCount': 44}    
    def __init__(self, m_AsyncWorkQueue: System.Collections.Generic.List<UnityEngine.UnitySynchronizationContext.WorkRequest>, m_CurrentFrameWork: System.Collections.Generic.List<UnityEngine.UnitySynchronizationContext.WorkRequest>, m_MainThreadID: System.Int32, m_TrackedCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_AsyncWorkQueue = m_AsyncWorkQueue
		self.m_CurrentFrameWork = m_CurrentFrameWork
		self.m_MainThreadID = m_MainThreadID
		self.m_TrackedCount = m_TrackedCount


class VRTextureUsage:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Vector2:
	zeroVector: UnityEngine.Vector2
    offsets = {'zeroVector': 0, 'oneVector': 8, 'upVector': 16, 'downVector': 24, 'leftVector': 32, 'rightVector': 40, 'positiveInfinityVector': 48, 'negativeInfinityVector': 56, 'x': 16, 'y': 20}    
    def __init__(self, zeroVector: UnityEngine.Vector2, oneVector: UnityEngine.Vector2, upVector: UnityEngine.Vector2, downVector: UnityEngine.Vector2, leftVector: UnityEngine.Vector2, rightVector: UnityEngine.Vector2, positiveInfinityVector: UnityEngine.Vector2, negativeInfinityVector: UnityEngine.Vector2, x: System.Single, y: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.zeroVector = zeroVector
		self.oneVector = oneVector
		self.upVector = upVector
		self.downVector = downVector
		self.leftVector = leftVector
		self.rightVector = rightVector
		self.positiveInfinityVector = positiveInfinityVector
		self.negativeInfinityVector = negativeInfinityVector
		self.x = x
		self.y = y


class Vector2Int:
	s_Zero: UnityEngine.Vector2Int
    offsets = {'s_Zero': 0, 's_One': 8, 's_Up': 16, 's_Down': 24, 's_Left': 32, 's_Right': 40, 'm_X': 16, 'm_Y': 20}    
    def __init__(self, s_Zero: UnityEngine.Vector2Int, s_One: UnityEngine.Vector2Int, s_Up: UnityEngine.Vector2Int, s_Down: UnityEngine.Vector2Int, s_Left: UnityEngine.Vector2Int, s_Right: UnityEngine.Vector2Int, m_X: System.Int32, m_Y: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Zero = s_Zero
		self.s_One = s_One
		self.s_Up = s_Up
		self.s_Down = s_Down
		self.s_Left = s_Left
		self.s_Right = s_Right
		self.m_X = m_X
		self.m_Y = m_Y


class Vector3:
	zeroVector: UnityEngine.Vector3
    offsets = {'zeroVector': 0, 'oneVector': 12, 'upVector': 24, 'downVector': 36, 'leftVector': 48, 'rightVector': 60, 'forwardVector': 72, 'backVector': 84, 'positiveInfinityVector': 96, 'negativeInfinityVector': 108, 'x': 16, 'y': 20, 'z': 24}    
    def __init__(self, zeroVector: UnityEngine.Vector3, oneVector: UnityEngine.Vector3, upVector: UnityEngine.Vector3, downVector: UnityEngine.Vector3, leftVector: UnityEngine.Vector3, rightVector: UnityEngine.Vector3, forwardVector: UnityEngine.Vector3, backVector: UnityEngine.Vector3, positiveInfinityVector: UnityEngine.Vector3, negativeInfinityVector: UnityEngine.Vector3, x: System.Single, y: System.Single, z: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.zeroVector = zeroVector
		self.oneVector = oneVector
		self.upVector = upVector
		self.downVector = downVector
		self.leftVector = leftVector
		self.rightVector = rightVector
		self.forwardVector = forwardVector
		self.backVector = backVector
		self.positiveInfinityVector = positiveInfinityVector
		self.negativeInfinityVector = negativeInfinityVector
		self.x = x
		self.y = y
		self.z = z


class Vector3Int:
	s_Zero: UnityEngine.Vector3Int
    offsets = {'s_Zero': 0, 's_One': 12, 's_Up': 24, 's_Down': 36, 's_Left': 48, 's_Right': 60, 'm_X': 16, 'm_Y': 20, 'm_Z': 24}    
    def __init__(self, s_Zero: UnityEngine.Vector3Int, s_One: UnityEngine.Vector3Int, s_Up: UnityEngine.Vector3Int, s_Down: UnityEngine.Vector3Int, s_Left: UnityEngine.Vector3Int, s_Right: UnityEngine.Vector3Int, m_X: System.Int32, m_Y: System.Int32, m_Z: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Zero = s_Zero
		self.s_One = s_One
		self.s_Up = s_Up
		self.s_Down = s_Down
		self.s_Left = s_Left
		self.s_Right = s_Right
		self.m_X = m_X
		self.m_Y = m_Y
		self.m_Z = m_Z


class Vector4:
	zeroVector: UnityEngine.Vector4
    offsets = {'zeroVector': 0, 'oneVector': 16, 'positiveInfinityVector': 32, 'negativeInfinityVector': 48, 'x': 16, 'y': 20, 'z': 24, 'w': 28}    
    def __init__(self, zeroVector: UnityEngine.Vector4, oneVector: UnityEngine.Vector4, positiveInfinityVector: UnityEngine.Vector4, negativeInfinityVector: UnityEngine.Vector4, x: System.Single, y: System.Single, z: System.Single, w: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.zeroVector = zeroVector
		self.oneVector = oneVector
		self.positiveInfinityVector = positiveInfinityVector
		self.negativeInfinityVector = negativeInfinityVector
		self.x = x
		self.y = y
		self.z = z
		self.w = w


class WaitForEndOfFrame:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WaitForFixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WaitForSeconds:

    offsets = {'m_Seconds': 16}    
    def __init__(self, m_Seconds: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Seconds = m_Seconds


class WaitForSecondsRealtime:

    offsets = {'<waitTime>k__BackingField': 16, 'm_WaitUntilTime': 20}    
    def __init__(self, <waitTime>k__BackingField: System.Single, m_WaitUntilTime: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.<waitTime>k__BackingField = <waitTime>k__BackingField
		self.m_WaitUntilTime = m_WaitUntilTime


class WaitUntil:

    offsets = {'m_Predicate': 16}    
    def __init__(self, m_Predicate: System.Func<System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Predicate = m_Predicate


class WrapMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class YieldInstruction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Assert:
	raiseExceptions: System.Boolean
    offsets = {'raiseExceptions': 0}    
    def __init__(self, raiseExceptions: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.raiseExceptions = raiseExceptions


class AssertionException:

    offsets = {'m_UserMessage': 136}    
    def __init__(self, m_UserMessage: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_UserMessage = m_UserMessage


class AssertionMessageUtil:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ArgumentCache:

    offsets = {'m_ObjectArgument': 16, 'm_ObjectArgumentAssemblyTypeName': 24, 'm_IntArgument': 32, 'm_FloatArgument': 36, 'm_StringArgument': 40, 'm_BoolArgument': 48}    
    def __init__(self, m_ObjectArgument: UnityEngine.Object, m_ObjectArgumentAssemblyTypeName: System.String, m_IntArgument: System.Int32, m_FloatArgument: System.Single, m_StringArgument: System.String, m_BoolArgument: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ObjectArgument = m_ObjectArgument
		self.m_ObjectArgumentAssemblyTypeName = m_ObjectArgumentAssemblyTypeName
		self.m_IntArgument = m_IntArgument
		self.m_FloatArgument = m_FloatArgument
		self.m_StringArgument = m_StringArgument
		self.m_BoolArgument = m_BoolArgument


class BaseInvokableCall:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CachedInvokableCall<T>:

    offsets = {'m_Arg1': 0}    
    def __init__(self, m_Arg1: T, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Arg1 = m_Arg1


class InvokableCall:

    offsets = {'Delegate': 16}    
    def __init__(self, Delegate: UnityEngine.Events.UnityAction, **kwargs):
        super().__init__(self, **kwargs)
		self.Delegate = Delegate


class InvokableCall<T1,T2,T3,T4>:

    offsets = {'Delegate': 0}    
    def __init__(self, Delegate: UnityEngine.Events.UnityAction<T1,T2,T3,T4>, **kwargs):
        super().__init__(self, **kwargs)
		self.Delegate = Delegate


class InvokableCall<T1,T2,T3>:

    offsets = {'Delegate': 0}    
    def __init__(self, Delegate: UnityEngine.Events.UnityAction<T1,T2,T3>, **kwargs):
        super().__init__(self, **kwargs)
		self.Delegate = Delegate


class InvokableCall<T1,T2>:

    offsets = {'Delegate': 0}    
    def __init__(self, Delegate: UnityEngine.Events.UnityAction<T1,T2>, **kwargs):
        super().__init__(self, **kwargs)
		self.Delegate = Delegate


class InvokableCall<T1>:

    offsets = {'Delegate': 0}    
    def __init__(self, Delegate: UnityEngine.Events.UnityAction<T1>, **kwargs):
        super().__init__(self, **kwargs)
		self.Delegate = Delegate


class InvokableCallList:

    offsets = {'m_PersistentCalls': 16, 'm_RuntimeCalls': 24, 'm_ExecutingCalls': 32, 'm_NeedsUpdate': 40}    
    def __init__(self, m_PersistentCalls: System.Collections.Generic.List<UnityEngine.Events.BaseInvokableCall>, m_RuntimeCalls: System.Collections.Generic.List<UnityEngine.Events.BaseInvokableCall>, m_ExecutingCalls: System.Collections.Generic.List<UnityEngine.Events.BaseInvokableCall>, m_NeedsUpdate: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_PersistentCalls = m_PersistentCalls
		self.m_RuntimeCalls = m_RuntimeCalls
		self.m_ExecutingCalls = m_ExecutingCalls
		self.m_NeedsUpdate = m_NeedsUpdate


class PersistentCall:

    offsets = {'m_Target': 16, 'm_MethodName': 24, 'm_Mode': 32, 'm_Arguments': 40, 'm_CallState': 48}    
    def __init__(self, m_Target: UnityEngine.Object, m_MethodName: System.String, m_Mode: UnityEngine.Events.PersistentListenerMode, m_Arguments: UnityEngine.Events.ArgumentCache, m_CallState: UnityEngine.Events.UnityEventCallState, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Target = m_Target
		self.m_MethodName = m_MethodName
		self.m_Mode = m_Mode
		self.m_Arguments = m_Arguments
		self.m_CallState = m_CallState


class PersistentCallGroup:

    offsets = {'m_Calls': 16}    
    def __init__(self, m_Calls: System.Collections.Generic.List<UnityEngine.Events.PersistentCall>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Calls = m_Calls


class PersistentListenerMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class UnityAction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityAction<T0,T1,T2,T3>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityAction<T0,T1,T2>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityAction<T0,T1>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityAction<T0>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityEvent<T0,T1,T2,T3>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityEvent<T0,T1,T2>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityEvent<T0,T1>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityEvent<T0>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityEventBase:

    offsets = {'m_Calls': 16, 'm_PersistentCalls': 24, 'm_CallsDirty': 32}    
    def __init__(self, m_Calls: UnityEngine.Events.InvokableCallList, m_PersistentCalls: UnityEngine.Events.PersistentCallGroup, m_CallsDirty: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Calls = m_Calls
		self.m_PersistentCalls = m_PersistentCalls
		self.m_CallsDirty = m_CallsDirty


class UnityEventCallState:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AngularFalloffType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DirectionalLight:

    offsets = {'instanceID': 16, 'shadow': 20, 'mode': 21, 'direction': 24, 'color': 36, 'indirectColor': 52, 'penumbraWidthRadian': 68}    
    def __init__(self, instanceID: System.Int32, shadow: System.Boolean, mode: UnityEngine.Experimental.GlobalIllumination.LightMode, direction: UnityEngine.Vector3, color: UnityEngine.Experimental.GlobalIllumination.LinearColor, indirectColor: UnityEngine.Experimental.GlobalIllumination.LinearColor, penumbraWidthRadian: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.instanceID = instanceID
		self.shadow = shadow
		self.mode = mode
		self.direction = direction
		self.color = color
		self.indirectColor = indirectColor
		self.penumbraWidthRadian = penumbraWidthRadian


class DiscLight:

    offsets = {'instanceID': 16, 'shadow': 20, 'mode': 21, 'position': 24, 'orientation': 36, 'color': 52, 'indirectColor': 68, 'range': 84, 'radius': 88, 'falloff': 92}    
    def __init__(self, instanceID: System.Int32, shadow: System.Boolean, mode: UnityEngine.Experimental.GlobalIllumination.LightMode, position: UnityEngine.Vector3, orientation: UnityEngine.Quaternion, color: UnityEngine.Experimental.GlobalIllumination.LinearColor, indirectColor: UnityEngine.Experimental.GlobalIllumination.LinearColor, range: System.Single, radius: System.Single, falloff: UnityEngine.Experimental.GlobalIllumination.FalloffType, **kwargs):
        super().__init__(self, **kwargs)
		self.instanceID = instanceID
		self.shadow = shadow
		self.mode = mode
		self.position = position
		self.orientation = orientation
		self.color = color
		self.indirectColor = indirectColor
		self.range = range
		self.radius = radius
		self.falloff = falloff


class FalloffType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LightDataGI:

    offsets = {'instanceID': 16, 'color': 20, 'indirectColor': 36, 'orientation': 52, 'position': 68, 'range': 80, 'coneAngle': 84, 'innerConeAngle': 88, 'shape0': 92, 'shape1': 96, 'type': 100, 'mode': 101, 'shadow': 102, 'falloff': 103}    
    def __init__(self, instanceID: System.Int32, color: UnityEngine.Experimental.GlobalIllumination.LinearColor, indirectColor: UnityEngine.Experimental.GlobalIllumination.LinearColor, orientation: UnityEngine.Quaternion, position: UnityEngine.Vector3, range: System.Single, coneAngle: System.Single, innerConeAngle: System.Single, shape0: System.Single, shape1: System.Single, type: UnityEngine.Experimental.GlobalIllumination.LightType, mode: UnityEngine.Experimental.GlobalIllumination.LightMode, shadow: System.Byte, falloff: UnityEngine.Experimental.GlobalIllumination.FalloffType, **kwargs):
        super().__init__(self, **kwargs)
		self.instanceID = instanceID
		self.color = color
		self.indirectColor = indirectColor
		self.orientation = orientation
		self.position = position
		self.range = range
		self.coneAngle = coneAngle
		self.innerConeAngle = innerConeAngle
		self.shape0 = shape0
		self.shape1 = shape1
		self.type = type
		self.mode = mode
		self.shadow = shadow
		self.falloff = falloff


class LightMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LightType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LightmapperUtils:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Lightmapping:
	s_DefaultDelegate: UnityEngine.Experimental.GlobalIllumination.Lightmapping.RequestLightsDelegate
    offsets = {'s_DefaultDelegate': 0, 's_RequestLightsDelegate': 8}    
    def __init__(self, s_DefaultDelegate: UnityEngine.Experimental.GlobalIllumination.Lightmapping.RequestLightsDelegate, s_RequestLightsDelegate: UnityEngine.Experimental.GlobalIllumination.Lightmapping.RequestLightsDelegate, **kwargs):
        super().__init__(self, **kwargs)
		self.s_DefaultDelegate = s_DefaultDelegate
		self.s_RequestLightsDelegate = s_RequestLightsDelegate


class LinearColor:

    offsets = {'m_red': 16, 'm_green': 20, 'm_blue': 24, 'm_intensity': 28}    
    def __init__(self, m_red: System.Single, m_green: System.Single, m_blue: System.Single, m_intensity: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_red = m_red
		self.m_green = m_green
		self.m_blue = m_blue
		self.m_intensity = m_intensity


class PointLight:

    offsets = {'instanceID': 16, 'shadow': 20, 'mode': 21, 'position': 24, 'color': 36, 'indirectColor': 52, 'range': 68, 'sphereRadius': 72, 'falloff': 76}    
    def __init__(self, instanceID: System.Int32, shadow: System.Boolean, mode: UnityEngine.Experimental.GlobalIllumination.LightMode, position: UnityEngine.Vector3, color: UnityEngine.Experimental.GlobalIllumination.LinearColor, indirectColor: UnityEngine.Experimental.GlobalIllumination.LinearColor, range: System.Single, sphereRadius: System.Single, falloff: UnityEngine.Experimental.GlobalIllumination.FalloffType, **kwargs):
        super().__init__(self, **kwargs)
		self.instanceID = instanceID
		self.shadow = shadow
		self.mode = mode
		self.position = position
		self.color = color
		self.indirectColor = indirectColor
		self.range = range
		self.sphereRadius = sphereRadius
		self.falloff = falloff


class RectangleLight:

    offsets = {'instanceID': 16, 'shadow': 20, 'mode': 21, 'position': 24, 'orientation': 36, 'color': 52, 'indirectColor': 68, 'range': 84, 'width': 88, 'height': 92, 'falloff': 96}    
    def __init__(self, instanceID: System.Int32, shadow: System.Boolean, mode: UnityEngine.Experimental.GlobalIllumination.LightMode, position: UnityEngine.Vector3, orientation: UnityEngine.Quaternion, color: UnityEngine.Experimental.GlobalIllumination.LinearColor, indirectColor: UnityEngine.Experimental.GlobalIllumination.LinearColor, range: System.Single, width: System.Single, height: System.Single, falloff: UnityEngine.Experimental.GlobalIllumination.FalloffType, **kwargs):
        super().__init__(self, **kwargs)
		self.instanceID = instanceID
		self.shadow = shadow
		self.mode = mode
		self.position = position
		self.orientation = orientation
		self.color = color
		self.indirectColor = indirectColor
		self.range = range
		self.width = width
		self.height = height
		self.falloff = falloff


class SpotLight:

    offsets = {'instanceID': 16, 'shadow': 20, 'mode': 21, 'position': 24, 'orientation': 36, 'color': 52, 'indirectColor': 68, 'range': 84, 'sphereRadius': 88, 'coneAngle': 92, 'innerConeAngle': 96, 'falloff': 100, 'angularFalloff': 101}    
    def __init__(self, instanceID: System.Int32, shadow: System.Boolean, mode: UnityEngine.Experimental.GlobalIllumination.LightMode, position: UnityEngine.Vector3, orientation: UnityEngine.Quaternion, color: UnityEngine.Experimental.GlobalIllumination.LinearColor, indirectColor: UnityEngine.Experimental.GlobalIllumination.LinearColor, range: System.Single, sphereRadius: System.Single, coneAngle: System.Single, innerConeAngle: System.Single, falloff: UnityEngine.Experimental.GlobalIllumination.FalloffType, angularFalloff: UnityEngine.Experimental.GlobalIllumination.AngularFalloffType, **kwargs):
        super().__init__(self, **kwargs)
		self.instanceID = instanceID
		self.shadow = shadow
		self.mode = mode
		self.position = position
		self.orientation = orientation
		self.color = color
		self.indirectColor = indirectColor
		self.range = range
		self.sphereRadius = sphereRadius
		self.coneAngle = coneAngle
		self.innerConeAngle = innerConeAngle
		self.falloff = falloff
		self.angularFalloff = angularFalloff


class CameraPlayable:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class MaterialEffectPlayable:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class TextureMixerPlayable:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class TexturePlayableOutput:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableOutputHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class BuiltinRuntimeReflectionSystem:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DefaultFormat:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class FormatUsage:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GraphicsFormat:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GraphicsFormatUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IScriptableRuntimeReflectionSystem:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ScriptableRuntimeReflectionSystemSettings:
	s_Instance: UnityEngine.Experimental.Rendering.ScriptableRuntimeReflectionSystemWrapper
    offsets = {'s_Instance': 0}    
    def __init__(self, s_Instance: UnityEngine.Experimental.Rendering.ScriptableRuntimeReflectionSystemWrapper, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Instance = s_Instance


class ScriptableRuntimeReflectionSystemWrapper:

    offsets = {'<implementation>k__BackingField': 16}    
    def __init__(self, <implementation>k__BackingField: UnityEngine.Experimental.Rendering.IScriptableRuntimeReflectionSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.<implementation>k__BackingField = <implementation>k__BackingField


class TextureCreationFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpriteIntermediateRendererInfo:

    offsets = {'SpriteID': 16, 'TextureID': 20, 'MaterialID': 24, 'Color': 28, 'Transform': 44, 'Bounds': 108, 'Layer': 132, 'SortingLayer': 136, 'SortingOrder': 140, 'SceneCullingMask': 144, 'IndexData': 152, 'VertexData': 160, 'IndexCount': 168, 'VertexCount': 172, 'ShaderChannelMask': 176}    
    def __init__(self, SpriteID: System.Int32, TextureID: System.Int32, MaterialID: System.Int32, Color: UnityEngine.Color, Transform: UnityEngine.Matrix4x4, Bounds: UnityEngine.Bounds, Layer: System.Int32, SortingLayer: System.Int32, SortingOrder: System.Int32, SceneCullingMask: System.UInt64, IndexData: System.IntPtr, VertexData: System.IntPtr, IndexCount: System.Int32, VertexCount: System.Int32, ShaderChannelMask: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.SpriteID = SpriteID
		self.TextureID = TextureID
		self.MaterialID = MaterialID
		self.Color = Color
		self.Transform = Transform
		self.Bounds = Bounds
		self.Layer = Layer
		self.SortingLayer = SortingLayer
		self.SortingOrder = SortingOrder
		self.SceneCullingMask = SceneCullingMask
		self.IndexData = IndexData
		self.VertexData = VertexData
		self.IndexCount = IndexCount
		self.VertexCount = VertexCount
		self.ShaderChannelMask = ShaderChannelMask


class SpriteRendererGroup:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DefaultValueAttribute:

    offsets = {'DefaultValue': 16}    
    def __init__(self, DefaultValue: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.DefaultValue = DefaultValue


class ExcludeFromDocsAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ISubAssetNotDuplicatable:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayerLoopSystem:

    offsets = {'type': 16, 'updateDelegate': 32, 'updateFunction': 40, 'loopConditionFunction': 48}    
    def __init__(self, type: System.Type, updateDelegate: UnityEngine.LowLevel.PlayerLoopSystem.UpdateFunction, updateFunction: System.IntPtr, loopConditionFunction: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.type = type
		self.updateDelegate = updateDelegate
		self.updateFunction = updateFunction
		self.loopConditionFunction = loopConditionFunction


class PlayerLoopSystemInternal:

    offsets = {'type': 16, 'updateDelegate': 24, 'updateFunction': 32, 'loopConditionFunction': 40, 'numSubSystems': 48}    
    def __init__(self, type: System.Type, updateDelegate: UnityEngine.LowLevel.PlayerLoopSystem.UpdateFunction, updateFunction: System.IntPtr, loopConditionFunction: System.IntPtr, numSubSystems: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.type = type
		self.updateDelegate = updateDelegate
		self.updateFunction = updateFunction
		self.loopConditionFunction = loopConditionFunction
		self.numSubSystems = numSubSystems


class MessageEventArgs:

    offsets = {'playerId': 16}    
    def __init__(self, playerId: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.playerId = playerId


class PlayerConnection:
	connectionNative: UnityEngine.IPlayerEditorConnectionNative
    offsets = {'connectionNative': 0, 's_Instance': 8, 'm_PlayerEditorConnectionEvents': 24, 'm_connectedPlayers': 32, 'm_IsInitilized': 40}    
    def __init__(self, connectionNative: UnityEngine.IPlayerEditorConnectionNative, s_Instance: UnityEngine.Networking.PlayerConnection.PlayerConnection, m_PlayerEditorConnectionEvents: UnityEngine.Networking.PlayerConnection.PlayerEditorConnectionEvents, m_connectedPlayers: System.Collections.Generic.List<System.Int32>, m_IsInitilized: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.connectionNative = connectionNative
		self.s_Instance = s_Instance
		self.m_PlayerEditorConnectionEvents = m_PlayerEditorConnectionEvents
		self.m_connectedPlayers = m_connectedPlayers
		self.m_IsInitilized = m_IsInitilized


class PlayerEditorConnectionEvents:

    offsets = {'messageTypeSubscribers': 16, 'connectionEvent': 24, 'disconnectionEvent': 32}    
    def __init__(self, messageTypeSubscribers: System.Collections.Generic.List<UnityEngine.Networking.PlayerConnection.PlayerEditorConnectionEvents.MessageTypeSubscribers>, connectionEvent: UnityEngine.Networking.PlayerConnection.PlayerEditorConnectionEvents.ConnectionChangeEvent, disconnectionEvent: UnityEngine.Networking.PlayerConnection.PlayerEditorConnectionEvents.ConnectionChangeEvent, **kwargs):
        super().__init__(self, **kwargs)
		self.messageTypeSubscribers = messageTypeSubscribers
		self.connectionEvent = connectionEvent
		self.disconnectionEvent = disconnectionEvent


class DirectorUpdateMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class FrameData:

    offsets = {'m_FrameID': 16, 'm_DeltaTime': 24, 'm_Weight': 32, 'm_EffectiveWeight': 36, 'm_EffectiveParentDelay': 40, 'm_EffectiveParentSpeed': 48, 'm_EffectiveSpeed': 52, 'm_Flags': 56, 'm_Output': 64}    
    def __init__(self, m_FrameID: System.UInt64, m_DeltaTime: System.Double, m_Weight: System.Single, m_EffectiveWeight: System.Single, m_EffectiveParentDelay: System.Double, m_EffectiveParentSpeed: System.Single, m_EffectiveSpeed: System.Single, m_Flags: UnityEngine.Playables.FrameData.Flags, m_Output: UnityEngine.Playables.PlayableOutput, **kwargs):
        super().__init__(self, **kwargs)
		self.m_FrameID = m_FrameID
		self.m_DeltaTime = m_DeltaTime
		self.m_Weight = m_Weight
		self.m_EffectiveWeight = m_EffectiveWeight
		self.m_EffectiveParentDelay = m_EffectiveParentDelay
		self.m_EffectiveParentSpeed = m_EffectiveParentSpeed
		self.m_EffectiveSpeed = m_EffectiveSpeed
		self.m_Flags = m_Flags
		self.m_Output = m_Output


class INotification:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class INotificationReceiver:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPlayable:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPlayableBehaviour:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPlayableOutput:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Playable:
	m_NullPlayable: UnityEngine.Playables.Playable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Playables.Playable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class PlayableAsset:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayableBehaviour:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayableBinding:

    offsets = {'DefaultDuration': 8, 'm_StreamName': 16, 'm_SourceObject': 24, 'm_SourceBindingType': 32, 'm_CreateOutputMethod': 40}    
    def __init__(self, DefaultDuration: System.Double, m_StreamName: System.String, m_SourceObject: UnityEngine.Object, m_SourceBindingType: System.Type, m_CreateOutputMethod: UnityEngine.Playables.PlayableBinding.CreateOutputMethod, **kwargs):
        super().__init__(self, **kwargs)
		self.DefaultDuration = DefaultDuration
		self.m_StreamName = m_StreamName
		self.m_SourceObject = m_SourceObject
		self.m_SourceBindingType = m_SourceBindingType
		self.m_CreateOutputMethod = m_CreateOutputMethod


class PlayableExtensions:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayableGraph:

    offsets = {'m_Handle': 16, 'm_Version': 24}    
    def __init__(self, m_Handle: System.IntPtr, m_Version: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle
		self.m_Version = m_Version


class PlayableHandle:
	m_Null: UnityEngine.Playables.PlayableHandle
    offsets = {'m_Null': 0, 'm_Handle': 16, 'm_Version': 24}    
    def __init__(self, m_Null: UnityEngine.Playables.PlayableHandle, m_Handle: System.IntPtr, m_Version: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Null = m_Null
		self.m_Handle = m_Handle
		self.m_Version = m_Version


class PlayableOutput:
	m_NullPlayableOutput: UnityEngine.Playables.PlayableOutput
    offsets = {'m_NullPlayableOutput': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayableOutput: UnityEngine.Playables.PlayableOutput, m_Handle: UnityEngine.Playables.PlayableOutputHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayableOutput = m_NullPlayableOutput
		self.m_Handle = m_Handle


class PlayableOutputExtensions:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayableOutputHandle:
	m_Null: UnityEngine.Playables.PlayableOutputHandle
    offsets = {'m_Null': 0, 'm_Handle': 16, 'm_Version': 24}    
    def __init__(self, m_Null: UnityEngine.Playables.PlayableOutputHandle, m_Handle: System.IntPtr, m_Version: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Null = m_Null
		self.m_Handle = m_Handle
		self.m_Version = m_Version


class ScriptPlayableOutput:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableOutputHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class EarlyUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FixedUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Initialization:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PostLateUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PreLateUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PreUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Update:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Profiler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DebugScreenCapture:

    offsets = {'<rawImageDataReference>k__BackingField': 16, '<imageFormat>k__BackingField': 32, '<width>k__BackingField': 36, '<height>k__BackingField': 40}    
    def __init__(self, <rawImageDataReference>k__BackingField: Unity.Collections.NativeArray<System.Byte>, <imageFormat>k__BackingField: UnityEngine.TextureFormat, <width>k__BackingField: System.Int32, <height>k__BackingField: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<rawImageDataReference>k__BackingField = <rawImageDataReference>k__BackingField
		self.<imageFormat>k__BackingField = <imageFormat>k__BackingField
		self.<width>k__BackingField = <width>k__BackingField
		self.<height>k__BackingField = <height>k__BackingField


class MemoryProfiler:
	m_SnapshotFinished: System.Action<System.String,System.Boolean>
    offsets = {'m_SnapshotFinished': 0, 'm_SaveScreenshotToDisk': 8, 'createMetaData': 16}    
    def __init__(self, m_SnapshotFinished: System.Action<System.String,System.Boolean>, m_SaveScreenshotToDisk: System.Action<System.String,System.Boolean,UnityEngine.Profiling.Experimental.DebugScreenCapture>, createMetaData: System.Action<UnityEngine.Profiling.Memory.Experimental.MetaData>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_SnapshotFinished = m_SnapshotFinished
		self.m_SaveScreenshotToDisk = m_SaveScreenshotToDisk
		self.createMetaData = createMetaData


class MetaData:

    offsets = {'content': 16, 'platform': 24}    
    def __init__(self, content: System.String, platform: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.content = content
		self.platform = platform


class AmbientMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class BatchCullingContext:

    offsets = {'cullingPlanes': 16, 'batchVisibility': 32, 'visibleIndices': 48, 'lodParameters': 64}    
    def __init__(self, cullingPlanes: Unity.Collections.NativeArray<UnityEngine.Plane>, batchVisibility: Unity.Collections.NativeArray<UnityEngine.Rendering.BatchVisibility>, visibleIndices: Unity.Collections.NativeArray<System.Int32>, lodParameters: UnityEngine.Rendering.LODParameters, **kwargs):
        super().__init__(self, **kwargs)
		self.cullingPlanes = cullingPlanes
		self.batchVisibility = batchVisibility
		self.visibleIndices = visibleIndices
		self.lodParameters = lodParameters


class BatchRendererCullingOutput:

    offsets = {'cullingJobsFence': 16, 'cullingPlanesCount': 56, 'batchVisibilityCount': 60, 'visibleIndicesCount': 64}    
    def __init__(self, cullingJobsFence: Unity.Jobs.JobHandle, cullingPlanesCount: System.Int32, batchVisibilityCount: System.Int32, visibleIndicesCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.cullingJobsFence = cullingJobsFence
		self.cullingPlanesCount = cullingPlanesCount
		self.batchVisibilityCount = batchVisibilityCount
		self.visibleIndicesCount = visibleIndicesCount


class BatchRendererGroup:

    offsets = {'m_GroupHandle': 16, 'm_PerformCulling': 24}    
    def __init__(self, m_GroupHandle: System.IntPtr, m_PerformCulling: UnityEngine.Rendering.BatchRendererGroup.OnPerformCulling, **kwargs):
        super().__init__(self, **kwargs)
		self.m_GroupHandle = m_GroupHandle
		self.m_PerformCulling = m_PerformCulling


class BatchVisibility:

    offsets = {'offset': 16, 'instancesCount': 20, 'visibleCount': 24}    
    def __init__(self, offset: System.Int32, instancesCount: System.Int32, visibleCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.offset = offset
		self.instancesCount = instancesCount
		self.visibleCount = visibleCount


class BuiltinRenderTextureType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CameraEvent:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CameraEventUtils:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CameraProperties:

    offsets = {'screenRect': 16, 'viewDir': 32, 'projectionNear': 44, 'projectionFar': 48, 'cameraNear': 52, 'cameraFar': 56, 'cameraAspect': 60, 'cameraToWorld': 64, 'actualWorldToClip': 128, 'cameraClipToWorld': 192, 'cameraWorldToClip': 256, 'implicitProjection': 320, 'stereoWorldToClipLeft': 384, 'stereoWorldToClipRight': 448, 'worldToCamera': 512, 'up': 576, 'right': 588, 'transformDirection': 600, 'cameraEuler': 612, 'velocity': 624, 'farPlaneWorldSpaceLength': 636, 'rendererCount': 640, 'm_ShadowCullPlanes': 644, 'm_CameraCullPlanes': 740, 'baseFarDistance': 836, 'shadowCullCenter': 840, 'layerCullDistances': 852, 'layerCullSpherical': 980, 'coreCameraValues': 984, 'cameraType': 1000, 'projectionIsOblique': 1004, 'isImplicitProjectionMatrix': 1008}    
    def __init__(self, screenRect: UnityEngine.Rect, viewDir: UnityEngine.Vector3, projectionNear: System.Single, projectionFar: System.Single, cameraNear: System.Single, cameraFar: System.Single, cameraAspect: System.Single, cameraToWorld: UnityEngine.Matrix4x4, actualWorldToClip: UnityEngine.Matrix4x4, cameraClipToWorld: UnityEngine.Matrix4x4, cameraWorldToClip: UnityEngine.Matrix4x4, implicitProjection: UnityEngine.Matrix4x4, stereoWorldToClipLeft: UnityEngine.Matrix4x4, stereoWorldToClipRight: UnityEngine.Matrix4x4, worldToCamera: UnityEngine.Matrix4x4, up: UnityEngine.Vector3, right: UnityEngine.Vector3, transformDirection: UnityEngine.Vector3, cameraEuler: UnityEngine.Vector3, velocity: UnityEngine.Vector3, farPlaneWorldSpaceLength: System.Single, rendererCount: System.UInt32, m_ShadowCullPlanes: UnityEngine.Rendering.CameraProperties.<m_ShadowCullPlanes>e__FixedBuffer, m_CameraCullPlanes: UnityEngine.Rendering.CameraProperties.<m_CameraCullPlanes>e__FixedBuffer, baseFarDistance: System.Single, shadowCullCenter: UnityEngine.Vector3, layerCullDistances: UnityEngine.Rendering.CameraProperties.<layerCullDistances>e__FixedBuffer, layerCullSpherical: System.Int32, coreCameraValues: UnityEngine.Rendering.CoreCameraValues, cameraType: System.UInt32, projectionIsOblique: System.Int32, isImplicitProjectionMatrix: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.screenRect = screenRect
		self.viewDir = viewDir
		self.projectionNear = projectionNear
		self.projectionFar = projectionFar
		self.cameraNear = cameraNear
		self.cameraFar = cameraFar
		self.cameraAspect = cameraAspect
		self.cameraToWorld = cameraToWorld
		self.actualWorldToClip = actualWorldToClip
		self.cameraClipToWorld = cameraClipToWorld
		self.cameraWorldToClip = cameraWorldToClip
		self.implicitProjection = implicitProjection
		self.stereoWorldToClipLeft = stereoWorldToClipLeft
		self.stereoWorldToClipRight = stereoWorldToClipRight
		self.worldToCamera = worldToCamera
		self.up = up
		self.right = right
		self.transformDirection = transformDirection
		self.cameraEuler = cameraEuler
		self.velocity = velocity
		self.farPlaneWorldSpaceLength = farPlaneWorldSpaceLength
		self.rendererCount = rendererCount
		self.m_ShadowCullPlanes = m_ShadowCullPlanes
		self.m_CameraCullPlanes = m_CameraCullPlanes
		self.baseFarDistance = baseFarDistance
		self.shadowCullCenter = shadowCullCenter
		self.layerCullDistances = layerCullDistances
		self.layerCullSpherical = layerCullSpherical
		self.coreCameraValues = coreCameraValues
		self.cameraType = cameraType
		self.projectionIsOblique = projectionIsOblique
		self.isImplicitProjectionMatrix = isImplicitProjectionMatrix


class ColorWriteMask:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CommandBuffer:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class CompareFunction:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ComputeQueueType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CoreCameraValues:

    offsets = {'filterMode': 16, 'cullingMask': 20, 'instanceID': 24, 'renderImmediateObjects': 28}    
    def __init__(self, filterMode: System.Int32, cullingMask: System.UInt32, instanceID: System.Int32, renderImmediateObjects: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.filterMode = filterMode
		self.cullingMask = cullingMask
		self.instanceID = instanceID
		self.renderImmediateObjects = renderImmediateObjects


class CullingOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DefaultReflectionMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GraphicsSettings:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GraphicsTier:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class IndexFormat:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LODParameters:

    offsets = {'m_IsOrthographic': 16, 'm_CameraPosition': 20, 'm_FieldOfView': 32, 'm_OrthoSize': 36, 'm_CameraPixelHeight': 40}    
    def __init__(self, m_IsOrthographic: System.Int32, m_CameraPosition: UnityEngine.Vector3, m_FieldOfView: System.Single, m_OrthoSize: System.Single, m_CameraPixelHeight: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_IsOrthographic = m_IsOrthographic
		self.m_CameraPosition = m_CameraPosition
		self.m_FieldOfView = m_FieldOfView
		self.m_OrthoSize = m_OrthoSize
		self.m_CameraPixelHeight = m_CameraPixelHeight


class LightProbeUsage:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class MeshUpdateFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class OnDemandRendering:
	m_RenderFrameInterval: System.Int32
    offsets = {'m_RenderFrameInterval': 0}    
    def __init__(self, m_RenderFrameInterval: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_RenderFrameInterval = m_RenderFrameInterval


class OpaqueSortMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ReflectionProbeSortingCriteria:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ReflectionProbeUsage:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RenderPipeline:

    offsets = {'<disposed>k__BackingField': 16}    
    def __init__(self, <disposed>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<disposed>k__BackingField = <disposed>k__BackingField


class RenderPipelineAsset:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RenderPipelineManager:
	s_CurrentPipelineAsset: UnityEngine.Rendering.RenderPipelineAsset
    offsets = {'s_CurrentPipelineAsset': 0, 's_CameraCapacity': 16, '<currentPipeline>k__BackingField': 24}    
    def __init__(self, s_CurrentPipelineAsset: UnityEngine.Rendering.RenderPipelineAsset, s_CameraCapacity: System.Int32, <currentPipeline>k__BackingField: UnityEngine.Rendering.RenderPipeline, **kwargs):
        super().__init__(self, **kwargs)
		self.s_CurrentPipelineAsset = s_CurrentPipelineAsset
		self.s_CameraCapacity = s_CameraCapacity
		self.<currentPipeline>k__BackingField = <currentPipeline>k__BackingField


class RenderTargetIdentifier:

    offsets = {'m_Type': 16, 'm_NameID': 20, 'm_InstanceID': 24, 'm_BufferPointer': 32, 'm_MipLevel': 40, 'm_CubeFace': 44, 'm_DepthSlice': 48}    
    def __init__(self, m_Type: UnityEngine.Rendering.BuiltinRenderTextureType, m_NameID: System.Int32, m_InstanceID: System.Int32, m_BufferPointer: System.IntPtr, m_MipLevel: System.Int32, m_CubeFace: UnityEngine.CubemapFace, m_DepthSlice: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Type = m_Type
		self.m_NameID = m_NameID
		self.m_InstanceID = m_InstanceID
		self.m_BufferPointer = m_BufferPointer
		self.m_MipLevel = m_MipLevel
		self.m_CubeFace = m_CubeFace
		self.m_DepthSlice = m_DepthSlice


class RenderTextureSubElement:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ScriptableCullingParameters:
	maximumCullingPlaneCount: System.Int32
    offsets = {'maximumCullingPlaneCount': 0, 'layerCount': 4, 'm_IsOrthographic': 16, 'm_LODParameters': 20, 'm_CullingPlanes': 48, 'm_CullingPlaneCount': 208, 'm_CullingMask': 212, 'm_SceneMask': 216, 'm_LayerFarCullDistances': 224, 'm_LayerCull': 352, 'm_CullingMatrix': 356, 'm_Origin': 420, 'm_ShadowDistance': 432, 'm_CullingOptions': 436, 'm_ReflectionProbeSortingCriteria': 440, 'm_CameraProperties': 444, 'm_AccurateOcclusionThreshold': 1440, 'm_MaximumPortalCullingJobs': 1444, 'm_StereoViewMatrix': 1448, 'm_StereoProjectionMatrix': 1512, 'm_StereoSeparationDistance': 1576, 'm_maximumVisibleLights': 1580}    
    def __init__(self, maximumCullingPlaneCount: System.Int32, layerCount: System.Int32, m_IsOrthographic: System.Int32, m_LODParameters: UnityEngine.Rendering.LODParameters, m_CullingPlanes: UnityEngine.Rendering.ScriptableCullingParameters.<m_CullingPlanes>e__FixedBuffer, m_CullingPlaneCount: System.Int32, m_CullingMask: System.UInt32, m_SceneMask: System.UInt64, m_LayerFarCullDistances: UnityEngine.Rendering.ScriptableCullingParameters.<m_LayerFarCullDistances>e__FixedBuffer, m_LayerCull: System.Int32, m_CullingMatrix: UnityEngine.Matrix4x4, m_Origin: UnityEngine.Vector3, m_ShadowDistance: System.Single, m_CullingOptions: UnityEngine.Rendering.CullingOptions, m_ReflectionProbeSortingCriteria: UnityEngine.Rendering.ReflectionProbeSortingCriteria, m_CameraProperties: UnityEngine.Rendering.CameraProperties, m_AccurateOcclusionThreshold: System.Single, m_MaximumPortalCullingJobs: System.Int32, m_StereoViewMatrix: UnityEngine.Matrix4x4, m_StereoProjectionMatrix: UnityEngine.Matrix4x4, m_StereoSeparationDistance: System.Single, m_maximumVisibleLights: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.maximumCullingPlaneCount = maximumCullingPlaneCount
		self.layerCount = layerCount
		self.m_IsOrthographic = m_IsOrthographic
		self.m_LODParameters = m_LODParameters
		self.m_CullingPlanes = m_CullingPlanes
		self.m_CullingPlaneCount = m_CullingPlaneCount
		self.m_CullingMask = m_CullingMask
		self.m_SceneMask = m_SceneMask
		self.m_LayerFarCullDistances = m_LayerFarCullDistances
		self.m_LayerCull = m_LayerCull
		self.m_CullingMatrix = m_CullingMatrix
		self.m_Origin = m_Origin
		self.m_ShadowDistance = m_ShadowDistance
		self.m_CullingOptions = m_CullingOptions
		self.m_ReflectionProbeSortingCriteria = m_ReflectionProbeSortingCriteria
		self.m_CameraProperties = m_CameraProperties
		self.m_AccurateOcclusionThreshold = m_AccurateOcclusionThreshold
		self.m_MaximumPortalCullingJobs = m_MaximumPortalCullingJobs
		self.m_StereoViewMatrix = m_StereoViewMatrix
		self.m_StereoProjectionMatrix = m_StereoProjectionMatrix
		self.m_StereoSeparationDistance = m_StereoSeparationDistance
		self.m_maximumVisibleLights = m_maximumVisibleLights


class ScriptableRenderContext:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class ShaderHardwareTier:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ShaderPropertyFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ShaderPropertyType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ShaderTagId:
	none: UnityEngine.Rendering.ShaderTagId
    offsets = {'none': 0, 'm_Id': 16}    
    def __init__(self, none: UnityEngine.Rendering.ShaderTagId, m_Id: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.none = none
		self.m_Id = m_Id


class ShadowCastingMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ShadowSamplingMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SortingGroup:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SphericalHarmonicsL2:

    offsets = {'shr0': 16, 'shr1': 20, 'shr2': 24, 'shr3': 28, 'shr4': 32, 'shr5': 36, 'shr6': 40, 'shr7': 44, 'shr8': 48, 'shg0': 52, 'shg1': 56, 'shg2': 60, 'shg3': 64, 'shg4': 68, 'shg5': 72, 'shg6': 76, 'shg7': 80, 'shg8': 84, 'shb0': 88, 'shb1': 92, 'shb2': 96, 'shb3': 100, 'shb4': 104, 'shb5': 108, 'shb6': 112, 'shb7': 116, 'shb8': 120}    
    def __init__(self, shr0: System.Single, shr1: System.Single, shr2: System.Single, shr3: System.Single, shr4: System.Single, shr5: System.Single, shr6: System.Single, shr7: System.Single, shr8: System.Single, shg0: System.Single, shg1: System.Single, shg2: System.Single, shg3: System.Single, shg4: System.Single, shg5: System.Single, shg6: System.Single, shg7: System.Single, shg8: System.Single, shb0: System.Single, shb1: System.Single, shb2: System.Single, shb3: System.Single, shb4: System.Single, shb5: System.Single, shb6: System.Single, shb7: System.Single, shb8: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.shr0 = shr0
		self.shr1 = shr1
		self.shr2 = shr2
		self.shr3 = shr3
		self.shr4 = shr4
		self.shr5 = shr5
		self.shr6 = shr6
		self.shr7 = shr7
		self.shr8 = shr8
		self.shg0 = shg0
		self.shg1 = shg1
		self.shg2 = shg2
		self.shg3 = shg3
		self.shg4 = shg4
		self.shg5 = shg5
		self.shg6 = shg6
		self.shg7 = shg7
		self.shg8 = shg8
		self.shb0 = shb0
		self.shb1 = shb1
		self.shb2 = shb2
		self.shb3 = shb3
		self.shb4 = shb4
		self.shb5 = shb5
		self.shb6 = shb6
		self.shb7 = shb7
		self.shb8 = shb8


class StencilOp:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SubMeshDescriptor:

    offsets = {'<bounds>k__BackingField': 16, '<topology>k__BackingField': 40, '<indexStart>k__BackingField': 44, '<indexCount>k__BackingField': 48, '<baseVertex>k__BackingField': 52, '<firstVertex>k__BackingField': 56, '<vertexCount>k__BackingField': 60}    
    def __init__(self, <bounds>k__BackingField: UnityEngine.Bounds, <topology>k__BackingField: UnityEngine.MeshTopology, <indexStart>k__BackingField: System.Int32, <indexCount>k__BackingField: System.Int32, <baseVertex>k__BackingField: System.Int32, <firstVertex>k__BackingField: System.Int32, <vertexCount>k__BackingField: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<bounds>k__BackingField = <bounds>k__BackingField
		self.<topology>k__BackingField = <topology>k__BackingField
		self.<indexStart>k__BackingField = <indexStart>k__BackingField
		self.<indexCount>k__BackingField = <indexCount>k__BackingField
		self.<baseVertex>k__BackingField = <baseVertex>k__BackingField
		self.<firstVertex>k__BackingField = <firstVertex>k__BackingField
		self.<vertexCount>k__BackingField = <vertexCount>k__BackingField


class SupportedRenderingFeatures:
	s_Active: UnityEngine.Rendering.SupportedRenderingFeatures
    offsets = {'s_Active': 0, '<reflectionProbeModes>k__BackingField': 16, '<defaultMixedLightingModes>k__BackingField': 20, '<mixedLightingModes>k__BackingField': 24, '<lightmapBakeTypes>k__BackingField': 28, '<lightmapsModes>k__BackingField': 32, '<enlighten>k__BackingField': 36, '<lightProbeProxyVolumes>k__BackingField': 37, '<motionVectors>k__BackingField': 38, '<receiveShadows>k__BackingField': 39, '<reflectionProbes>k__BackingField': 40, '<rendererPriority>k__BackingField': 41, '<terrainDetailUnsupported>k__BackingField': 42, '<overridesEnvironmentLighting>k__BackingField': 43, '<overridesFog>k__BackingField': 44, '<overridesOtherLightingSettings>k__BackingField': 45, '<editableMaterialRenderQueue>k__BackingField': 46, '<overridesLODBias>k__BackingField': 47, '<overridesMaximumLODLevel>k__BackingField': 48}    
    def __init__(self, s_Active: UnityEngine.Rendering.SupportedRenderingFeatures, <reflectionProbeModes>k__BackingField: UnityEngine.Rendering.SupportedRenderingFeatures.ReflectionProbeModes, <defaultMixedLightingModes>k__BackingField: UnityEngine.Rendering.SupportedRenderingFeatures.LightmapMixedBakeModes, <mixedLightingModes>k__BackingField: UnityEngine.Rendering.SupportedRenderingFeatures.LightmapMixedBakeModes, <lightmapBakeTypes>k__BackingField: UnityEngine.LightmapBakeType, <lightmapsModes>k__BackingField: UnityEngine.LightmapsMode, <enlighten>k__BackingField: System.Boolean, <lightProbeProxyVolumes>k__BackingField: System.Boolean, <motionVectors>k__BackingField: System.Boolean, <receiveShadows>k__BackingField: System.Boolean, <reflectionProbes>k__BackingField: System.Boolean, <rendererPriority>k__BackingField: System.Boolean, <terrainDetailUnsupported>k__BackingField: System.Boolean, <overridesEnvironmentLighting>k__BackingField: System.Boolean, <overridesFog>k__BackingField: System.Boolean, <overridesOtherLightingSettings>k__BackingField: System.Boolean, <editableMaterialRenderQueue>k__BackingField: System.Boolean, <overridesLODBias>k__BackingField: System.Boolean, <overridesMaximumLODLevel>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Active = s_Active
		self.<reflectionProbeModes>k__BackingField = <reflectionProbeModes>k__BackingField
		self.<defaultMixedLightingModes>k__BackingField = <defaultMixedLightingModes>k__BackingField
		self.<mixedLightingModes>k__BackingField = <mixedLightingModes>k__BackingField
		self.<lightmapBakeTypes>k__BackingField = <lightmapBakeTypes>k__BackingField
		self.<lightmapsModes>k__BackingField = <lightmapsModes>k__BackingField
		self.<enlighten>k__BackingField = <enlighten>k__BackingField
		self.<lightProbeProxyVolumes>k__BackingField = <lightProbeProxyVolumes>k__BackingField
		self.<motionVectors>k__BackingField = <motionVectors>k__BackingField
		self.<receiveShadows>k__BackingField = <receiveShadows>k__BackingField
		self.<reflectionProbes>k__BackingField = <reflectionProbes>k__BackingField
		self.<rendererPriority>k__BackingField = <rendererPriority>k__BackingField
		self.<terrainDetailUnsupported>k__BackingField = <terrainDetailUnsupported>k__BackingField
		self.<overridesEnvironmentLighting>k__BackingField = <overridesEnvironmentLighting>k__BackingField
		self.<overridesFog>k__BackingField = <overridesFog>k__BackingField
		self.<overridesOtherLightingSettings>k__BackingField = <overridesOtherLightingSettings>k__BackingField
		self.<editableMaterialRenderQueue>k__BackingField = <editableMaterialRenderQueue>k__BackingField
		self.<overridesLODBias>k__BackingField = <overridesLODBias>k__BackingField
		self.<overridesMaximumLODLevel>k__BackingField = <overridesMaximumLODLevel>k__BackingField


class TextureDimension:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VertexAttribute:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VertexAttributeDescriptor:

    offsets = {'<attribute>k__BackingField': 16, '<format>k__BackingField': 20, '<dimension>k__BackingField': 24, '<stream>k__BackingField': 28}    
    def __init__(self, <attribute>k__BackingField: UnityEngine.Rendering.VertexAttribute, <format>k__BackingField: UnityEngine.Rendering.VertexAttributeFormat, <dimension>k__BackingField: System.Int32, <stream>k__BackingField: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<attribute>k__BackingField = <attribute>k__BackingField
		self.<format>k__BackingField = <format>k__BackingField
		self.<dimension>k__BackingField = <dimension>k__BackingField
		self.<stream>k__BackingField = <stream>k__BackingField


class VertexAttributeFormat:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LoadSceneMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LoadSceneParameters:

    offsets = {'m_LoadSceneMode': 16, 'm_LocalPhysicsMode': 20}    
    def __init__(self, m_LoadSceneMode: UnityEngine.SceneManagement.LoadSceneMode, m_LocalPhysicsMode: UnityEngine.SceneManagement.LocalPhysicsMode, **kwargs):
        super().__init__(self, **kwargs)
		self.m_LoadSceneMode = m_LoadSceneMode
		self.m_LocalPhysicsMode = m_LocalPhysicsMode


class LocalPhysicsMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Scene:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class SceneManager:
	s_AllowLoadScene: System.Boolean
    offsets = {'s_AllowLoadScene': 0, 'sceneLoaded': 8, 'sceneUnloaded': 16, 'activeSceneChanged': 24}    
    def __init__(self, s_AllowLoadScene: System.Boolean, sceneLoaded: UnityEngine.Events.UnityAction<UnityEngine.SceneManagement.Scene,UnityEngine.SceneManagement.LoadSceneMode>, sceneUnloaded: UnityEngine.Events.UnityAction<UnityEngine.SceneManagement.Scene>, activeSceneChanged: UnityEngine.Events.UnityAction<UnityEngine.SceneManagement.Scene,UnityEngine.SceneManagement.Scene>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_AllowLoadScene = s_AllowLoadScene
		self.sceneLoaded = sceneLoaded
		self.sceneUnloaded = sceneUnloaded
		self.activeSceneChanged = activeSceneChanged


class SceneManagerAPIInternal:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnloadSceneOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PreserveAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MovedFromAttribute:

    offsets = {'data': 16}    
    def __init__(self, data: UnityEngine.Scripting.APIUpdating.MovedFromAttributeData, **kwargs):
        super().__init__(self, **kwargs)
		self.data = data


class MovedFromAttributeData:

    offsets = {'className': 16, 'nameSpace': 24, 'assembly': 32, 'classHasChanged': 40, 'nameSpaceHasChanged': 41, 'assemblyHasChanged': 42, 'autoUdpateAPI': 43}    
    def __init__(self, className: System.String, nameSpace: System.String, assembly: System.String, classHasChanged: System.Boolean, nameSpaceHasChanged: System.Boolean, assemblyHasChanged: System.Boolean, autoUdpateAPI: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.className = className
		self.nameSpace = nameSpace
		self.assembly = assembly
		self.classHasChanged = classHasChanged
		self.nameSpaceHasChanged = nameSpaceHasChanged
		self.assemblyHasChanged = assemblyHasChanged
		self.autoUdpateAPI = autoUdpateAPI


class FormerlySerializedAsAttribute:

    offsets = {'m_oldName': 16}    
    def __init__(self, m_oldName: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_oldName = m_oldName


class DataUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SpriteAtlas:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SpriteAtlasManager:
	atlasRequested: System.Action<System.String,System.Action<UnityEngine.U2D.SpriteAtlas>>
    offsets = {'atlasRequested': 0, 'atlasRegistered': 8}    
    def __init__(self, atlasRequested: System.Action<System.String,System.Action<UnityEngine.U2D.SpriteAtlas>>, atlasRegistered: System.Action<UnityEngine.U2D.SpriteAtlas>, **kwargs):
        super().__init__(self, **kwargs)
		self.atlasRequested = atlasRequested
		self.atlasRegistered = atlasRegistered


class SpriteBone:

    offsets = {'m_Name': 16, 'm_Position': 24, 'm_Rotation': 36, 'm_Length': 52, 'm_ParentId': 56}    
    def __init__(self, m_Name: System.String, m_Position: UnityEngine.Vector3, m_Rotation: UnityEngine.Quaternion, m_Length: System.Single, m_ParentId: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Name = m_Name
		self.m_Position = m_Position
		self.m_Rotation = m_Rotation
		self.m_Length = m_Length
		self.m_ParentId = m_ParentId


class ConfidenceLevel:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DictationCompletionCause:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DictationRecognizer:

    offsets = {'m_Recognizer': 16, 'DictationHypothesis': 24, 'DictationResult': 32, 'DictationComplete': 40, 'DictationError': 48}    
    def __init__(self, m_Recognizer: System.IntPtr, DictationHypothesis: UnityEngine.Windows.Speech.DictationRecognizer.DictationHypothesisDelegate, DictationResult: UnityEngine.Windows.Speech.DictationRecognizer.DictationResultDelegate, DictationComplete: UnityEngine.Windows.Speech.DictationRecognizer.DictationCompletedDelegate, DictationError: UnityEngine.Windows.Speech.DictationRecognizer.DictationErrorHandler, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Recognizer = m_Recognizer
		self.DictationHypothesis = DictationHypothesis
		self.DictationResult = DictationResult
		self.DictationComplete = DictationComplete
		self.DictationError = DictationError


class PhraseRecognitionSystem:
	OnError: UnityEngine.Windows.Speech.PhraseRecognitionSystem.ErrorDelegate
    offsets = {'OnError': 0, 'OnStatusChanged': 8}    
    def __init__(self, OnError: UnityEngine.Windows.Speech.PhraseRecognitionSystem.ErrorDelegate, OnStatusChanged: UnityEngine.Windows.Speech.PhraseRecognitionSystem.StatusDelegate, **kwargs):
        super().__init__(self, **kwargs)
		self.OnError = OnError
		self.OnStatusChanged = OnStatusChanged


class PhraseRecognizedEventArgs:

    offsets = {'confidence': 16, 'text': 32, 'phraseStartTime': 40, 'phraseDuration': 48}    
    def __init__(self, confidence: UnityEngine.Windows.Speech.ConfidenceLevel, text: System.String, phraseStartTime: System.DateTime, phraseDuration: System.TimeSpan, **kwargs):
        super().__init__(self, **kwargs)
		self.confidence = confidence
		self.text = text
		self.phraseStartTime = phraseStartTime
		self.phraseDuration = phraseDuration


class PhraseRecognizer:

    offsets = {'m_Recognizer': 16, 'OnPhraseRecognized': 24}    
    def __init__(self, m_Recognizer: System.IntPtr, OnPhraseRecognized: UnityEngine.Windows.Speech.PhraseRecognizer.PhraseRecognizedDelegate, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Recognizer = m_Recognizer
		self.OnPhraseRecognized = OnPhraseRecognized


class SemanticMeaning:

    offsets = {'key': 16}    
    def __init__(self, key: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.key = key


class SpeechError:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SpeechSystemStatus:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CapturePixelFormat:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PhotoCapture:
	HR_SUCCESS: System.Int64
    offsets = {'HR_SUCCESS': 0, 'm_NativePtr': 16}    
    def __init__(self, HR_SUCCESS: System.Int64, m_NativePtr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.HR_SUCCESS = HR_SUCCESS
		self.m_NativePtr = m_NativePtr


class PhotoCaptureFrame:

    offsets = {'m_NativePtr': 16, '<dataLength>k__BackingField': 24, '<hasLocationData>k__BackingField': 28, '<pixelFormat>k__BackingField': 32}    
    def __init__(self, m_NativePtr: System.IntPtr, <dataLength>k__BackingField: System.Int32, <hasLocationData>k__BackingField: System.Boolean, <pixelFormat>k__BackingField: UnityEngine.Windows.WebCam.CapturePixelFormat, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NativePtr = m_NativePtr
		self.<dataLength>k__BackingField = <dataLength>k__BackingField
		self.<hasLocationData>k__BackingField = <hasLocationData>k__BackingField
		self.<pixelFormat>k__BackingField = <pixelFormat>k__BackingField


class VideoCapture:
	HR_SUCCESS: System.Int64
    offsets = {'HR_SUCCESS': 0, 'm_NativePtr': 16}    
    def __init__(self, HR_SUCCESS: System.Int64, m_NativePtr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.HR_SUCCESS = HR_SUCCESS
		self.m_NativePtr = m_NativePtr


class APIUpdaterRuntimeHelpers:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GenericStack:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MathfInternal:
	FloatMinNormal: System.Single
    offsets = {'FloatMinNormal': 0, 'FloatMinDenormal': 4, 'IsFlushToZeroEnabled': 8}    
    def __init__(self, FloatMinNormal: System.Single, FloatMinDenormal: System.Single, IsFlushToZeroEnabled: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.FloatMinNormal = FloatMinNormal
		self.FloatMinDenormal = FloatMinDenormal
		self.IsFlushToZeroEnabled = IsFlushToZeroEnabled


class TypeInferenceRuleAttribute:

    offsets = {'_rule': 16}    
    def __init__(self, _rule: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self._rule = _rule


class TypeInferenceRules:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__