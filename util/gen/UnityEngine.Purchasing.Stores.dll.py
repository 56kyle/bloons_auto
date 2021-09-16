


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c__DisplayClass2_0:

    offsets = {'request': 16, 'errorHandler': 24, 'responseHandler': 32}    
    def __init__(self, request: UnityEngine.Networking.UnityWebRequest, errorHandler: System.Action<System.String>, responseHandler: System.Action<System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.request = request
		self.errorHandler = errorHandler
		self.responseHandler = responseHandler


class <DoInvoke>d__4:

    offsets = {'<>1__state': 16, '<>2__current': 24, 'delayInSeconds': 32, 'a': 40}    
    def __init__(self, <>1__state: System.Int32, <>2__current: System.Object, delayInSeconds: System.Int32, a: System.Action, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.delayInSeconds = delayInSeconds
		self.a = a


class <DelayedCoroutine>d__48:

    offsets = {'<>1__state': 16, '<>2__current': 24, 'delay': 32, '<>4__this': 40, 'coroutine': 48}    
    def __init__(self, <>1__state: System.Int32, <>2__current: System.Object, delay: System.Int32, <>4__this: UnityEngine.Purchasing.Extension.UnityUtil, coroutine: System.Collections.IEnumerator, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.delay = delay
		self.<>4__this = <>4__this
		self.coroutine = coroutine


class ProductCatalogPayoutType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LifecycleNotifier:

    offsets = {'OnDestroyCallback': 24}    
    def __init__(self, OnDestroyCallback: System.Action, **kwargs):
        super().__init__(self, **kwargs)
		self.OnDestroyCallback = OnDestroyCallback


class <>c__DisplayClass0_0:

    offsets = {'sku': 16}    
    def __init__(self, sku: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.sku = sku


class IUtil:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AdsIPC:
	adsAdvertisementClassName: System.String
    offsets = {'adsAdvertisementClassName': 0, 'adsMessageSendName': 8, 'adsAdvertisementType': 16, 'adsMessageSend': 24}    
    def __init__(self, adsAdvertisementClassName: System.String, adsMessageSendName: System.String, adsAdvertisementType: System.Type, adsMessageSend: System.Reflection.MethodInfo, **kwargs):
        super().__init__(self, **kwargs)
		self.adsAdvertisementClassName = adsAdvertisementClassName
		self.adsMessageSendName = adsMessageSendName
		self.adsAdvertisementType = adsAdvertisementType
		self.adsMessageSend = adsMessageSend


class AsyncWebUtil:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class BillingClientStateListener:

    offsets = {'m_OnConnected': 32, 'm_Disconnect': 40}    
    def __init__(self, m_OnConnected: System.Action, m_Disconnect: System.Action, **kwargs):
        super().__init__(self, **kwargs)
		self.m_OnConnected = m_OnConnected
		self.m_Disconnect = m_Disconnect


class EventQueue:
	QueueInstance: UnityEngine.Purchasing.EventQueue
    offsets = {'QueueInstance': 0, 'm_AsyncUtil': 16, 'Profile': 24, 'TrackingUrl': 32, 'EventUrl': 40, 'ProfileDict': 48}    
    def __init__(self, QueueInstance: UnityEngine.Purchasing.EventQueue, m_AsyncUtil: UnityEngine.Purchasing.IAsyncWebUtil, Profile: UnityEngine.Purchasing.ProfileData, TrackingUrl: System.String, EventUrl: System.String, ProfileDict: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.QueueInstance = QueueInstance
		self.m_AsyncUtil = m_AsyncUtil
		self.Profile = Profile
		self.TrackingUrl = TrackingUrl
		self.EventUrl = EventUrl
		self.ProfileDict = ProfileDict


class FakeStore:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GoogleAcknowledgePurchaseListener:

    offsets = {'m_OnAcknowledgePurchaseResponse': 32, 'm_Product': 40, 'm_Purchase': 48}    
    def __init__(self, m_OnAcknowledgePurchaseResponse: System.Action<UnityEngine.Purchasing.ProductDefinition,UnityEngine.Purchasing.Models.GooglePurchase,UnityEngine.Purchasing.Models.GoogleBillingResult>, m_Product: UnityEngine.Purchasing.ProductDefinition, m_Purchase: UnityEngine.Purchasing.Models.GooglePurchase, **kwargs):
        super().__init__(self, **kwargs)
		self.m_OnAcknowledgePurchaseResponse = m_OnAcknowledgePurchaseResponse
		self.m_Product = m_Product
		self.m_Purchase = m_Purchase


class GoogleConsumeResponseListener:

    offsets = {'m_Product': 32, 'm_Purchase': 40, 'm_OnConsumeResponse': 48}    
    def __init__(self, m_Product: UnityEngine.Purchasing.ProductDefinition, m_Purchase: UnityEngine.Purchasing.Models.GooglePurchase, m_OnConsumeResponse: System.Action<UnityEngine.Purchasing.ProductDefinition,UnityEngine.Purchasing.Models.GooglePurchase,UnityEngine.Purchasing.Models.GoogleBillingResult,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Product = m_Product
		self.m_Purchase = m_Purchase
		self.m_OnConsumeResponse = m_OnConsumeResponse


class GooglePlayProrationMode:
	k_NullProrationMode: System.Int32
    offsets = {'k_NullProrationMode': 0, 'k_UnknownProrationMode': 4, 'k_ImmediateWithoutProration': 8, 'k_DeferredProrationMode': 12}    
    def __init__(self, k_NullProrationMode: System.Int32, k_UnknownProrationMode: System.Int32, k_ImmediateWithoutProration: System.Int32, k_DeferredProrationMode: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.k_NullProrationMode = k_NullProrationMode
		self.k_UnknownProrationMode = k_UnknownProrationMode
		self.k_ImmediateWithoutProration = k_ImmediateWithoutProration
		self.k_DeferredProrationMode = k_DeferredProrationMode


class GooglePriceChangeConfirmationListener:

    offsets = {'m_OnPriceChangeConfirmationResult': 32}    
    def __init__(self, m_OnPriceChangeConfirmationResult: System.Action<UnityEngine.Purchasing.Models.GoogleBillingResult>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_OnPriceChangeConfirmationResult = m_OnPriceChangeConfirmationResult


class GooglePurchaseUpdatedListener:

    offsets = {'m_LastKnownProductService': 32, 'm_GooglePurchaseCallback': 40, 'm_GoogleCachedQuerySkuDetailsService': 48}    
    def __init__(self, m_LastKnownProductService: UnityEngine.Purchasing.Interfaces.IGoogleLastKnownProductService, m_GooglePurchaseCallback: UnityEngine.Purchasing.Interfaces.IGooglePurchaseCallback, m_GoogleCachedQuerySkuDetailsService: UnityEngine.Purchasing.IGoogleCachedQuerySkuDetailsService, **kwargs):
        super().__init__(self, **kwargs)
		self.m_LastKnownProductService = m_LastKnownProductService
		self.m_GooglePurchaseCallback = m_GooglePurchaseCallback
		self.m_GoogleCachedQuerySkuDetailsService = m_GoogleCachedQuerySkuDetailsService


class IAppleExtensions:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IAsyncWebUtil:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IGoogleCachedQuerySkuDetailsService:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IProductCatalogImpl:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class JSONSerializer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class JSONStore:

    offsets = {'unity': 16, 'store': 24, 'promoPayload': 32}    
    def __init__(self, unity: UnityEngine.Purchasing.Extension.IStoreCallback, store: UnityEngine.Purchasing.INativeStore, promoPayload: System.Collections.Generic.Dictionary<System.String,System.Object>, **kwargs):
        super().__init__(self, **kwargs)
		self.unity = unity
		self.store = store
		self.promoPayload = promoPayload


class LocalizedProductDescription:

    offsets = {'googleLocale': 16, 'title': 24, 'description': 32}    
    def __init__(self, googleLocale: UnityEngine.Purchasing.TranslationLocale, title: System.String, description: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.googleLocale = googleLocale
		self.title = title
		self.description = description


class Price:

    offsets = {'value': 16, 'num': 40}    
    def __init__(self, value: System.Decimal, num: System.Double, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.num = num


class ProductCatalog:
	instance: UnityEngine.Purchasing.IProductCatalogImpl
    offsets = {'instance': 0, 'appleSKU': 16, 'appleTeamID': 24, 'enableCodelessAutoInitialization': 32, 'products': 40}    
    def __init__(self, instance: UnityEngine.Purchasing.IProductCatalogImpl, appleSKU: System.String, appleTeamID: System.String, enableCodelessAutoInitialization: System.Boolean, products: System.Collections.Generic.List<UnityEngine.Purchasing.ProductCatalogItem>, **kwargs):
        super().__init__(self, **kwargs)
		self.instance = instance
		self.appleSKU = appleSKU
		self.appleTeamID = appleTeamID
		self.enableCodelessAutoInitialization = enableCodelessAutoInitialization
		self.products = products


class ProductCatalogImpl:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProductCatalogItem:

    offsets = {'id': 16, 'type': 24, 'storeIDs': 32, 'defaultDescription': 40, 'screenshotPath': 48, 'applePriceTier': 56, 'googlePrice': 64, 'pricingTemplateID': 72, 'descriptions': 80, 'udpPrice': 88, 'payouts': 96}    
    def __init__(self, id: System.String, type: UnityEngine.Purchasing.ProductType, storeIDs: System.Collections.Generic.List<UnityEngine.Purchasing.StoreID>, defaultDescription: UnityEngine.Purchasing.LocalizedProductDescription, screenshotPath: System.String, applePriceTier: System.Int32, googlePrice: UnityEngine.Purchasing.Price, pricingTemplateID: System.String, descriptions: System.Collections.Generic.List<UnityEngine.Purchasing.LocalizedProductDescription>, udpPrice: UnityEngine.Purchasing.Price, payouts: System.Collections.Generic.List<UnityEngine.Purchasing.ProductCatalogPayout>, **kwargs):
        super().__init__(self, **kwargs)
		self.id = id
		self.type = type
		self.storeIDs = storeIDs
		self.defaultDescription = defaultDescription
		self.screenshotPath = screenshotPath
		self.applePriceTier = applePriceTier
		self.googlePrice = googlePrice
		self.pricingTemplateID = pricingTemplateID
		self.descriptions = descriptions
		self.udpPrice = udpPrice
		self.payouts = payouts


class ProductCatalogPayout:

    offsets = {'t': 16, 'st': 24, 'q': 32, 'd': 40}    
    def __init__(self, t: System.String, st: System.String, q: System.Double, d: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.t = t
		self.st = st
		self.q = q
		self.d = d


class ProfileData:
	ProfileInstance: UnityEngine.Purchasing.ProfileData
    offsets = {'ProfileInstance': 0, 'm_Util': 16, '<AppId>k__BackingField': 24, '<UserId>k__BackingField': 32, '<SessionId>k__BackingField': 40, '<Platform>k__BackingField': 48, '<PlatformId>k__BackingField': 56, '<SdkVer>k__BackingField': 64, '<OsVer>k__BackingField': 72, '<ScreenWidth>k__BackingField': 80, '<ScreenHeight>k__BackingField': 84, '<ScreenDpi>k__BackingField': 88, '<ScreenOrientation>k__BackingField': 96, '<DeviceId>k__BackingField': 104, '<BuildGUID>k__BackingField': 112, '<IapVer>k__BackingField': 120, '<AdsGamerToken>k__BackingField': 128, '<TrackingOptOut>k__BackingField': 136, '<AdsABGroup>k__BackingField': 140, '<AdsGameId>k__BackingField': 152, '<StoreABGroup>k__BackingField': 160, '<CatalogId>k__BackingField': 168, '<StoreName>k__BackingField': 176, '<GameVersion>k__BackingField': 184, '<StoreTestEnabled>k__BackingField': 192}    
    def __init__(self, ProfileInstance: UnityEngine.Purchasing.ProfileData, m_Util: Uniject.IUtil, <AppId>k__BackingField: System.String, <UserId>k__BackingField: System.String, <SessionId>k__BackingField: System.UInt64, <Platform>k__BackingField: System.String, <PlatformId>k__BackingField: System.Int32, <SdkVer>k__BackingField: System.String, <OsVer>k__BackingField: System.String, <ScreenWidth>k__BackingField: System.Int32, <ScreenHeight>k__BackingField: System.Int32, <ScreenDpi>k__BackingField: System.Single, <ScreenOrientation>k__BackingField: System.String, <DeviceId>k__BackingField: System.String, <BuildGUID>k__BackingField: System.String, <IapVer>k__BackingField: System.String, <AdsGamerToken>k__BackingField: System.String, <TrackingOptOut>k__BackingField: System.Nullable<System.Boolean>, <AdsABGroup>k__BackingField: System.Nullable<System.Int32>, <AdsGameId>k__BackingField: System.String, <StoreABGroup>k__BackingField: System.Nullable<System.Int32>, <CatalogId>k__BackingField: System.String, <StoreName>k__BackingField: System.String, <GameVersion>k__BackingField: System.String, <StoreTestEnabled>k__BackingField: System.Nullable<System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.ProfileInstance = ProfileInstance
		self.m_Util = m_Util
		self.<AppId>k__BackingField = <AppId>k__BackingField
		self.<UserId>k__BackingField = <UserId>k__BackingField
		self.<SessionId>k__BackingField = <SessionId>k__BackingField
		self.<Platform>k__BackingField = <Platform>k__BackingField
		self.<PlatformId>k__BackingField = <PlatformId>k__BackingField
		self.<SdkVer>k__BackingField = <SdkVer>k__BackingField
		self.<OsVer>k__BackingField = <OsVer>k__BackingField
		self.<ScreenWidth>k__BackingField = <ScreenWidth>k__BackingField
		self.<ScreenHeight>k__BackingField = <ScreenHeight>k__BackingField
		self.<ScreenDpi>k__BackingField = <ScreenDpi>k__BackingField
		self.<ScreenOrientation>k__BackingField = <ScreenOrientation>k__BackingField
		self.<DeviceId>k__BackingField = <DeviceId>k__BackingField
		self.<BuildGUID>k__BackingField = <BuildGUID>k__BackingField
		self.<IapVer>k__BackingField = <IapVer>k__BackingField
		self.<AdsGamerToken>k__BackingField = <AdsGamerToken>k__BackingField
		self.<TrackingOptOut>k__BackingField = <TrackingOptOut>k__BackingField
		self.<AdsABGroup>k__BackingField = <AdsABGroup>k__BackingField
		self.<AdsGameId>k__BackingField = <AdsGameId>k__BackingField
		self.<StoreABGroup>k__BackingField = <StoreABGroup>k__BackingField
		self.<CatalogId>k__BackingField = <CatalogId>k__BackingField
		self.<StoreName>k__BackingField = <StoreName>k__BackingField
		self.<GameVersion>k__BackingField = <GameVersion>k__BackingField
		self.<StoreTestEnabled>k__BackingField = <StoreTestEnabled>k__BackingField


class Promo:
	s_PromoPurchaser: UnityEngine.Purchasing.JSONStore
    offsets = {'s_PromoPurchaser': 0, 's_Unity': 8, 's_Logger': 16, 's_Version': 24, 's_Util': 32, 's_WebUtil': 40, 's_IsReady': 48, 's_ProductJSON': 56}    
    def __init__(self, s_PromoPurchaser: UnityEngine.Purchasing.JSONStore, s_Unity: UnityEngine.Purchasing.Extension.IStoreCallback, s_Logger: UnityEngine.ILogger, s_Version: System.String, s_Util: Uniject.IUtil, s_WebUtil: UnityEngine.Purchasing.IAsyncWebUtil, s_IsReady: System.Boolean, s_ProductJSON: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.s_PromoPurchaser = s_PromoPurchaser
		self.s_Unity = s_Unity
		self.s_Logger = s_Logger
		self.s_Version = s_Version
		self.s_Util = s_Util
		self.s_WebUtil = s_WebUtil
		self.s_IsReady = s_IsReady
		self.s_ProductJSON = s_ProductJSON


class SkuDetailsResponseListener:

    offsets = {'m_OnSkuDetailsResponse': 32}    
    def __init__(self, m_OnSkuDetailsResponse: System.Action<UnityEngine.AndroidJavaObject,UnityEngine.AndroidJavaObject>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_OnSkuDetailsResponse = m_OnSkuDetailsResponse


class StoreID:

    offsets = {'store': 16, 'id': 24}    
    def __init__(self, store: System.String, id: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.store = store
		self.id = id


class TranslationLocale:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class UIFakeStore:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityUtil:
	s_Callbacks: System.Collections.Generic.List<System.Action>
    offsets = {'s_Callbacks': 0, 's_CallbacksPending': 8, 's_PcControlledPlatforms': 16, 'pauseListeners': 24}    
    def __init__(self, s_Callbacks: System.Collections.Generic.List<System.Action>, s_CallbacksPending: System.Boolean, s_PcControlledPlatforms: System.Collections.Generic.List<UnityEngine.RuntimePlatform>, pauseListeners: System.Collections.Generic.List<System.Action<System.Boolean>>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Callbacks = s_Callbacks
		self.s_CallbacksPending = s_CallbacksPending
		self.s_PcControlledPlatforms = s_PcControlledPlatforms
		self.pauseListeners = pauseListeners


class IGoogleLastKnownProductService:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IGooglePurchaseCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class BillingClientResponseEnum:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GoogleBillingResult:

    offsets = {'responseCode': 16, 'debugMessage': 24}    
    def __init__(self, responseCode: System.Int32, debugMessage: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.responseCode = responseCode
		self.debugMessage = debugMessage


class GooglePurchase:

    offsets = {'javaPurchase': 16, 'purchaseState': 24, 'sku': 32, 'orderId': 40, 'receipt': 48, 'signature': 56, 'originalJson': 64, 'purchaseToken': 72}    
    def __init__(self, javaPurchase: UnityEngine.AndroidJavaObject, purchaseState: System.Int32, sku: System.String, orderId: System.String, receipt: System.String, signature: System.String, originalJson: System.String, purchaseToken: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.javaPurchase = javaPurchase
		self.purchaseState = purchaseState
		self.sku = sku
		self.orderId = orderId
		self.receipt = receipt
		self.signature = signature
		self.originalJson = originalJson
		self.purchaseToken = purchaseToken


class GooglePurchaseStateEnum:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GooglePurchaseHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GoogleReceiptEncoder:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
