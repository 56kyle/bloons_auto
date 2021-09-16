


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IdentityTokenChanged:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SessionStateChanged:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Tag:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class UpdatedEventHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RemoteConfigSettings:

    offsets = {'m_Ptr': 16, 'Updated': 24}    
    def __init__(self, m_Ptr: System.IntPtr, Updated: System.Action<System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.Updated = Updated


class RemoteConfigSettingsHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RemoteSettings:
	Updated: UnityEngine.RemoteSettings.UpdatedEventHandler
    offsets = {'Updated': 0, 'BeforeFetchFromServer': 8, 'Completed': 16}    
    def __init__(self, Updated: UnityEngine.RemoteSettings.UpdatedEventHandler, BeforeFetchFromServer: System.Action, Completed: System.Action<System.Boolean,System.Boolean,System.Int32>, **kwargs):
        super().__init__(self, **kwargs)
		self.Updated = Updated
		self.BeforeFetchFromServer = BeforeFetchFromServer
		self.Completed = Completed


class Analytics:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AnalyticsResult:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AnalyticsSessionInfo:
	sessionStateChanged: UnityEngine.Analytics.AnalyticsSessionInfo.SessionStateChanged
    offsets = {'sessionStateChanged': 0, 'identityTokenChanged': 8}    
    def __init__(self, sessionStateChanged: UnityEngine.Analytics.AnalyticsSessionInfo.SessionStateChanged, identityTokenChanged: UnityEngine.Analytics.AnalyticsSessionInfo.IdentityTokenChanged, **kwargs):
        super().__init__(self, **kwargs)
		self.sessionStateChanged = sessionStateChanged
		self.identityTokenChanged = identityTokenChanged


class AnalyticsSessionState:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ContinuousEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CustomEventData:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr