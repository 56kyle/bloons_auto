


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class OnNavMeshPreUpdate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NavMesh:
	onPreUpdate: UnityEngine.AI.NavMesh.OnNavMeshPreUpdate
    offsets = {'onPreUpdate': 0}    
    def __init__(self, onPreUpdate: UnityEngine.AI.NavMesh.OnNavMeshPreUpdate, **kwargs):
        super().__init__(self, **kwargs)
		self.onPreUpdate = onPreUpdate