


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class HeightmapChangedCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TextureChangedCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c__DisplayClass4_0:

    offsets = {'onlyAutoConnectedTerrains': 16}    
    def __init__(self, onlyAutoConnectedTerrains: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.onlyAutoConnectedTerrains = onlyAutoConnectedTerrains


class <>c__DisplayClass4_1:

    offsets = {'t': 16, 'CS$<>8__locals1': 24}    
    def __init__(self, t: UnityEngine.Terrain, CS$<>8__locals1: UnityEngine.Experimental.TerrainAPI.TerrainUtility.<>c__DisplayClass4_0, **kwargs):
        super().__init__(self, **kwargs)
		self.t = t
		self.CS$<>8__locals1 = CS$<>8__locals1


class TerrainGroups:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TerrainMap:

    offsets = {'m_patchSize': 16, 'm_errorCode': 28, 'm_terrainTiles': 32}    
    def __init__(self, m_patchSize: UnityEngine.Vector3, m_errorCode: UnityEngine.Experimental.TerrainAPI.TerrainUtility.TerrainMap.ErrorCode, m_terrainTiles: System.Collections.Generic.Dictionary<UnityEngine.Experimental.TerrainAPI.TerrainUtility.TerrainMap.TileCoord,UnityEngine.Terrain>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_patchSize = m_patchSize
		self.m_errorCode = m_errorCode
		self.m_terrainTiles = m_terrainTiles


class <>c__DisplayClass4_0:

    offsets = {'groupID': 16}    
    def __init__(self, groupID: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.groupID = groupID


class ErrorCode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TerrainFilter:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TileCoord:

    offsets = {'tileX': 16, 'tileZ': 20}    
    def __init__(self, tileX: System.Int32, tileZ: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.tileX = tileX
		self.tileZ = tileZ


class BoundaryValueType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Terrain:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TerrainData:
	k_MaximumResolution: System.Int32
    offsets = {'k_MaximumResolution': 0, 'k_MinimumDetailResolutionPerPatch': 4, 'k_MaximumDetailResolutionPerPatch': 8, 'k_MaximumDetailPatchCount': 12, 'k_MaximumDetailsPerRes': 16, 'k_MinimumAlphamapResolution': 20, 'k_MaximumAlphamapResolution': 24, 'k_MinimumBaseMapResolution': 28, 'k_MaximumBaseMapResolution': 32}    
    def __init__(self, k_MaximumResolution: System.Int32, k_MinimumDetailResolutionPerPatch: System.Int32, k_MaximumDetailResolutionPerPatch: System.Int32, k_MaximumDetailPatchCount: System.Int32, k_MaximumDetailsPerRes: System.Int32, k_MinimumAlphamapResolution: System.Int32, k_MaximumAlphamapResolution: System.Int32, k_MinimumBaseMapResolution: System.Int32, k_MaximumBaseMapResolution: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.k_MaximumResolution = k_MaximumResolution
		self.k_MinimumDetailResolutionPerPatch = k_MinimumDetailResolutionPerPatch
		self.k_MaximumDetailResolutionPerPatch = k_MaximumDetailResolutionPerPatch
		self.k_MaximumDetailPatchCount = k_MaximumDetailPatchCount
		self.k_MaximumDetailsPerRes = k_MaximumDetailsPerRes
		self.k_MinimumAlphamapResolution = k_MinimumAlphamapResolution
		self.k_MaximumAlphamapResolution = k_MaximumAlphamapResolution
		self.k_MinimumBaseMapResolution = k_MinimumBaseMapResolution
		self.k_MaximumBaseMapResolution = k_MaximumBaseMapResolution


class TerrainCallbacks:
	heightmapChanged: UnityEngine.Experimental.TerrainAPI.TerrainCallbacks.HeightmapChangedCallback
    offsets = {'heightmapChanged': 0, 'textureChanged': 8}    
    def __init__(self, heightmapChanged: UnityEngine.Experimental.TerrainAPI.TerrainCallbacks.HeightmapChangedCallback, textureChanged: UnityEngine.Experimental.TerrainAPI.TerrainCallbacks.TextureChangedCallback, **kwargs):
        super().__init__(self, **kwargs)
		self.heightmapChanged = heightmapChanged
		self.textureChanged = textureChanged


class TerrainUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
