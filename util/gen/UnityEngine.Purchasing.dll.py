


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c:
	<>9: UnityEngine.Purchasing.ProductCollection.<>c
    offsets = {'<>9': 0, '<>9__5_0': 8, '<>9__5_1': 16}    
    def __init__(self, <>9: UnityEngine.Purchasing.ProductCollection.<>c, <>9__5_0: System.Func<UnityEngine.Purchasing.Product,System.String>, <>9__5_1: System.Func<UnityEngine.Purchasing.Product,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__5_0 = <>9__5_0
		self.<>9__5_1 = <>9__5_1


class <>c:
	<>9: UnityEngine.Purchasing.PurchasingManager.<>c
    offsets = {'<>9': 0, '<>9__36_0': 8}    
    def __init__(self, <>9: UnityEngine.Purchasing.PurchasingManager.<>c, <>9__36_0: System.Func<UnityEngine.Purchasing.ProductDefinition,UnityEngine.Purchasing.Product>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__36_0 = <>9__36_0


class UnifiedReceipt:

    offsets = {'Store': 16, 'TransactionID': 24, 'Payload': 32}    
    def __init__(self, Store: System.String, TransactionID: System.String, Payload: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.Store = Store
		self.TransactionID = TransactionID
		self.Payload = Payload


class <>c__DisplayClass2_0:

    offsets = {'manager': 16, 'proxy': 24}    
    def __init__(self, manager: UnityEngine.Purchasing.PurchasingManager, proxy: UnityEngine.Purchasing.StoreListenerProxy, **kwargs):
        super().__init__(self, **kwargs)
		self.manager = manager
		self.proxy = proxy


class <>c__DisplayClass3_0:

    offsets = {'localProductSet': 16, 'callback': 24}    
    def __init__(self, localProductSet: System.Collections.Generic.HashSet<UnityEngine.Purchasing.ProductDefinition>, callback: System.Action<System.Collections.Generic.HashSet<UnityEngine.Purchasing.ProductDefinition>>, **kwargs):
        super().__init__(self, **kwargs)
		self.localProductSet = localProductSet
		self.callback = callback


class AnalyticsReporter:

    offsets = {'m_Analytics': 16}    
    def __init__(self, m_Analytics: UnityEngine.Purchasing.IUnityAnalytics, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Analytics = m_Analytics


class ConfigurationBuilder:

    offsets = {'m_Factory': 16, 'm_Products': 24, '<useCatalogProvider>k__BackingField': 32}    
    def __init__(self, m_Factory: UnityEngine.Purchasing.PurchasingFactory, m_Products: System.Collections.Generic.HashSet<UnityEngine.Purchasing.ProductDefinition>, <useCatalogProvider>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Factory = m_Factory
		self.m_Products = m_Products
		self.<useCatalogProvider>k__BackingField = <useCatalogProvider>k__BackingField


class IDs:

    offsets = {'m_Dic': 16}    
    def __init__(self, m_Dic: System.Collections.Generic.Dictionary<System.String,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Dic = m_Dic


class IExtensionProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IInternalStoreListener:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IStoreController:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IStoreExtension:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IStoreListener:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IUnityAnalytics:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class InitializationFailureReason:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PayoutDefinition:

    offsets = {'m_Type': 16, 'm_Subtype': 24, 'm_Quantity': 32, 'm_Data': 40}    
    def __init__(self, m_Type: UnityEngine.Purchasing.PayoutType, m_Subtype: System.String, m_Quantity: System.Double, m_Data: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Type = m_Type
		self.m_Subtype = m_Subtype
		self.m_Quantity = m_Quantity
		self.m_Data = m_Data


class PayoutType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Product:

    offsets = {'<definition>k__BackingField': 16, '<metadata>k__BackingField': 24, '<availableToPurchase>k__BackingField': 32, '<transactionID>k__BackingField': 40, '<receipt>k__BackingField': 48}    
    def __init__(self, <definition>k__BackingField: UnityEngine.Purchasing.ProductDefinition, <metadata>k__BackingField: UnityEngine.Purchasing.ProductMetadata, <availableToPurchase>k__BackingField: System.Boolean, <transactionID>k__BackingField: System.String, <receipt>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<definition>k__BackingField = <definition>k__BackingField
		self.<metadata>k__BackingField = <metadata>k__BackingField
		self.<availableToPurchase>k__BackingField = <availableToPurchase>k__BackingField
		self.<transactionID>k__BackingField = <transactionID>k__BackingField
		self.<receipt>k__BackingField = <receipt>k__BackingField


class ProductCollection:

    offsets = {'m_IdToProduct': 16, 'm_StoreSpecificIdToProduct': 24, 'm_ProductSet': 40}    
    def __init__(self, m_IdToProduct: System.Collections.Generic.Dictionary<System.String,UnityEngine.Purchasing.Product>, m_StoreSpecificIdToProduct: System.Collections.Generic.Dictionary<System.String,UnityEngine.Purchasing.Product>, m_ProductSet: System.Collections.Generic.HashSet<UnityEngine.Purchasing.Product>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_IdToProduct = m_IdToProduct
		self.m_StoreSpecificIdToProduct = m_StoreSpecificIdToProduct
		self.m_ProductSet = m_ProductSet


class ProductDefinition:

    offsets = {'<id>k__BackingField': 16, '<storeSpecificId>k__BackingField': 24, '<type>k__BackingField': 32, '<enabled>k__BackingField': 36, 'm_Payouts': 40}    
    def __init__(self, <id>k__BackingField: System.String, <storeSpecificId>k__BackingField: System.String, <type>k__BackingField: UnityEngine.Purchasing.ProductType, <enabled>k__BackingField: System.Boolean, m_Payouts: System.Collections.Generic.List<UnityEngine.Purchasing.PayoutDefinition>, **kwargs):
        super().__init__(self, **kwargs)
		self.<id>k__BackingField = <id>k__BackingField
		self.<storeSpecificId>k__BackingField = <storeSpecificId>k__BackingField
		self.<type>k__BackingField = <type>k__BackingField
		self.<enabled>k__BackingField = <enabled>k__BackingField
		self.m_Payouts = m_Payouts


class ProductMetadata:

    offsets = {'<localizedPriceString>k__BackingField': 16, '<localizedTitle>k__BackingField': 24, '<localizedDescription>k__BackingField': 32, '<isoCurrencyCode>k__BackingField': 40, '<localizedPrice>k__BackingField': 48}    
    def __init__(self, <localizedPriceString>k__BackingField: System.String, <localizedTitle>k__BackingField: System.String, <localizedDescription>k__BackingField: System.String, <isoCurrencyCode>k__BackingField: System.String, <localizedPrice>k__BackingField: System.Decimal, **kwargs):
        super().__init__(self, **kwargs)
		self.<localizedPriceString>k__BackingField = <localizedPriceString>k__BackingField
		self.<localizedTitle>k__BackingField = <localizedTitle>k__BackingField
		self.<localizedDescription>k__BackingField = <localizedDescription>k__BackingField
		self.<isoCurrencyCode>k__BackingField = <isoCurrencyCode>k__BackingField
		self.<localizedPrice>k__BackingField = <localizedPrice>k__BackingField


class ProductType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PurchaseEventArgs:

    offsets = {'<purchasedProduct>k__BackingField': 16}    
    def __init__(self, <purchasedProduct>k__BackingField: UnityEngine.Purchasing.Product, **kwargs):
        super().__init__(self, **kwargs)
		self.<purchasedProduct>k__BackingField = <purchasedProduct>k__BackingField


class PurchaseFailureReason:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PurchaseProcessingResult:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PurchasingFactory:

    offsets = {'m_ConfigMap': 16, 'm_ExtensionMap': 24, 'm_Store': 32, 'm_CatalogProvider': 40, '<storeName>k__BackingField': 48}    
    def __init__(self, m_ConfigMap: System.Collections.Generic.Dictionary<System.Type,UnityEngine.Purchasing.Extension.IStoreConfiguration>, m_ExtensionMap: System.Collections.Generic.Dictionary<System.Type,UnityEngine.Purchasing.IStoreExtension>, m_Store: UnityEngine.Purchasing.Extension.IStore, m_CatalogProvider: UnityEngine.Purchasing.Extension.ICatalogProvider, <storeName>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ConfigMap = m_ConfigMap
		self.m_ExtensionMap = m_ExtensionMap
		self.m_Store = m_Store
		self.m_CatalogProvider = m_CatalogProvider
		self.<storeName>k__BackingField = <storeName>k__BackingField


class PurchasingManager:

    offsets = {'m_Store': 16, 'm_Listener': 24, 'm_Logger': 32, 'm_TransactionLog': 40, 'm_StoreName': 48, 'm_AdditionalProductsCallback': 56, 'm_AdditionalProductsFailCallback': 64, '<useTransactionLog>k__BackingField': 72, '<products>k__BackingField': 80, 'initialized': 88}    
    def __init__(self, m_Store: UnityEngine.Purchasing.Extension.IStore, m_Listener: UnityEngine.Purchasing.IInternalStoreListener, m_Logger: UnityEngine.ILogger, m_TransactionLog: UnityEngine.Purchasing.TransactionLog, m_StoreName: System.String, m_AdditionalProductsCallback: System.Action, m_AdditionalProductsFailCallback: System.Action<UnityEngine.Purchasing.InitializationFailureReason>, <useTransactionLog>k__BackingField: System.Boolean, <products>k__BackingField: UnityEngine.Purchasing.ProductCollection, initialized: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Store = m_Store
		self.m_Listener = m_Listener
		self.m_Logger = m_Logger
		self.m_TransactionLog = m_TransactionLog
		self.m_StoreName = m_StoreName
		self.m_AdditionalProductsCallback = m_AdditionalProductsCallback
		self.m_AdditionalProductsFailCallback = m_AdditionalProductsFailCallback
		self.<useTransactionLog>k__BackingField = <useTransactionLog>k__BackingField
		self.<products>k__BackingField = <products>k__BackingField
		self.initialized = initialized


class StoreListenerProxy:

    offsets = {'m_Analytics': 16, 'm_ForwardTo': 24, 'm_Extensions': 32}    
    def __init__(self, m_Analytics: UnityEngine.Purchasing.AnalyticsReporter, m_ForwardTo: UnityEngine.Purchasing.IStoreListener, m_Extensions: UnityEngine.Purchasing.IExtensionProvider, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Analytics = m_Analytics
		self.m_ForwardTo = m_ForwardTo
		self.m_Extensions = m_Extensions


class TransactionLog:

    offsets = {'logger': 16, 'persistentDataPath': 24}    
    def __init__(self, logger: UnityEngine.ILogger, persistentDataPath: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.logger = logger
		self.persistentDataPath = persistentDataPath


class UnityAnalytics:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityPurchasing:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AbstractPurchasingModule:

    offsets = {'m_Binder': 16}    
    def __init__(self, m_Binder: UnityEngine.Purchasing.Extension.IPurchasingBinder, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Binder = m_Binder


class AbstractStore:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ICatalogProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPurchasingBinder:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPurchasingModule:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IStore:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IStoreCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IStoreConfiguration:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProductDescription:

    offsets = {'<storeSpecificId>k__BackingField': 16, 'type': 24, '<metadata>k__BackingField': 32, '<receipt>k__BackingField': 40, '<transactionId>k__BackingField': 48}    
    def __init__(self, <storeSpecificId>k__BackingField: System.String, type: UnityEngine.Purchasing.ProductType, <metadata>k__BackingField: UnityEngine.Purchasing.ProductMetadata, <receipt>k__BackingField: System.String, <transactionId>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<storeSpecificId>k__BackingField = <storeSpecificId>k__BackingField
		self.type = type
		self.<metadata>k__BackingField = <metadata>k__BackingField
		self.<receipt>k__BackingField = <receipt>k__BackingField
		self.<transactionId>k__BackingField = <transactionId>k__BackingField


class PurchaseFailureDescription:

    offsets = {'<productId>k__BackingField': 16, '<reason>k__BackingField': 24, '<message>k__BackingField': 32}    
    def __init__(self, <productId>k__BackingField: System.String, <reason>k__BackingField: UnityEngine.Purchasing.PurchaseFailureReason, <message>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<productId>k__BackingField = <productId>k__BackingField
		self.<reason>k__BackingField = <reason>k__BackingField
		self.<message>k__BackingField = <message>k__BackingField