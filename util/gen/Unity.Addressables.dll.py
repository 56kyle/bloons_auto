


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PackedPlayModeBuildLogs:

    offsets = {'m_RuntimeBuildLogs': 16}    
    def __init__(self, m_RuntimeBuildLogs: System.Collections.Generic.List<PackedPlayModeBuildLogs.RuntimeBuildLog>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_RuntimeBuildLogs = m_RuntimeBuildLogs


class RuntimeBuildLog:

    offsets = {'Type': 16, 'Message': 24}    
    def __init__(self, Type: UnityEngine.LogType, Message: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.Type = Type
		self.Message = Message


class MergeMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class <>c:
	<>9: UnityEngine.AddressableAssets.AddressablesImpl.<>c
    offsets = {'<>9': 0, '<>9__51_0': 8, '<>9__122_0': 16, '<>9__122_1': 24}    
    def __init__(self, <>9: UnityEngine.AddressableAssets.AddressablesImpl.<>c, <>9__51_0: System.Func<UnityEngine.AddressableAssets.AddressablesImpl.ResourceLocatorInfo,UnityEngine.AddressableAssets.ResourceLocators.IResourceLocator>, <>9__122_0: System.Func<UnityEngine.AddressableAssets.AddressablesImpl.ResourceLocatorInfo,System.Boolean>, <>9__122_1: System.Func<UnityEngine.AddressableAssets.AddressablesImpl.ResourceLocatorInfo,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__51_0 = <>9__51_0
		self.<>9__122_0 = <>9__122_0
		self.<>9__122_1 = <>9__122_1


class <>c__DisplayClass104_0:

    offsets = {'<>4__this': 16, 'key': 24, 'instantiateParameters': 32}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, key: System.Object, instantiateParameters: UnityEngine.ResourceManagement.ResourceProviders.InstantiationParameters, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.key = key
		self.instantiateParameters = instantiateParameters


class <>c__DisplayClass106_0:

    offsets = {'<>4__this': 16, 'location': 24, 'instantiateParameters': 32}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, location: UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation, instantiateParameters: UnityEngine.ResourceManagement.ResourceProviders.InstantiationParameters, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.location = location
		self.instantiateParameters = instantiateParameters


class <>c__DisplayClass109_0:

    offsets = {'<>4__this': 16, 'key': 24, 'loadMode': 32, 'activateOnLoad': 36, 'priority': 40}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, key: System.Object, loadMode: UnityEngine.SceneManagement.LoadSceneMode, activateOnLoad: System.Boolean, priority: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.key = key
		self.loadMode = loadMode
		self.activateOnLoad = activateOnLoad
		self.priority = priority


class <>c__DisplayClass115_0:

    offsets = {'<>4__this': 16, 'autoReleaseHandle': 24}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, autoReleaseHandle: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.autoReleaseHandle = autoReleaseHandle


class <>c__DisplayClass116_0:

    offsets = {'<>4__this': 16, 'autoReleaseHandle': 24}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, autoReleaseHandle: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.autoReleaseHandle = autoReleaseHandle


class <>c__DisplayClass123_0:

    offsets = {'<>4__this': 16, 'autoReleaseHandle': 24}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, autoReleaseHandle: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.autoReleaseHandle = autoReleaseHandle


class <>c__DisplayClass33_0:

    offsets = {'op': 16, '<>4__this': 40}    
    def __init__(self, op: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<UnityEngine.ResourceManagement.ResourceProviders.SceneInstance>, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, **kwargs):
        super().__init__(self, **kwargs)
		self.op = op
		self.<>4__this = <>4__this


class <>c__DisplayClass53_0:

    offsets = {'loc': 16}    
    def __init__(self, loc: UnityEngine.AddressableAssets.ResourceLocators.IResourceLocator, **kwargs):
        super().__init__(self, **kwargs)
		self.loc = loc


class <>c__DisplayClass60_0:

    offsets = {'<>4__this': 16, 'catalogPath': 24, 'autoReleaseHandle': 32, 'providerSuffix': 40, 'handle': 48}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, catalogPath: System.String, autoReleaseHandle: System.Boolean, providerSuffix: System.String, handle: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<UnityEngine.AddressableAssets.ResourceLocators.IResourceLocator>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.catalogPath = catalogPath
		self.autoReleaseHandle = autoReleaseHandle
		self.providerSuffix = providerSuffix
		self.handle = handle


class <>c__DisplayClass66_0<TObject>:

    offsets = {'<>4__this': 0, 'key': 0}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, key: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.key = key


class <>c__DisplayClass70_0:

    offsets = {'<>4__this': 16, 'keys': 24, 'mode': 32, 'type': 40}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, keys: System.Collections.IEnumerable, mode: UnityEngine.AddressableAssets.Addressables.MergeMode, type: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.keys = keys
		self.mode = mode
		self.type = type


class <>c__DisplayClass72_0:

    offsets = {'<>4__this': 16, 'key': 24, 'type': 32}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, key: System.Object, type: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.key = key
		self.type = type


class <>c__DisplayClass75_0<TObject>:

    offsets = {'<>4__this': 0, 'keys': 0, 'callback': 0, 'mode': 0, 'releaseDependenciesOnFailure': 0}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, keys: System.Collections.IEnumerable, callback: System.Action<TObject>, mode: UnityEngine.AddressableAssets.Addressables.MergeMode, releaseDependenciesOnFailure: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.keys = keys
		self.callback = callback
		self.mode = mode
		self.releaseDependenciesOnFailure = releaseDependenciesOnFailure


class <>c__DisplayClass77_0<TObject>:

    offsets = {'<>4__this': 0, 'key': 0, 'callback': 0, 'releaseDependenciesOnFailure': 0}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, key: System.Object, callback: System.Action<TObject>, releaseDependenciesOnFailure: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.key = key
		self.callback = callback
		self.releaseDependenciesOnFailure = releaseDependenciesOnFailure


class <>c__DisplayClass85_0:

    offsets = {'<>4__this': 16, 'key': 24}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, key: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.key = key


class <>c__DisplayClass86_0:

    offsets = {'<>4__this': 16, 'keys': 24}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, keys: System.Collections.IEnumerable, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.keys = keys


class <>c__DisplayClass89_0:

    offsets = {'<>4__this': 16, 'key': 24}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, key: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.key = key


class <>c__DisplayClass92_0:

    offsets = {'<>4__this': 16, 'locations': 24}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, locations: System.Collections.Generic.IList<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.locations = locations


class <>c__DisplayClass94_0:

    offsets = {'<>4__this': 16, 'keys': 24, 'mode': 32}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, keys: System.Collections.IEnumerable, mode: UnityEngine.AddressableAssets.Addressables.MergeMode, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.keys = keys
		self.mode = mode


class <>c__DisplayClass97_0:

    offsets = {'<>4__this': 16, 'key': 24, 'autoReleaseHandle': 32}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, key: System.Object, autoReleaseHandle: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.key = key
		self.autoReleaseHandle = autoReleaseHandle


class <>c__DisplayClass98_0:

    offsets = {'<>4__this': 16, 'locations': 24, 'autoReleaseHandle': 32}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, locations: System.Collections.Generic.IList<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation>, autoReleaseHandle: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.locations = locations
		self.autoReleaseHandle = autoReleaseHandle


class <>c__DisplayClass99_0:

    offsets = {'<>4__this': 16, 'keys': 24, 'autoReleaseHandle': 32}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.AddressablesImpl, keys: System.Collections.IEnumerable, autoReleaseHandle: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.keys = keys
		self.autoReleaseHandle = autoReleaseHandle


class LoadResourceLocationKeyOp:

    offsets = {'m_Keys': 128, 'm_locations': 136, 'm_Addressables': 144, 'm_ResourceType': 152}    
    def __init__(self, m_Keys: System.Object, m_locations: System.Collections.Generic.IList<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation>, m_Addressables: UnityEngine.AddressableAssets.AddressablesImpl, m_ResourceType: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Keys = m_Keys
		self.m_locations = m_locations
		self.m_Addressables = m_Addressables
		self.m_ResourceType = m_ResourceType


class LoadResourceLocationKeysOp:

    offsets = {'m_Key': 128, 'm_MergeMode': 136, 'm_locations': 144, 'm_Addressables': 152, 'm_ResourceType': 160}    
    def __init__(self, m_Key: System.Collections.IEnumerable, m_MergeMode: UnityEngine.AddressableAssets.Addressables.MergeMode, m_locations: System.Collections.Generic.IList<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation>, m_Addressables: UnityEngine.AddressableAssets.AddressablesImpl, m_ResourceType: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Key = m_Key
		self.m_MergeMode = m_MergeMode
		self.m_locations = m_locations
		self.m_Addressables = m_Addressables
		self.m_ResourceType = m_ResourceType


class ResourceLocatorInfo:

    offsets = {'<Locator>k__BackingField': 16, '<LocalHash>k__BackingField': 24, '<CatalogLocation>k__BackingField': 32, '<ContentUpdateAvailable>k__BackingField': 40}    
    def __init__(self, <Locator>k__BackingField: UnityEngine.AddressableAssets.ResourceLocators.IResourceLocator, <LocalHash>k__BackingField: System.String, <CatalogLocation>k__BackingField: UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation, <ContentUpdateAvailable>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<Locator>k__BackingField = <Locator>k__BackingField
		self.<LocalHash>k__BackingField = <LocalHash>k__BackingField
		self.<CatalogLocation>k__BackingField = <CatalogLocation>k__BackingField
		self.<ContentUpdateAvailable>k__BackingField = <ContentUpdateAvailable>k__BackingField


class <>c:
	<>9: UnityEngine.AddressableAssets.CheckCatalogsOperation.<>c
    offsets = {'<>9': 0, '<>9__5_0': 8}    
    def __init__(self, <>9: UnityEngine.AddressableAssets.CheckCatalogsOperation.<>c, <>9__5_0: System.Func<UnityEngine.ResourceManagement.ResourceProviders.IResourceProvider,System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__5_0 = <>9__5_0


class <>c__DisplayClass1_0:

    offsets = {'<>4__this': 16, 'id': 24, 'data': 32}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.Initialization.CacheInitialization, id: System.String, data: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.id = id
		self.data = data


class CacheInitOp:

    offsets = {'m_Callback': 128, 'm_UpdateRequired': 136}    
    def __init__(self, m_Callback: System.Func<System.Boolean>, m_UpdateRequired: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Callback = m_Callback
		self.m_UpdateRequired = m_UpdateRequired


class <>c:
	<>9: UnityEngine.AddressableAssets.Initialization.InitializationOperation.<>c
    offsets = {'<>9': 0, '<>9__11_0': 8}    
    def __init__(self, <>9: UnityEngine.AddressableAssets.Initialization.InitializationOperation.<>c, <>9__11_0: System.Func<UnityEngine.ResourceManagement.ResourceProviders.IResourceProvider,System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__11_0 = <>9__11_0


class <>c__DisplayClass14_0:

    offsets = {'addressables': 16, 'providerSuffix': 24}    
    def __init__(self, addressables: UnityEngine.AddressableAssets.AddressablesImpl, providerSuffix: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.addressables = addressables
		self.providerSuffix = providerSuffix


class <>c__DisplayClass16_0:

    offsets = {'<>4__this': 16, 'locMap': 24, 'index': 32, 'catalogs': 40}    
    def __init__(self, <>4__this: UnityEngine.AddressableAssets.Initialization.InitializationOperation, locMap: UnityEngine.AddressableAssets.ResourceLocators.ResourceLocationMap, index: System.Int32, catalogs: System.Collections.Generic.IList<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>4__this = <>4__this
		self.locMap = locMap
		self.index = index
		self.catalogs = catalogs


class Bucket:

    offsets = {'dataOffset': 16}    
    def __init__(self, dataOffset: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.dataOffset = dataOffset


class CompactLocation:

    offsets = {'m_Locator': 16, 'm_InternalId': 24, 'm_ProviderId': 32, 'm_Dependency': 40, 'm_Data': 48, 'm_HashCode': 56, 'm_DependencyHashCode': 60, 'm_PrimaryKey': 64, 'm_Type': 72}    
    def __init__(self, m_Locator: UnityEngine.AddressableAssets.ResourceLocators.ResourceLocationMap, m_InternalId: System.String, m_ProviderId: System.String, m_Dependency: System.Object, m_Data: System.Object, m_HashCode: System.Int32, m_DependencyHashCode: System.Int32, m_PrimaryKey: System.String, m_Type: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Locator = m_Locator
		self.m_InternalId = m_InternalId
		self.m_ProviderId = m_ProviderId
		self.m_Dependency = m_Dependency
		self.m_Data = m_Data
		self.m_HashCode = m_HashCode
		self.m_DependencyHashCode = m_DependencyHashCode
		self.m_PrimaryKey = m_PrimaryKey
		self.m_Type = m_Type


class DependencyHashIndex:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class InternalOp:

    offsets = {'m_LocalDataPath': 16, 'm_RemoteHashValue': 24, 'm_LocalHashValue': 32, 'm_ProviderInterface': 40, 'm_ContentCatalogData': 64}    
    def __init__(self, m_LocalDataPath: System.String, m_RemoteHashValue: System.String, m_LocalHashValue: System.String, m_ProviderInterface: UnityEngine.ResourceManagement.ResourceProviders.ProvideHandle, m_ContentCatalogData: UnityEngine.AddressableAssets.ResourceLocators.ContentCatalogData, **kwargs):
        super().__init__(self, **kwargs)
		self.m_LocalDataPath = m_LocalDataPath
		self.m_RemoteHashValue = m_RemoteHashValue
		self.m_LocalHashValue = m_LocalHashValue
		self.m_ProviderInterface = m_ProviderInterface
		self.m_ContentCatalogData = m_ContentCatalogData


class BundledCatalog:

    offsets = {'m_BundlePath': 16, 'm_OpInProgress': 24, 'm_LoadBundleRequest': 32, 'm_CatalogAssetBundle': 40, 'm_LoadTextAssetRequest': 48, 'm_CatalogData': 56, 'OnLoaded': 64}    
    def __init__(self, m_BundlePath: System.String, m_OpInProgress: System.Boolean, m_LoadBundleRequest: UnityEngine.AssetBundleCreateRequest, m_CatalogAssetBundle: UnityEngine.AssetBundle, m_LoadTextAssetRequest: UnityEngine.AssetBundleRequest, m_CatalogData: UnityEngine.AddressableAssets.ResourceLocators.ContentCatalogData, OnLoaded: System.Action<UnityEngine.AddressableAssets.ResourceLocators.ContentCatalogData>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_BundlePath = m_BundlePath
		self.m_OpInProgress = m_OpInProgress
		self.m_LoadBundleRequest = m_LoadBundleRequest
		self.m_CatalogAssetBundle = m_CatalogAssetBundle
		self.m_LoadTextAssetRequest = m_LoadTextAssetRequest
		self.m_CatalogData = m_CatalogData
		self.OnLoaded = OnLoaded


class <>c:
	<>9: UnityEngine.AddressableAssets.UpdateCatalogsOperation.<>c
    offsets = {'<>9': 0, '<>9__4_0': 8}    
    def __init__(self, <>9: UnityEngine.AddressableAssets.UpdateCatalogsOperation.<>c, <>9__4_0: System.Func<UnityEngine.ResourceManagement.ResourceProviders.IResourceProvider,System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__4_0 = <>9__4_0


class ObjectType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AssetReferenceUILabelRestriction:

    offsets = {'m_CachedToString': 24}    
    def __init__(self, m_CachedToString: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_CachedToString = m_CachedToString


class AssetReferenceUIRestriction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Addressables:
	reinitializeAddressables: System.Boolean
    offsets = {'reinitializeAddressables': 0, 'm_AddressablesInstance': 8}    
    def __init__(self, reinitializeAddressables: System.Boolean, m_AddressablesInstance: UnityEngine.AddressableAssets.AddressablesImpl, **kwargs):
        super().__init__(self, **kwargs)
		self.reinitializeAddressables = reinitializeAddressables
		self.m_AddressablesInstance = m_AddressablesInstance


class AddressablesImpl:

    offsets = {'m_ResourceManager': 16, 'm_InstanceProvider': 24, 'SceneProvider': 32, 'm_ResourceLocators': 40, 'm_InitializationOperation': 48, 'm_ActiveCheckUpdateOperation': 72, 'm_ActiveUpdateOperation': 96, 'm_OnHandleCompleteAction': 120, 'm_OnSceneHandleCompleteAction': 128, 'm_OnHandleDestroyedAction': 136, 'm_resultToHandle': 144, 'm_SceneInstances': 152, 'hasStartedInitialization': 160}    
    def __init__(self, m_ResourceManager: UnityEngine.ResourceManagement.ResourceManager, m_InstanceProvider: UnityEngine.ResourceManagement.ResourceProviders.IInstanceProvider, SceneProvider: UnityEngine.ResourceManagement.ResourceProviders.ISceneProvider, m_ResourceLocators: System.Collections.Generic.List<UnityEngine.AddressableAssets.AddressablesImpl.ResourceLocatorInfo>, m_InitializationOperation: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<UnityEngine.AddressableAssets.ResourceLocators.IResourceLocator>, m_ActiveCheckUpdateOperation: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<System.Collections.Generic.List<System.String>>, m_ActiveUpdateOperation: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<System.Collections.Generic.List<UnityEngine.AddressableAssets.ResourceLocators.IResourceLocator>>, m_OnHandleCompleteAction: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, m_OnSceneHandleCompleteAction: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, m_OnHandleDestroyedAction: System.Action<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, m_resultToHandle: System.Collections.Generic.Dictionary<System.Object,UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, m_SceneInstances: System.Collections.Generic.HashSet<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>, hasStartedInitialization: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ResourceManager = m_ResourceManager
		self.m_InstanceProvider = m_InstanceProvider
		self.SceneProvider = SceneProvider
		self.m_ResourceLocators = m_ResourceLocators
		self.m_InitializationOperation = m_InitializationOperation
		self.m_ActiveCheckUpdateOperation = m_ActiveCheckUpdateOperation
		self.m_ActiveUpdateOperation = m_ActiveUpdateOperation
		self.m_OnHandleCompleteAction = m_OnHandleCompleteAction
		self.m_OnSceneHandleCompleteAction = m_OnSceneHandleCompleteAction
		self.m_OnHandleDestroyedAction = m_OnHandleDestroyedAction
		self.m_resultToHandle = m_resultToHandle
		self.m_SceneInstances = m_SceneInstances
		self.hasStartedInitialization = hasStartedInitialization


class AddressablesPlatform:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AssetLabelReference:

    offsets = {'m_LabelString': 16}    
    def __init__(self, m_LabelString: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_LabelString = m_LabelString


class AssetReference:

    offsets = {'m_AssetGUID': 16, 'm_SubObjectName': 24, 'm_SubObjectType': 32, 'm_Operation': 40}    
    def __init__(self, m_AssetGUID: System.String, m_SubObjectName: System.String, m_SubObjectType: System.String, m_Operation: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_AssetGUID = m_AssetGUID
		self.m_SubObjectName = m_SubObjectName
		self.m_SubObjectType = m_SubObjectType
		self.m_Operation = m_Operation


class AssetReferenceAtlasedSprite:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AssetReferenceGameObject:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AssetReferenceSprite:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AssetReferenceT<TObject>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AssetReferenceTexture:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AssetReferenceTexture2D:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AssetReferenceTexture3D:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CheckCatalogsOperation:

    offsets = {'m_Addressables': 128, 'm_LocalHashes': 136, 'm_LocatorInfos': 144, 'm_DepOp': 152}    
    def __init__(self, m_Addressables: UnityEngine.AddressableAssets.AddressablesImpl, m_LocalHashes: System.Collections.Generic.List<System.String>, m_LocatorInfos: System.Collections.Generic.List<UnityEngine.AddressableAssets.AddressablesImpl.ResourceLocatorInfo>, m_DepOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<System.Collections.Generic.IList<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Addressables = m_Addressables
		self.m_LocalHashes = m_LocalHashes
		self.m_LocatorInfos = m_LocatorInfos
		self.m_DepOp = m_DepOp


class DynamicResourceLocator:

    offsets = {'m_Addressables': 16}    
    def __init__(self, m_Addressables: UnityEngine.AddressableAssets.AddressablesImpl, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Addressables = m_Addressables


class IKeyEvaluator:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class InvalidKeyException:

    offsets = {'<Key>k__BackingField': 136, '<Type>k__BackingField': 144}    
    def __init__(self, <Key>k__BackingField: System.Object, <Type>k__BackingField: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.<Key>k__BackingField = <Key>k__BackingField
		self.<Type>k__BackingField = <Type>k__BackingField


class PlatformMappingService:
	s_RuntimeTargetMapping: System.Collections.Generic.Dictionary<UnityEngine.RuntimePlatform,UnityEngine.AddressableAssets.AddressablesPlatform>
    offsets = {'s_RuntimeTargetMapping': 0}    
    def __init__(self, s_RuntimeTargetMapping: System.Collections.Generic.Dictionary<UnityEngine.RuntimePlatform,UnityEngine.AddressableAssets.AddressablesPlatform>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_RuntimeTargetMapping = s_RuntimeTargetMapping


class UpdateCatalogsOperation:

    offsets = {'m_Addressables': 128, 'm_LocatorInfos': 136, 'm_DepOp': 144}    
    def __init__(self, m_Addressables: UnityEngine.AddressableAssets.AddressablesImpl, m_LocatorInfos: System.Collections.Generic.List<UnityEngine.AddressableAssets.AddressablesImpl.ResourceLocatorInfo>, m_DepOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<System.Collections.Generic.IList<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Addressables = m_Addressables
		self.m_LocatorInfos = m_LocatorInfos
		self.m_DepOp = m_DepOp


class AddressablesRuntimeProperties:
	s_CachedValues: System.Collections.Generic.Dictionary<System.String,System.String>
    offsets = {'s_CachedValues': 0}    
    def __init__(self, s_CachedValues: System.Collections.Generic.Dictionary<System.String,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_CachedValues = s_CachedValues


class CacheInitialization:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CacheInitializationData:

    offsets = {'m_CompressionEnabled': 16, 'm_CacheDirectoryOverride': 24, 'm_ExpirationDelay': 32, 'm_LimitCacheSize': 36, 'm_MaximumCacheSize': 40}    
    def __init__(self, m_CompressionEnabled: System.Boolean, m_CacheDirectoryOverride: System.String, m_ExpirationDelay: System.Int32, m_LimitCacheSize: System.Boolean, m_MaximumCacheSize: System.Int64, **kwargs):
        super().__init__(self, **kwargs)
		self.m_CompressionEnabled = m_CompressionEnabled
		self.m_CacheDirectoryOverride = m_CacheDirectoryOverride
		self.m_ExpirationDelay = m_ExpirationDelay
		self.m_LimitCacheSize = m_LimitCacheSize
		self.m_MaximumCacheSize = m_MaximumCacheSize


class InitializationOperation:

    offsets = {'m_rtdOp': 128, 'm_ProviderSuffix': 152, 'm_Addressables': 160, 'm_Diagnostics': 168, 'm_InitGroupOps': 176}    
    def __init__(self, m_rtdOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<UnityEngine.AddressableAssets.Initialization.ResourceManagerRuntimeData>, m_ProviderSuffix: System.String, m_Addressables: UnityEngine.AddressableAssets.AddressablesImpl, m_Diagnostics: UnityEngine.AddressableAssets.Utility.ResourceManagerDiagnostics, m_InitGroupOps: UnityEngine.ResourceManagement.AsyncOperations.InitalizationObjectsOperation, **kwargs):
        super().__init__(self, **kwargs)
		self.m_rtdOp = m_rtdOp
		self.m_ProviderSuffix = m_ProviderSuffix
		self.m_Addressables = m_Addressables
		self.m_Diagnostics = m_Diagnostics
		self.m_InitGroupOps = m_InitGroupOps


class ResourceManagerRuntimeData:

    offsets = {'m_buildTarget': 16, 'm_SettingsHash': 24, 'm_CatalogLocations': 32, 'm_ProfileEvents': 40, 'm_LogResourceManagerExceptions': 41, 'm_ExtraInitializationData': 48, 'm_DisableCatalogUpdateOnStart': 56, 'm_IsLocalCatalogInBundle': 57, 'm_CertificateHandlerType': 64, 'm_AddressablesVersion': 96, 'm_maxConcurrentWebRequests': 104}    
    def __init__(self, m_buildTarget: System.String, m_SettingsHash: System.String, m_CatalogLocations: System.Collections.Generic.List<UnityEngine.AddressableAssets.ResourceLocators.ResourceLocationData>, m_ProfileEvents: System.Boolean, m_LogResourceManagerExceptions: System.Boolean, m_ExtraInitializationData: System.Collections.Generic.List<UnityEngine.ResourceManagement.Util.ObjectInitializationData>, m_DisableCatalogUpdateOnStart: System.Boolean, m_IsLocalCatalogInBundle: System.Boolean, m_CertificateHandlerType: UnityEngine.ResourceManagement.Util.SerializedType, m_AddressablesVersion: System.String, m_maxConcurrentWebRequests: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_buildTarget = m_buildTarget
		self.m_SettingsHash = m_SettingsHash
		self.m_CatalogLocations = m_CatalogLocations
		self.m_ProfileEvents = m_ProfileEvents
		self.m_LogResourceManagerExceptions = m_LogResourceManagerExceptions
		self.m_ExtraInitializationData = m_ExtraInitializationData
		self.m_DisableCatalogUpdateOnStart = m_DisableCatalogUpdateOnStart
		self.m_IsLocalCatalogInBundle = m_IsLocalCatalogInBundle
		self.m_CertificateHandlerType = m_CertificateHandlerType
		self.m_AddressablesVersion = m_AddressablesVersion
		self.m_maxConcurrentWebRequests = m_maxConcurrentWebRequests


class ContentCatalogData:

    offsets = {'localHash': 16, 'location': 24, 'm_LocatorId': 32, 'm_InstanceProviderData': 40, 'm_SceneProviderData': 88, 'm_ResourceProviderData': 136, 'm_KeyDataString': 160, 'm_BucketDataString': 168, 'm_EntryDataString': 176, 'm_ExtraDataString': 184}    
    def __init__(self, localHash: System.String, location: UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation, m_LocatorId: System.String, m_InstanceProviderData: UnityEngine.ResourceManagement.Util.ObjectInitializationData, m_SceneProviderData: UnityEngine.ResourceManagement.Util.ObjectInitializationData, m_ResourceProviderData: System.Collections.Generic.List<UnityEngine.ResourceManagement.Util.ObjectInitializationData>, m_KeyDataString: System.String, m_BucketDataString: System.String, m_EntryDataString: System.String, m_ExtraDataString: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.localHash = localHash
		self.location = location
		self.m_LocatorId = m_LocatorId
		self.m_InstanceProviderData = m_InstanceProviderData
		self.m_SceneProviderData = m_SceneProviderData
		self.m_ResourceProviderData = m_ResourceProviderData
		self.m_KeyDataString = m_KeyDataString
		self.m_BucketDataString = m_BucketDataString
		self.m_EntryDataString = m_EntryDataString
		self.m_ExtraDataString = m_ExtraDataString


class ContentCatalogDataEntry:

    offsets = {'<InternalId>k__BackingField': 16, '<Provider>k__BackingField': 24, '<Keys>k__BackingField': 32, '<Dependencies>k__BackingField': 40, '<Data>k__BackingField': 48, '<ResourceType>k__BackingField': 56}    
    def __init__(self, <InternalId>k__BackingField: System.String, <Provider>k__BackingField: System.String, <Keys>k__BackingField: System.Collections.Generic.List<System.Object>, <Dependencies>k__BackingField: System.Collections.Generic.List<System.Object>, <Data>k__BackingField: System.Object, <ResourceType>k__BackingField: System.Type, **kwargs):
        super().__init__(self, **kwargs)
		self.<InternalId>k__BackingField = <InternalId>k__BackingField
		self.<Provider>k__BackingField = <Provider>k__BackingField
		self.<Keys>k__BackingField = <Keys>k__BackingField
		self.<Dependencies>k__BackingField = <Dependencies>k__BackingField
		self.<Data>k__BackingField = <Data>k__BackingField
		self.<ResourceType>k__BackingField = <ResourceType>k__BackingField


class IResourceLocator:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LegacyResourcesLocator:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ResourceLocationData:

    offsets = {'m_InternalId': 24, 'm_Provider': 32, 'm_ResourceType': 48}    
    def __init__(self, m_InternalId: System.String, m_Provider: System.String, m_ResourceType: UnityEngine.ResourceManagement.Util.SerializedType, **kwargs):
        super().__init__(self, **kwargs)
		self.m_InternalId = m_InternalId
		self.m_Provider = m_Provider
		self.m_ResourceType = m_ResourceType


class ResourceLocationMap:

    offsets = {'<LocatorId>k__BackingField': 16, '<Locations>k__BackingField': 24}    
    def __init__(self, <LocatorId>k__BackingField: System.String, <Locations>k__BackingField: System.Collections.Generic.Dictionary<System.Object,System.Collections.Generic.IList<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation>>, **kwargs):
        super().__init__(self, **kwargs)
		self.<LocatorId>k__BackingField = <LocatorId>k__BackingField
		self.<Locations>k__BackingField = <Locations>k__BackingField


class ContentCatalogProvider:

    offsets = {'DisableCatalogUpdateOnStart': 32, 'IsLocalCatalogInBundle': 33, 'm_LocationToCatalogLoadOpMap': 40, 'm_RM': 48}    
    def __init__(self, DisableCatalogUpdateOnStart: System.Boolean, IsLocalCatalogInBundle: System.Boolean, m_LocationToCatalogLoadOpMap: System.Collections.Generic.Dictionary<UnityEngine.ResourceManagement.ResourceLocations.IResourceLocation,UnityEngine.AddressableAssets.ResourceProviders.ContentCatalogProvider.InternalOp>, m_RM: UnityEngine.ResourceManagement.ResourceManager, **kwargs):
        super().__init__(self, **kwargs)
		self.DisableCatalogUpdateOnStart = DisableCatalogUpdateOnStart
		self.IsLocalCatalogInBundle = IsLocalCatalogInBundle
		self.m_LocationToCatalogLoadOpMap = m_LocationToCatalogLoadOpMap
		self.m_RM = m_RM


class DiagnosticInfo:

    offsets = {'DisplayName': 16, 'ObjectId': 24}    
    def __init__(self, DisplayName: System.String, ObjectId: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.DisplayName = DisplayName
		self.ObjectId = ObjectId


class ResourceManagerDiagnostics:

    offsets = {'m_ResourceManager': 16, 'm_cachedDiagnosticInfo': 24}    
    def __init__(self, m_ResourceManager: UnityEngine.ResourceManagement.ResourceManager, m_cachedDiagnosticInfo: System.Collections.Generic.Dictionary<System.Int32,UnityEngine.AddressableAssets.Utility.DiagnosticInfo>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ResourceManager = m_ResourceManager
		self.m_cachedDiagnosticInfo = m_cachedDiagnosticInfo


class SerializationUtilities:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class InitalizationObjectsOperation:

    offsets = {'m_RtdOp': 128, 'm_Addressables': 152, 'm_DepOp': 160}    
    def __init__(self, m_RtdOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<UnityEngine.AddressableAssets.Initialization.ResourceManagerRuntimeData>, m_Addressables: UnityEngine.AddressableAssets.AddressablesImpl, m_DepOp: UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<System.Collections.Generic.IList<UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle>>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_RtdOp = m_RtdOp
		self.m_Addressables = m_Addressables
		self.m_DepOp = m_DepOp