


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <PrivateImplementationDetails>:
	FE8212EABC2145162026C28CCC7324192E0DB919: System.Int64
    offsets = {'FE8212EABC2145162026C28CCC7324192E0DB919': 0}    
    def __init__(self, FE8212EABC2145162026C28CCC7324192E0DB919: System.Int64, **kwargs):
        super().__init__(self, **kwargs)
		self.FE8212EABC2145162026C28CCC7324192E0DB919 = FE8212EABC2145162026C28CCC7324192E0DB919


class DelegateList<T>:

    offsets = {'m_acquireFunc': 0, 'm_releaseFunc': 0, 'm_callbacks': 0, 'm_invoking': 0}    
    def __init__(self, m_acquireFunc: System.Func<System.Action<T>,System.Collections.Generic.LinkedListNode<System.Action<T>>>, m_releaseFunc: System.Action<System.Collections.Generic.LinkedListNode<System.Action<T>>>, m_callbacks: System.Collections.Generic.LinkedList<System.Action<T>>, m_invoking: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_acquireFunc = m_acquireFunc
		self.m_releaseFunc = m_releaseFunc
		self.m_callbacks = m_callbacks
		self.m_invoking = m_invoking


class ListWithEvents<T>:

    offsets = {'m_List': 0, 'OnElementAdded': 0, 'OnElementRemoved': 0}    
    def __init__(self, m_List: System.Collections.Generic.List<T>, OnElementAdded: System.Action<T>, OnElementRemoved: System.Action<T>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_List = m_List
		self.OnElementAdded = OnElementAdded
		self.OnElementRemoved = OnElementRemoved


class MonoBehaviourCallbackHooks:

    offsets = {'m_OnUpdateDelegate': 24}    
    def __init__(self, m_OnUpdateDelegate: System.Action<System.Single>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_OnUpdateDelegate = m_OnUpdateDelegate


class <>c__DisplayClass42_0<TObject>:

    offsets = {'handle': 0}    
    def __init__(self, handle: System.Threading.WaitHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.handle = handle


class <>c__DisplayClass44_0<TObject>:

    offsets = {'handle': 0}    
    def __init__(self, handle: System.Threading.WaitHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.handle = handle


class <>c__DisplayClass55_0<TObject>:

    offsets = {'value': 0}    
    def __init__(self, value: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value


class <>c__DisplayClass56_0<TObject>:

    offsets = {'value': 0}    
    def __init__(self, value: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value


class GroupOperationSettings:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class <>c:
	<>9: UnityEngine.ResourceManagement.Diagnostics.DiagnosticEventCollectorSingleton.<>c
    offsets = {'<>9': 0, '<>9__8_0': 8, '<>9__11_0': 16}    
    def __init__(self, <>9: UnityEngine.ResourceManagement.Diagnostics.DiagnosticEventCollectorSingleton.<>c, <>9__8_0: System.Func<UnityEngine.ResourceManagement.Diagnostics.DiagnosticEvent,System.Int32>, <>9__11_0: System.Action<UnityEngine.ResourceManagement.Diagnostics.DiagnosticEvent>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__8_0 = <>9__8_0
		self.<>9__11_0 = <>9__11_0


class <>c__DisplayClass83_0<TObject>:

    offsets = {'callback': 0, 'releaseDependenciesOnFailure': 0, '<>4__this': 0}    
    def __init__(self, callback: System.Action<TObject>, releaseDependenciesOnFailure: System.Boolean, <>4__this: UnityEngine.ResourceManagement.ResourceManager, **kwargs):
        super().__init__(self, **kwargs)
		self.callback = callback
		self.releaseDependenciesOnFailure = releaseDependenciesOnFailure
		self.<>4__this = <>4__this


class CompletedOperation<TObject>:

    offsets = {'m_Success': 0, 'm_ErrorMsg': 0, 'm_ReleaseDependenciesOnFailure': 0}    
    def __init__(self, m_Success: System.Boolean, m_ErrorMsg: System.String, m_ReleaseDependenciesOnFailure: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Success = m_Success
		self.m_ErrorMsg = m_ErrorMsg
		self.m_ReleaseDependenciesOnFailure = m_ReleaseDependenciesOnFailure


class DiagnosticEventContext:

    offsets = {'<OperationHandle>k__BackingField': 16, '<Type>k__BackingField': 40, '<EventValue>k__BackingField': 44, '<Location>k__BackingField': 48, '<Context>k__BackingField': 56, '<Error>k__BackingField': 64}    
    def __init__(self, <OperationHandle>k__BackingField: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle, <Type>k__BackingField: UnityEngine.ResourceManagement.ResourceManager.DiagnosticEventType, <EventValue>k__BackingField: System.Int32, <Location>k__BackingField: UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation, <Context>k__BackingField: System.Object, <Error>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<OperationHandle>k__BackingField = <OperationHandle>k__BackingField
		self.<Type>k__BackingField = <Type>k__BackingField
		self.<EventValue>k__BackingField = <EventValue>k__BackingField
		self.<Location>k__BackingField = <Location>k__BackingField
		self.<Context>k__BackingField = <Context>k__BackingField
		self.<Error>k__BackingField = <Error>k__BackingField


class DiagnosticEventType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class InstanceOperation:

    offsets = {'m_dependency': 128, 'm_instantiationParams': 152, 'm_instanceProvider': 200, 'm_instance': 208, 'm_scene': 216}    
    def __init__(self, m_dependency: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<UnityEngine.GameObject>, m_instantiationParams: UnityEngine.ResourceManagement.ResourceProviders.InstantiationParameters, m_instanceProvider: UnityEngine.ResourceManagement.ResourceProviders.IInstanceProvider, m_instance: UnityEngine.GameObject, m_scene: UnityEngine.SceneManagement.Scene, **kwargs):
        super().__init__(self, **kwargs)
		self.m_dependency = m_dependency
		self.m_instantiationParams = m_instantiationParams
		self.m_instanceProvider = m_instanceProvider
		self.m_instance = m_instance
		self.m_scene = m_scene


class InternalOp:

    offsets = {'m_RequestOperation': 16, 'm_ProvideHandle': 24, 'subObjectName': 48}    
    def __init__(self, m_RequestOperation: UnityEngine.AssetBundleRequest, m_ProvideHandle: UnityEngine.ResourceManagement.ResourceProviders.ProvideHandle, subObjectName: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_RequestOperation = m_RequestOperation
		self.m_ProvideHandle = m_ProvideHandle
		self.subObjectName = subObjectName


class InternalOp:

    offsets = {'m_RequestOperation': 16, 'm_ProvideHandle': 24}    
    def __init__(self, m_RequestOperation: UnityEngine.AsyncOperation, m_ProvideHandle: UnityEngine.ResourceManagement.ResourceProviders.ProvideHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_RequestOperation = m_RequestOperation
		self.m_ProvideHandle = m_ProvideHandle


class <>c__DisplayClass10_0:

    offsets = {'<>4__this': 16, 'id': 24, 'data': 32}    
    def __init__(self, <>4__this: UnityEngine.ResourceManagement.ResourceProviders.ResourceProviderBase, id: System.String, data: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.id = id
		self.data = data


class BaseInitAsyncOp:

    offsets = {'m_CallBack': 128}    
    def __init__(self, m_CallBack: System.Func<System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_CallBack = m_CallBack


class SceneOp:

    offsets = {'m_ActivateOnLoad': 136, 'm_Inst': 144, 'm_Location': 160, 'm_LoadMode': 168, 'm_Priority': 172, 'm_DepOp': 176, 'm_ResourceManager': 200}    
    def __init__(self, m_ActivateOnLoad: System.Boolean, m_Inst: UnityEngine.ResourceManagement.ResourceProviders.SceneInstance, m_Location: UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation, m_LoadMode: UnityEngine.SceneManagement.LoadSceneMode, m_Priority: System.Int32, m_DepOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<System.Collections.Generic.IList<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>>, m_ResourceManager: UnityEngine.ResourceManagement.ResourceManager, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ActivateOnLoad = m_ActivateOnLoad
		self.m_Inst = m_Inst
		self.m_Location = m_Location
		self.m_LoadMode = m_LoadMode
		self.m_Priority = m_Priority
		self.m_DepOp = m_DepOp
		self.m_ResourceManager = m_ResourceManager


class UnloadSceneOp:

    offsets = {'m_Instance': 136, 'm_sceneLoadHandle': 152}    
    def __init__(self, m_Instance: UnityEngine.ResourceManagement.ResourceProviders.SceneInstance, m_sceneLoadHandle: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<UnityEngine.ResourceManagement.ResourceProviders.SceneInstance>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Instance = m_Instance
		self.m_sceneLoadHandle = m_sceneLoadHandle


class InternalOp:

    offsets = {'m_Provider': 16, 'm_RequestOperation': 24, 'm_RequestQueueOperation': 32, 'm_IgnoreFailures': 40, 'm_PI': 48}    
    def __init__(self, m_Provider: UnityEngine.ResourceManagement.ResourceProviders.TextDataProvider, m_RequestOperation: UnityEngine.Networking.UnityWebRequestAsyncOperation, m_RequestQueueOperation: UnityEngine.ResourceManagement.WebRequestQueueOperation, m_IgnoreFailures: System.Boolean, m_PI: UnityEngine.ResourceManagement.ResourceProviders.ProvideHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Provider = m_Provider
		self.m_RequestOperation = m_RequestOperation
		self.m_RequestQueueOperation = m_RequestQueueOperation
		self.m_IgnoreFailures = m_IgnoreFailures
		self.m_PI = m_PI


class DelegateInfo:
	s_Id: System.Int32
    offsets = {'s_Id': 0, 'm_Id': 16, 'm_Delegate': 24, '<InvocationTime>k__BackingField': 40}    
    def __init__(self, s_Id: System.Int32, m_Id: System.Int32, m_Delegate: System.Delegate, <InvocationTime>k__BackingField: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Id = s_Id
		self.m_Id = m_Id
		self.m_Delegate = m_Delegate
		self.<InvocationTime>k__BackingField = <InvocationTime>k__BackingField


class ChainOperation<TObject,TObjectDependency>:

    offsets = {'m_DepOp': 0, 'm_WrappedOp': 0, 'm_Callback': 0, 'm_CachedOnWrappedCompleted': 0, 'm_ReleaseDependenciesOnFailure': 0}    
    def __init__(self, m_DepOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObjectDependency>, m_WrappedOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObject>, m_Callback: System.Func<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObjectDependency>,UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObject>>, m_CachedOnWrappedCompleted: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObject>>, m_ReleaseDependenciesOnFailure: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DepOp = m_DepOp
		self.m_WrappedOp = m_WrappedOp
		self.m_Callback = m_Callback
		self.m_CachedOnWrappedCompleted = m_CachedOnWrappedCompleted
		self.m_ReleaseDependenciesOnFailure = m_ReleaseDependenciesOnFailure


class ChainOperationTypelessDepedency<TObject>:

    offsets = {'m_DepOp': 0, 'm_WrappedOp': 0, 'm_Callback': 0, 'm_CachedOnWrappedCompleted': 0, 'm_ReleaseDependenciesOnFailure': 0}    
    def __init__(self, m_DepOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle, m_WrappedOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObject>, m_Callback: System.Func<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle,UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObject>>, m_CachedOnWrappedCompleted: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObject>>, m_ReleaseDependenciesOnFailure: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DepOp = m_DepOp
		self.m_WrappedOp = m_WrappedOp
		self.m_Callback = m_Callback
		self.m_CachedOnWrappedCompleted = m_CachedOnWrappedCompleted
		self.m_ReleaseDependenciesOnFailure = m_ReleaseDependenciesOnFailure


class IUpdateReceiver:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ResourceManager:
	<ExceptionHandler>k__BackingField: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle,System.Exception>
    offsets = {'<ExceptionHandler>k__BackingField': 0, 's_GroupOperationTypeHash': 8, 's_InstanceOperationTypeHash': 12, 'postProfilerEvents': 16, '<InternalIdTransformFunc>k__BackingField': 24, 'CallbackHooksEnabled': 32, 'm_ResourceProviders': 40, 'm_allocator': 48, 'm_UpdateReceivers': 56, 'm_UpdateReceiversToRemove': 64, 'm_UpdatingReceivers': 72, 'm_providerMap': 80, 'm_AssetOperationCache': 88, 'm_TrackedInstanceOperations': 96, 'm_UpdateCallbacks': 104, 'm_DeferredCompleteCallbacks': 112, 'm_obsoleteDiagnosticsHandler': 120, 'm_diagnosticsHandler': 128, 'm_ReleaseOpNonCached': 136, 'm_ReleaseOpCached': 144, 'm_ReleaseInstanceOp': 152, '<CertificateHandlerInstance>k__BackingField': 160, 'm_RegisteredForCallbacks': 168, 'm_ProviderOperationTypeCache': 176}    
    def __init__(self, <ExceptionHandler>k__BackingField: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle,System.Exception>, s_GroupOperationTypeHash: System.Int32, s_InstanceOperationTypeHash: System.Int32, postProfilerEvents: System.Boolean, <InternalIdTransformFunc>k__BackingField: System.Func<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation,System.String>, CallbackHooksEnabled: System.Boolean, m_ResourceProviders: ListWithEvents<UnityEngine.ResourceManagement.ResourceProviders.IResourceProvider>, m_allocator: UnityEngine.ResourceManagement.Util.IAllocationStrategy, m_UpdateReceivers: ListWithEvents<UnityEngine.ResourceManagement.IUpdateReceiver>, m_UpdateReceiversToRemove: System.Collections.Generic.List<UnityEngine.ResourceManagement.IUpdateReceiver>, m_UpdatingReceivers: System.Boolean, m_providerMap: System.Collections.Generic.Dictionary<System.Int32,UnityEngine.ResourceManagement.ResourceProviders.IResourceProvider>, m_AssetOperationCache: System.Collections.Generic.Dictionary<System.Int32,UnityEngine.ResourceManagement.AsyncOperations.IAsyncOperation>, m_TrackedInstanceOperations: System.Collections.Generic.HashSet<UnityEngine.ResourceManagement.ResourceManager.InstanceOperation>, m_UpdateCallbacks: DelegateList<System.Single>, m_DeferredCompleteCallbacks: System.Collections.Generic.List<UnityEngine.ResourceManagement.AsyncOperations.IAsyncOperation>, m_obsoleteDiagnosticsHandler: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle,UnityEngine.ResourceManagement.ResourceManager.DiagnosticEventType,System.Int32,System.Object>, m_diagnosticsHandler: System.Action<UnityEngine.ResourceManagement.ResourceManager.DiagnosticEventContext>, m_ReleaseOpNonCached: System.Action<UnityEngine.ResourceManagement.AsyncOperations.IAsyncOperation>, m_ReleaseOpCached: System.Action<UnityEngine.ResourceManagement.AsyncOperations.IAsyncOperation>, m_ReleaseInstanceOp: System.Action<UnityEngine.ResourceManagement.AsyncOperations.IAsyncOperation>, <CertificateHandlerInstance>k__BackingField: UnityEngine.Networking.CertificateHandler, m_RegisteredForCallbacks: System.Boolean, m_ProviderOperationTypeCache: System.Collections.Generic.Dictionary<System.Type,System.Type>, **kwargs):
        super().__init__(self, **kwargs)
		self.<ExceptionHandler>k__BackingField = <ExceptionHandler>k__BackingField
		self.s_GroupOperationTypeHash = s_GroupOperationTypeHash
		self.s_InstanceOperationTypeHash = s_InstanceOperationTypeHash
		self.postProfilerEvents = postProfilerEvents
		self.<InternalIdTransformFunc>k__BackingField = <InternalIdTransformFunc>k__BackingField
		self.CallbackHooksEnabled = CallbackHooksEnabled
		self.m_ResourceProviders = m_ResourceProviders
		self.m_allocator = m_allocator
		self.m_UpdateReceivers = m_UpdateReceivers
		self.m_UpdateReceiversToRemove = m_UpdateReceiversToRemove
		self.m_UpdatingReceivers = m_UpdatingReceivers
		self.m_providerMap = m_providerMap
		self.m_AssetOperationCache = m_AssetOperationCache
		self.m_TrackedInstanceOperations = m_TrackedInstanceOperations
		self.m_UpdateCallbacks = m_UpdateCallbacks
		self.m_DeferredCompleteCallbacks = m_DeferredCompleteCallbacks
		self.m_obsoleteDiagnosticsHandler = m_obsoleteDiagnosticsHandler
		self.m_diagnosticsHandler = m_diagnosticsHandler
		self.m_ReleaseOpNonCached = m_ReleaseOpNonCached
		self.m_ReleaseOpCached = m_ReleaseOpCached
		self.m_ReleaseInstanceOp = m_ReleaseInstanceOp
		self.<CertificateHandlerInstance>k__BackingField = <CertificateHandlerInstance>k__BackingField
		self.m_RegisteredForCallbacks = m_RegisteredForCallbacks
		self.m_ProviderOperationTypeCache = m_ProviderOperationTypeCache


class WebRequestQueue:
	s_MaxRequest: System.Int32
    offsets = {'s_MaxRequest': 0, 's_QueuedOperations': 8, 's_ActiveRequests': 16}    
    def __init__(self, s_MaxRequest: System.Int32, s_QueuedOperations: System.Collections.Generic.Queue<UnityEngine.ResourceManagement.WebRequestQueueOperation>, s_ActiveRequests: System.Collections.Generic.List<UnityEngine.Networking.UnityWebRequestAsyncOperation>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_MaxRequest = s_MaxRequest
		self.s_QueuedOperations = s_QueuedOperations
		self.s_ActiveRequests = s_ActiveRequests


class WebRequestQueueOperation:

    offsets = {'Result': 16, 'OnComplete': 24, 'm_WebRequest': 32}    
    def __init__(self, Result: UnityEngine.Networking.UnityWebRequestAsyncOperation, OnComplete: System.Action<UnityEngine.Networking.UnityWebRequestAsyncOperation>, m_WebRequest: UnityEngine.Networking.UnityWebRequest, **kwargs):
        super().__init__(self, **kwargs)
		self.Result = Result
		self.OnComplete = OnComplete
		self.m_WebRequest = m_WebRequest


class AsyncOperationBase<TObject>:

    offsets = {'<Result>k__BackingField': 0, 'm_referenceCount': 0, 'm_Status': 0, 'm_Error': 0, 'm_RM': 0, 'm_Version': 0, 'm_DestroyedAction': 0, 'm_CompletedActionT': 0, 'm_OnDestroyAction': 0, 'm_dependencyCompleteAction': 0, '<IsRunning>k__BackingField': 0, 'm_waitHandle': 0, 'm_InDeferredCallbackQueue': 0, 'm_UpdateCallbacks': 0, 'm_UpdateCallback': 0}    
    def __init__(self, <Result>k__BackingField: TObject, m_referenceCount: System.Int32, m_Status: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationStatus, m_Error: System.Exception, m_RM: UnityEngine.ResourceManagement.ResourceManager, m_Version: System.Int32, m_DestroyedAction: DelegateList<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, m_CompletedActionT: DelegateList<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<TObject>>, m_OnDestroyAction: System.Action<UnityEngine.ResourceManagement.AsyncOperations.IAsyncOperation>, m_dependencyCompleteAction: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, <IsRunning>k__BackingField: System.Boolean, m_waitHandle: System.Threading.EventWaitHandle, m_InDeferredCallbackQueue: System.Boolean, m_UpdateCallbacks: DelegateList<System.Single>, m_UpdateCallback: System.Action<System.Single>, **kwargs):
        super().__init__(self, **kwargs)
		self.<Result>k__BackingField = <Result>k__BackingField
		self.m_referenceCount = m_referenceCount
		self.m_Status = m_Status
		self.m_Error = m_Error
		self.m_RM = m_RM
		self.m_Version = m_Version
		self.m_DestroyedAction = m_DestroyedAction
		self.m_CompletedActionT = m_CompletedActionT
		self.m_OnDestroyAction = m_OnDestroyAction
		self.m_dependencyCompleteAction = m_dependencyCompleteAction
		self.<IsRunning>k__BackingField = <IsRunning>k__BackingField
		self.m_waitHandle = m_waitHandle
		self.m_InDeferredCallbackQueue = m_InDeferredCallbackQueue
		self.m_UpdateCallbacks = m_UpdateCallbacks
		self.m_UpdateCallback = m_UpdateCallback


class AsyncOperationHandle:

    offsets = {'m_InternalOp': 16, 'm_Version': 24, 'm_LocationName': 32}    
    def __init__(self, m_InternalOp: UnityEngine.ResourceManagement.AsyncOperations.IAsyncOperation, m_Version: System.Int32, m_LocationName: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_InternalOp = m_InternalOp
		self.m_Version = m_Version
		self.m_LocationName = m_LocationName


class AsyncOperationHandle<TObject>:

    offsets = {'m_InternalOp': 0, 'm_Version': 0, 'm_LocationName': 0}    
    def __init__(self, m_InternalOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationBase<TObject>, m_Version: System.Int32, m_LocationName: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_InternalOp = m_InternalOp
		self.m_Version = m_Version
		self.m_LocationName = m_LocationName


class AsyncOperationStatus:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DownloadStatus:

    offsets = {'TotalBytes': 16, 'DownloadedBytes': 24, 'IsDone': 32}    
    def __init__(self, TotalBytes: System.Int64, DownloadedBytes: System.Int64, IsDone: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.TotalBytes = TotalBytes
		self.DownloadedBytes = DownloadedBytes
		self.IsDone = IsDone


class GroupOperation:

    offsets = {'m_InternalOnComplete': 128, 'm_LoadedCount': 136, 'm_Settings': 140, 'debugName': 144, '<UnityEngine.ResourceManagement.AsyncOperations.ICachable.Hash>k__BackingField': 152, 'm_CachedDependencyLocations': 160}    
    def __init__(self, m_InternalOnComplete: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, m_LoadedCount: System.Int32, m_Settings: UnityEngine.ResourceManagement.AsyncOperations.GroupOperation.GroupOperationSettings, debugName: System.String, <UnityEngine.ResourceManagement.AsyncOperations.ICachable.Hash>k__BackingField: System.Int32, m_CachedDependencyLocations: System.Collections.Generic.HashSet<System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_InternalOnComplete = m_InternalOnComplete
		self.m_LoadedCount = m_LoadedCount
		self.m_Settings = m_Settings
		self.debugName = debugName
		self.<UnityEngine.ResourceManagement.AsyncOperations.ICachable.Hash>k__BackingField = <UnityEngine.ResourceManagement.AsyncOperations.ICachable.Hash>k__BackingField
		self.m_CachedDependencyLocations = m_CachedDependencyLocations


class IAsyncOperation:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ICachable:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IGenericProviderOperation:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProviderOperation<TObject>:

    offsets = {'m_ReleaseDependenciesOnFailure': 0, 'm_CompletionCallback': 0, 'm_GetDepCallback': 0, 'm_GetProgressCallback': 0, 'm_GetDownloadProgressCallback': 0, 'm_DownloadStatus': 0, 'm_Provider': 0, 'm_DepOp': 0, 'm_Location': 0, 'm_ProvideHandleVersion': 0, 'm_NeedsRelease': 0, '<UnityEngine.ResourceManagement.AsyncOperations.ICachable.Hash>k__BackingField': 0, 'm_ResourceManager': 0}    
    def __init__(self, m_ReleaseDependenciesOnFailure: System.Boolean, m_CompletionCallback: System.Action<System.Int32,System.Object,System.Boolean,System.Exception>, m_GetDepCallback: System.Action<System.Int32,System.Collections.Generic.IList<System.Object>>, m_GetProgressCallback: System.Func<System.Single>, m_GetDownloadProgressCallback: System.Func<UnityEngine.ResourceManagement.AsyncOperations.DownloadStatus>, m_DownloadStatus: UnityEngine.ResourceManagement.AsyncOperations.DownloadStatus, m_Provider: UnityEngine.ResourceManagement.ResourceProviders.IResourceProvider, m_DepOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<System.Collections.Generic.IList<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>>, m_Location: UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation, m_ProvideHandleVersion: System.Int32, m_NeedsRelease: System.Boolean, <UnityEngine.ResourceManagement.AsyncOperations.ICachable.Hash>k__BackingField: System.Int32, m_ResourceManager: UnityEngine.ResourceManagement.ResourceManager, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ReleaseDependenciesOnFailure = m_ReleaseDependenciesOnFailure
		self.m_CompletionCallback = m_CompletionCallback
		self.m_GetDepCallback = m_GetDepCallback
		self.m_GetProgressCallback = m_GetProgressCallback
		self.m_GetDownloadProgressCallback = m_GetDownloadProgressCallback
		self.m_DownloadStatus = m_DownloadStatus
		self.m_Provider = m_Provider
		self.m_DepOp = m_DepOp
		self.m_Location = m_Location
		self.m_ProvideHandleVersion = m_ProvideHandleVersion
		self.m_NeedsRelease = m_NeedsRelease
		self.<UnityEngine.ResourceManagement.AsyncOperations.ICachable.Hash>k__BackingField = <UnityEngine.ResourceManagement.AsyncOperations.ICachable.Hash>k__BackingField
		self.m_ResourceManager = m_ResourceManager


class DiagnosticEvent:

    offsets = {'m_Graph': 16, 'm_ObjectId': 32, 'm_DisplayName': 40, 'm_Stream': 48, 'm_Frame': 52, 'm_Value': 56}    
    def __init__(self, m_Graph: System.String, m_ObjectId: System.Int32, m_DisplayName: System.String, m_Stream: System.Int32, m_Frame: System.Int32, m_Value: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Graph = m_Graph
		self.m_ObjectId = m_ObjectId
		self.m_DisplayName = m_DisplayName
		self.m_Stream = m_Stream
		self.m_Frame = m_Frame
		self.m_Value = m_Value


class DiagnosticEventCollector:
	s_Collector: UnityEngine.ResourceManagement.Diagnostics.DiagnosticEventCollector
    offsets = {'s_Collector': 0}    
    def __init__(self, s_Collector: UnityEngine.ResourceManagement.Diagnostics.DiagnosticEventCollector, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Collector = s_Collector


class DiagnosticEventCollectorSingleton:
	s_editorConnectionGuid: System.Guid
    offsets = {'s_editorConnectionGuid': 0, 'm_CreatedEvents': 24, 'm_UnhandledEvents': 32, 's_EventHandlers': 40, 'm_lastTickSent': 48, 'm_lastFrame': 52, 'fpsAvg': 56}    
    def __init__(self, s_editorConnectionGuid: System.Guid, m_CreatedEvents: System.Collections.Generic.Dictionary<System.Int32,UnityEngine.ResourceManagement.Diagnostics.DiagnosticEvent>, m_UnhandledEvents: System.Collections.Generic.List<UnityEngine.ResourceManagement.Diagnostics.DiagnosticEvent>, s_EventHandlers: DelegateList<UnityEngine.ResourceManagement.Diagnostics.DiagnosticEvent>, m_lastTickSent: System.Single, m_lastFrame: System.Int32, fpsAvg: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.s_editorConnectionGuid = s_editorConnectionGuid
		self.m_CreatedEvents = m_CreatedEvents
		self.m_UnhandledEvents = m_UnhandledEvents
		self.s_EventHandlers = s_EventHandlers
		self.m_lastTickSent = m_lastTickSent
		self.m_lastFrame = m_lastFrame
		self.fpsAvg = fpsAvg


class ResourceManagerException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnknownResourceProviderException:

    offsets = {'<Location>k__BackingField': 136}    
    def __init__(self, <Location>k__BackingField: UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation, **kwargs):
        super().__init__(self, **kwargs)
		self.<Location>k__BackingField = <Location>k__BackingField


class ILocationSizeData:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IResourceLocation:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ResourceLocationBase:

    offsets = {'m_Name': 16, 'm_Id': 24, 'm_ProviderId': 32, 'm_Data': 40, 'm_DependencyHashCode': 48, 'm_HashCode': 52, 'm_Type': 56, 'm_Dependencies': 64, 'm_PrimaryKey': 72}    
    def __init__(self, m_Name: System.String, m_Id: System.String, m_ProviderId: System.String, m_Data: System.Object, m_DependencyHashCode: System.Int32, m_HashCode: System.Int32, m_Type: System.Type, m_Dependencies: System.Collections.Generic.List<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation>, m_PrimaryKey: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Name = m_Name
		self.m_Id = m_Id
		self.m_ProviderId = m_ProviderId
		self.m_Data = m_Data
		self.m_DependencyHashCode = m_DependencyHashCode
		self.m_HashCode = m_HashCode
		self.m_Type = m_Type
		self.m_Dependencies = m_Dependencies
		self.m_PrimaryKey = m_PrimaryKey


class AssetBundleProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AssetBundleRequestOptions:

    offsets = {'m_Hash': 16, 'm_Crc': 24, 'm_Timeout': 28, 'm_ChunkedTransfer': 32, 'm_RedirectLimit': 36, 'm_RetryCount': 40, 'm_BundleName': 48, 'm_BundleSize': 56, 'm_UseCrcForCachedBundles': 64}    
    def __init__(self, m_Hash: System.String, m_Crc: System.UInt32, m_Timeout: System.Int32, m_ChunkedTransfer: System.Boolean, m_RedirectLimit: System.Int32, m_RetryCount: System.Int32, m_BundleName: System.String, m_BundleSize: System.Int64, m_UseCrcForCachedBundles: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Hash = m_Hash
		self.m_Crc = m_Crc
		self.m_Timeout = m_Timeout
		self.m_ChunkedTransfer = m_ChunkedTransfer
		self.m_RedirectLimit = m_RedirectLimit
		self.m_RetryCount = m_RetryCount
		self.m_BundleName = m_BundleName
		self.m_BundleSize = m_BundleSize
		self.m_UseCrcForCachedBundles = m_UseCrcForCachedBundles


class AssetBundleResource:

    offsets = {'m_AssetBundle': 16, 'm_downloadHandler': 24, 'm_RequestOperation': 32, 'm_WebRequestQueueOperation': 40, 'm_ProvideHandle': 48, 'm_Options': 72, 'm_Retries': 80, 'm_BytesToDownload': 88}    
    def __init__(self, m_AssetBundle: UnityEngine.AssetBundle, m_downloadHandler: UnityEngine.Networking.DownloadHandlerAssetBundle, m_RequestOperation: UnityEngine.AsyncOperation, m_WebRequestQueueOperation: UnityEngine.ResourceManagement.WebRequestQueueOperation, m_ProvideHandle: UnityEngine.ResourceManagement.ResourceProviders.ProvideHandle, m_Options: UnityEngine.ResourceManagement.ResourceProviders.AssetBundleRequestOptions, m_Retries: System.Int32, m_BytesToDownload: System.Int64, **kwargs):
        super().__init__(self, **kwargs)
		self.m_AssetBundle = m_AssetBundle
		self.m_downloadHandler = m_downloadHandler
		self.m_RequestOperation = m_RequestOperation
		self.m_WebRequestQueueOperation = m_WebRequestQueueOperation
		self.m_ProvideHandle = m_ProvideHandle
		self.m_Options = m_Options
		self.m_Retries = m_Retries
		self.m_BytesToDownload = m_BytesToDownload


class AtlasSpriteProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class BundledAssetProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IAssetBundleResource:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IInstanceProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IResourceProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ISceneProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class InstanceProvider:

    offsets = {'m_InstanceObjectToPrefabHandle': 16}    
    def __init__(self, m_InstanceObjectToPrefabHandle: System.Collections.Generic.Dictionary<UnityEngine.GameObject,UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<UnityEngine.GameObject>>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_InstanceObjectToPrefabHandle = m_InstanceObjectToPrefabHandle


class InstantiationParameters:

    offsets = {'m_Position': 16, 'm_Rotation': 28, 'm_Parent': 48, 'm_InstantiateInWorldPosition': 56, 'm_SetPositionRotation': 57}    
    def __init__(self, m_Position: UnityEngine.Vector3, m_Rotation: UnityEngine.Quaternion, m_Parent: UnityEngine.Transform, m_InstantiateInWorldPosition: System.Boolean, m_SetPositionRotation: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Position = m_Position
		self.m_Rotation = m_Rotation
		self.m_Parent = m_Parent
		self.m_InstantiateInWorldPosition = m_InstantiateInWorldPosition
		self.m_SetPositionRotation = m_SetPositionRotation


class JsonAssetProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LegacyResourcesProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProvideHandle:

    offsets = {'m_Version': 16, 'm_InternalOp': 24, 'm_ResourceManager': 32}    
    def __init__(self, m_Version: System.Int32, m_InternalOp: UnityEngine.ResourceManagement.AsyncOperations.IGenericProviderOperation, m_ResourceManager: UnityEngine.ResourceManagement.ResourceManager, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Version = m_Version
		self.m_InternalOp = m_InternalOp
		self.m_ResourceManager = m_ResourceManager


class ProviderBehaviourFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ResourceProviderBase:

    offsets = {'m_ProviderId': 16, 'm_BehaviourFlags': 24}    
    def __init__(self, m_ProviderId: System.String, m_BehaviourFlags: UnityEngine.ResourceManagement.ResourceProviders.ProviderBehaviourFlags, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ProviderId = m_ProviderId
		self.m_BehaviourFlags = m_BehaviourFlags


class SceneInstance:

    offsets = {'m_Scene': 16, 'm_Operation': 24}    
    def __init__(self, m_Scene: UnityEngine.SceneManagement.Scene, m_Operation: UnityEngine.AsyncOperation, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Scene = m_Scene
		self.m_Operation = m_Operation


class SceneProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TextDataProvider:

    offsets = {'<IgnoreFailures>k__BackingField': 32}    
    def __init__(self, <IgnoreFailures>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<IgnoreFailures>k__BackingField = <IgnoreFailures>k__BackingField


class ComponentSingleton<T>:
	s_Instance: T
    offsets = {'s_Instance': 0}    
    def __init__(self, s_Instance: T, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Instance = s_Instance


class DefaultAllocationStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DelayedActionManager:

    offsets = {'m_DelayedActions': 32, 'm_NodeCache': 40, 'm_CollectionIndex': 48, 'm_DestroyOnCompletion': 52}    
    def __init__(self, m_DelayedActions: System.Collections.Generic.LinkedList<UnityEngine.ResourceManagement.Util.DelayedActionManager.DelegateInfo>, m_NodeCache: System.Collections.Generic.Stack<System.Collections.Generic.LinkedListNode<UnityEngine.ResourceManagement.Util.DelayedActionManager.DelegateInfo>>, m_CollectionIndex: System.Int32, m_DestroyOnCompletion: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DelayedActions = m_DelayedActions
		self.m_NodeCache = m_NodeCache
		self.m_CollectionIndex = m_CollectionIndex
		self.m_DestroyOnCompletion = m_DestroyOnCompletion


class GlobalLinkedListNodeCache<T>:
	m_globalCache: UnityEngine.ResourceManagement.Util.LinkedListNodeCache<T>
    offsets = {'m_globalCache': 0}    
    def __init__(self, m_globalCache: UnityEngine.ResourceManagement.Util.LinkedListNodeCache<T>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_globalCache = m_globalCache


class IAllocationStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IInitializableObject:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IObjectInitializationDataProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LRUCacheAllocationStrategy:

    offsets = {'m_poolMaxSize': 16, 'm_poolInitialCapacity': 20, 'm_poolCacheMaxSize': 24, 'm_poolCache': 32, 'm_cache': 40}    
    def __init__(self, m_poolMaxSize: System.Int32, m_poolInitialCapacity: System.Int32, m_poolCacheMaxSize: System.Int32, m_poolCache: System.Collections.Generic.List<System.Collections.Generic.List<System.Object>>, m_cache: System.Collections.Generic.Dictionary<System.Int32,System.Collections.Generic.List<System.Object>>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_poolMaxSize = m_poolMaxSize
		self.m_poolInitialCapacity = m_poolInitialCapacity
		self.m_poolCacheMaxSize = m_poolCacheMaxSize
		self.m_poolCache = m_poolCache
		self.m_cache = m_cache


class LinkedListNodeCache<T>:

    offsets = {'m_NodesCreated': 0, 'm_NodeCache': 0}    
    def __init__(self, m_NodesCreated: System.Int32, m_NodeCache: System.Collections.Generic.LinkedList<T>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NodesCreated = m_NodesCreated
		self.m_NodeCache = m_NodeCache


class ObjectInitializationData:

    offsets = {'m_Id': 16, 'm_ObjectType': 24, 'm_Data': 56}    
    def __init__(self, m_Id: System.String, m_ObjectType: UnityEngine.ResourceManagement.Util.SerializedType, m_Data: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Id = m_Id
		self.m_ObjectType = m_ObjectType
		self.m_Data = m_Data


class ResourceManagerConfig:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SerializedType:

    offsets = {'m_AssemblyName': 16, 'm_ClassName': 24, 'm_CachedType': 32, '<ValueChanged>k__BackingField': 40}    
    def __init__(self, m_AssemblyName: System.String, m_ClassName: System.String, m_CachedType: System.Type, <ValueChanged>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_AssemblyName = m_AssemblyName
		self.m_ClassName = m_ClassName
		self.m_CachedType = m_CachedType
		self.<ValueChanged>k__BackingField = <ValueChanged>k__BackingField


class SerializedTypeRestrictionAttribute:

    offsets = {'type': 16}    
    def __init__(self, type: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.type = type