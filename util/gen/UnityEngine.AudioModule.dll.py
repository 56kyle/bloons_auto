


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PCMReaderCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PCMSetPositionCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioConfigurationChangeHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SampleFramesHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioBehaviour:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioClip:

    offsets = {'m_PCMReaderCallback': 24, 'm_PCMSetPositionCallback': 32}    
    def __init__(self, m_PCMReaderCallback: UnityEngine.AudioClip.PCMReaderCallback, m_PCMSetPositionCallback: UnityEngine.AudioClip.PCMSetPositionCallback, **kwargs):
        super().__init__(self, **kwargs)
		self.m_PCMReaderCallback = m_PCMReaderCallback
		self.m_PCMSetPositionCallback = m_PCMSetPositionCallback


class AudioClipLoadType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AudioDataLoadState:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AudioListener:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioRolloffMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AudioSettings:
	OnAudioConfigurationChanged: UnityEngine.AudioSettings.AudioConfigurationChangeHandler
    offsets = {'OnAudioConfigurationChanged': 0}    
    def __init__(self, OnAudioConfigurationChanged: UnityEngine.AudioSettings.AudioConfigurationChangeHandler, **kwargs):
        super().__init__(self, **kwargs)
		self.OnAudioConfigurationChanged = OnAudioConfigurationChanged


class AudioSource:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioSourceCurveType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AudioVelocityUpdateMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class FFTWindow:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AudioClipPlayable:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class AudioMixer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioMixerGroup:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioMixerPlayable:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class AudioMixerSnapshot:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AudioMixerUpdateMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AudioPlayableOutput:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableOutputHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class AudioSampleProvider:

    offsets = {'sampleFramesAvailable': 16, 'sampleFramesOverflow': 24}    
    def __init__(self, sampleFramesAvailable: UnityEngine.Experimental.Audio.AudioSampleProvider.SampleFramesHandler, sampleFramesOverflow: UnityEngine.Experimental.Audio.AudioSampleProvider.SampleFramesHandler, **kwargs):
        super().__init__(self, **kwargs)
		self.sampleFramesAvailable = sampleFramesAvailable
		self.sampleFramesOverflow = sampleFramesOverflow