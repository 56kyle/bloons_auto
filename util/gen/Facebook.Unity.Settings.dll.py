


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c:
	<>9: Facebook.Unity.Settings.FacebookSettings.<>c
    offsets = {'<>9': 0, '<>9__76_0': 8}    
    def __init__(self, <>9: Facebook.Unity.Settings.FacebookSettings.<>c, <>9__76_0: System.Action<Facebook.Unity.Settings.FacebookSettings.OnChangeCallback>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__76_0 = <>9__76_0


class OnChangeCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UrlSchemes:

    offsets = {'list': 16}    
    def __init__(self, list: System.Collections.Generic.List<System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.list = list


class FacebookSettings:
	onChangeCallbacks: System.Collections.Generic.List<Facebook.Unity.Settings.FacebookSettings.OnChangeCallback>
    offsets = {'onChangeCallbacks': 0, 'instance': 8, 'selectedAppIndex': 24, 'clientTokens': 32, 'appIds': 40, 'appLabels': 48, 'cookie': 56, 'logging': 57, 'status': 58, 'xfbml': 59, 'frictionlessRequests': 60, 'iosURLSuffix': 64, 'appLinkSchemes': 72, 'uploadAccessToken': 80, 'autoLogAppEventsEnabled': 88, 'advertiserIDCollectionEnabled': 89}    
    def __init__(self, onChangeCallbacks: System.Collections.Generic.List<Facebook.Unity.Settings.FacebookSettings.OnChangeCallback>, instance: Facebook.Unity.Settings.FacebookSettings, selectedAppIndex: System.Int32, clientTokens: System.Collections.Generic.List<System.String>, appIds: System.Collections.Generic.List<System.String>, appLabels: System.Collections.Generic.List<System.String>, cookie: System.Boolean, logging: System.Boolean, status: System.Boolean, xfbml: System.Boolean, frictionlessRequests: System.Boolean, iosURLSuffix: System.String, appLinkSchemes: System.Collections.Generic.List<Facebook.Unity.Settings.FacebookSettings.UrlSchemes>, uploadAccessToken: System.String, autoLogAppEventsEnabled: System.Boolean, advertiserIDCollectionEnabled: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.onChangeCallbacks = onChangeCallbacks
		self.instance = instance
		self.selectedAppIndex = selectedAppIndex
		self.clientTokens = clientTokens
		self.appIds = appIds
		self.appLabels = appLabels
		self.cookie = cookie
		self.logging = logging
		self.status = status
		self.xfbml = xfbml
		self.frictionlessRequests = frictionlessRequests
		self.iosURLSuffix = iosURLSuffix
		self.appLinkSchemes = appLinkSchemes
		self.uploadAccessToken = uploadAccessToken
		self.autoLogAppEventsEnabled = autoLogAppEventsEnabled
		self.advertiserIDCollectionEnabled = advertiserIDCollectionEnabled