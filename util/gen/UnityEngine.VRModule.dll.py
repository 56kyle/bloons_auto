


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnTrackingChangedDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XRDevice:
	deviceLoaded: System.Action<System.String>
    offsets = {'deviceLoaded': 0}    
    def __init__(self, deviceLoaded: System.Action<System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.deviceLoaded = deviceLoaded


class WorldAnchor:

    offsets = {'OnTrackingChanged': 24}    
    def __init__(self, OnTrackingChanged: UnityEngine.XR.WSA.WorldAnchor.OnTrackingChangedDelegate, **kwargs):
        super().__init__(self, **kwargs)
		self.OnTrackingChanged = OnTrackingChanged