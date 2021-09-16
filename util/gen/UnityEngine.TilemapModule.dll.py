


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ColliderType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ITilemap:
	s_Instance: UnityEngine.Tilemaps.ITilemap
    offsets = {'s_Instance': 0, 'm_Tilemap': 16}    
    def __init__(self, s_Instance: UnityEngine.Tilemaps.ITilemap, m_Tilemap: UnityEngine.Tilemaps.Tilemap, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Instance = s_Instance
		self.m_Tilemap = m_Tilemap


class Tile:

    offsets = {'m_Sprite': 24, 'm_Color': 32, 'm_Transform': 48, 'm_InstancedGameObject': 112, 'm_Flags': 120, 'm_ColliderType': 124}    
    def __init__(self, m_Sprite: UnityEngine.Sprite, m_Color: UnityEngine.Color, m_Transform: UnityEngine.Matrix4x4, m_InstancedGameObject: UnityEngine.GameObject, m_Flags: UnityEngine.Tilemaps.TileFlags, m_ColliderType: UnityEngine.Tilemaps.Tile.ColliderType, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Sprite = m_Sprite
		self.m_Color = m_Color
		self.m_Transform = m_Transform
		self.m_InstancedGameObject = m_InstancedGameObject
		self.m_Flags = m_Flags
		self.m_ColliderType = m_ColliderType


class TileAnimationData:

    offsets = {'m_AnimationSpeed': 24, 'm_AnimationStartTime': 28}    
    def __init__(self, m_AnimationSpeed: System.Single, m_AnimationStartTime: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_AnimationSpeed = m_AnimationSpeed
		self.m_AnimationStartTime = m_AnimationStartTime


class TileBase:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TileData:

    offsets = {'m_Sprite': 16, 'm_Color': 24, 'm_Transform': 40, 'm_GameObject': 104, 'm_Flags': 112, 'm_ColliderType': 116}    
    def __init__(self, m_Sprite: UnityEngine.Sprite, m_Color: UnityEngine.Color, m_Transform: UnityEngine.Matrix4x4, m_GameObject: UnityEngine.GameObject, m_Flags: UnityEngine.Tilemaps.TileFlags, m_ColliderType: UnityEngine.Tilemaps.Tile.ColliderType, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Sprite = m_Sprite
		self.m_Color = m_Color
		self.m_Transform = m_Transform
		self.m_GameObject = m_GameObject
		self.m_Flags = m_Flags
		self.m_ColliderType = m_ColliderType


class TileFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Tilemap:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TilemapRenderer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
