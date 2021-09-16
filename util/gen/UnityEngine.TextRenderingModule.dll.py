


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FontTextureRebuildCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CharacterInfo:

    offsets = {'index': 16, 'uv': 20, 'vert': 36, 'width': 52, 'size': 56, 'style': 60, 'flipped': 64}    
    def __init__(self, index: System.Int32, uv: UnityEngine.Rect, vert: UnityEngine.Rect, width: System.Single, size: System.Int32, style: UnityEngine.FontStyle, flipped: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.index = index
		self.uv = uv
		self.vert = vert
		self.width = width
		self.size = size
		self.style = style
		self.flipped = flipped


class Font:
	textureRebuilt: System.Action<UnityEngine.Font>
    offsets = {'textureRebuilt': 0, 'm_FontTextureRebuildCallback': 24}    
    def __init__(self, textureRebuilt: System.Action<UnityEngine.Font>, m_FontTextureRebuildCallback: UnityEngine.Font.FontTextureRebuildCallback, **kwargs):
        super().__init__(self, **kwargs)
		self.textureRebuilt = textureRebuilt
		self.m_FontTextureRebuildCallback = m_FontTextureRebuildCallback


class FontStyle:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class HorizontalWrapMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TextAnchor:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TextGenerationError:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TextGenerationSettings:

    offsets = {'font': 16, 'color': 24, 'fontSize': 40, 'lineSpacing': 44, 'richText': 48, 'scaleFactor': 52, 'fontStyle': 56, 'textAnchor': 60, 'alignByGeometry': 64, 'resizeTextForBestFit': 65, 'resizeTextMinSize': 68, 'resizeTextMaxSize': 72, 'updateBounds': 76, 'verticalOverflow': 80, 'horizontalOverflow': 84, 'generationExtents': 88, 'pivot': 96, 'generateOutOfBounds': 104}    
    def __init__(self, font: UnityEngine.Font, color: UnityEngine.Color, fontSize: System.Int32, lineSpacing: System.Single, richText: System.Boolean, scaleFactor: System.Single, fontStyle: UnityEngine.FontStyle, textAnchor: UnityEngine.TextAnchor, alignByGeometry: System.Boolean, resizeTextForBestFit: System.Boolean, resizeTextMinSize: System.Int32, resizeTextMaxSize: System.Int32, updateBounds: System.Boolean, verticalOverflow: UnityEngine.VerticalWrapMode, horizontalOverflow: UnityEngine.HorizontalWrapMode, generationExtents: UnityEngine.Vector2, pivot: UnityEngine.Vector2, generateOutOfBounds: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.font = font
		self.color = color
		self.fontSize = fontSize
		self.lineSpacing = lineSpacing
		self.richText = richText
		self.scaleFactor = scaleFactor
		self.fontStyle = fontStyle
		self.textAnchor = textAnchor
		self.alignByGeometry = alignByGeometry
		self.resizeTextForBestFit = resizeTextForBestFit
		self.resizeTextMinSize = resizeTextMinSize
		self.resizeTextMaxSize = resizeTextMaxSize
		self.updateBounds = updateBounds
		self.verticalOverflow = verticalOverflow
		self.horizontalOverflow = horizontalOverflow
		self.generationExtents = generationExtents
		self.pivot = pivot
		self.generateOutOfBounds = generateOutOfBounds


class TextGenerator:

    offsets = {'m_Ptr': 16, 'm_LastString': 24, 'm_LastSettings': 32, 'm_HasGenerated': 128, 'm_LastValid': 132, 'm_Verts': 136, 'm_Characters': 144, 'm_Lines': 152, 'm_CachedVerts': 160, 'm_CachedCharacters': 161, 'm_CachedLines': 162}    
    def __init__(self, m_Ptr: System.IntPtr, m_LastString: System.String, m_LastSettings: UnityEngine.TextGenerationSettings, m_HasGenerated: System.Boolean, m_LastValid: UnityEngine.TextGenerationError, m_Verts: System.Collections.Generic.List<UnityEngine.UIVertex>, m_Characters: System.Collections.Generic.List<UnityEngine.UICharInfo>, m_Lines: System.Collections.Generic.List<UnityEngine.UILineInfo>, m_CachedVerts: System.Boolean, m_CachedCharacters: System.Boolean, m_CachedLines: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_LastString = m_LastString
		self.m_LastSettings = m_LastSettings
		self.m_HasGenerated = m_HasGenerated
		self.m_LastValid = m_LastValid
		self.m_Verts = m_Verts
		self.m_Characters = m_Characters
		self.m_Lines = m_Lines
		self.m_CachedVerts = m_CachedVerts
		self.m_CachedCharacters = m_CachedCharacters
		self.m_CachedLines = m_CachedLines


class UICharInfo:

    offsets = {'cursorPos': 16, 'charWidth': 24}    
    def __init__(self, cursorPos: UnityEngine.Vector2, charWidth: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.cursorPos = cursorPos
		self.charWidth = charWidth


class UILineInfo:

    offsets = {'startCharIdx': 16, 'height': 20, 'topY': 24, 'leading': 28}    
    def __init__(self, startCharIdx: System.Int32, height: System.Int32, topY: System.Single, leading: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.startCharIdx = startCharIdx
		self.height = height
		self.topY = topY
		self.leading = leading


class UIVertex:
	s_DefaultColor: UnityEngine.Color32
    offsets = {'s_DefaultColor': 0, 's_DefaultTangent': 4, 'simpleVert': 20, 'position': 16, 'normal': 28, 'tangent': 40, 'color': 56, 'uv0': 60, 'uv1': 68, 'uv2': 76, 'uv3': 84}    
    def __init__(self, s_DefaultColor: UnityEngine.Color32, s_DefaultTangent: UnityEngine.Vector4, simpleVert: UnityEngine.UIVertex, position: UnityEngine.Vector3, normal: UnityEngine.Vector3, tangent: UnityEngine.Vector4, color: UnityEngine.Color32, uv0: UnityEngine.Vector2, uv1: UnityEngine.Vector2, uv2: UnityEngine.Vector2, uv3: UnityEngine.Vector2, **kwargs):
        super().__init__(self, **kwargs)
		self.s_DefaultColor = s_DefaultColor
		self.s_DefaultTangent = s_DefaultTangent
		self.simpleVert = simpleVert
		self.position = position
		self.normal = normal
		self.tangent = tangent
		self.color = color
		self.uv0 = uv0
		self.uv1 = uv1
		self.uv2 = uv2
		self.uv3 = uv3


class VerticalWrapMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__