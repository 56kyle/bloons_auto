


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PlayableDirector:

    offsets = {'played': 24, 'paused': 32, 'stopped': 40}    
    def __init__(self, played: System.Action<UnityEngine.Playables.PlayableDirector>, paused: System.Action<UnityEngine.Playables.PlayableDirector>, stopped: System.Action<UnityEngine.Playables.PlayableDirector>, **kwargs):
        super().__init__(self, **kwargs)
		self.played = played
		self.paused = paused
		self.stopped = stopped