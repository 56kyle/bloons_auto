


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ErrorEventHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EventHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FrameReadyEventHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TimeEventHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VideoClipPlayable:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class Video3DLayout:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VideoAspectRatio:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VideoAudioOutputMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VideoClip:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VideoPlayer:

    offsets = {'prepareCompleted': 24, 'loopPointReached': 32, 'started': 40, 'frameDropped': 48, 'errorReceived': 56, 'seekCompleted': 64, 'clockResyncOccurred': 72, 'frameReady': 80}    
    def __init__(self, prepareCompleted: UnityEngine.Video.VideoPlayer.EventHandler, loopPointReached: UnityEngine.Video.VideoPlayer.EventHandler, started: UnityEngine.Video.VideoPlayer.EventHandler, frameDropped: UnityEngine.Video.VideoPlayer.EventHandler, errorReceived: UnityEngine.Video.VideoPlayer.ErrorEventHandler, seekCompleted: UnityEngine.Video.VideoPlayer.EventHandler, clockResyncOccurred: UnityEngine.Video.VideoPlayer.TimeEventHandler, frameReady: UnityEngine.Video.VideoPlayer.FrameReadyEventHandler, **kwargs):
        super().__init__(self, **kwargs)
		self.prepareCompleted = prepareCompleted
		self.loopPointReached = loopPointReached
		self.started = started
		self.frameDropped = frameDropped
		self.errorReceived = errorReceived
		self.seekCompleted = seekCompleted
		self.clockResyncOccurred = clockResyncOccurred
		self.frameReady = frameReady


class VideoRenderMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VideoSource:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VideoTimeReference:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VideoTimeSource:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__