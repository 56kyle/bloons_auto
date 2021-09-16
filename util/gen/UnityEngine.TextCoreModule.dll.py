


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FaceInfo:

    offsets = {'m_FaceIndex': 16, 'm_FamilyName': 24, 'm_StyleName': 32, 'm_PointSize': 40, 'm_Scale': 44, 'm_LineHeight': 48, 'm_AscentLine': 52, 'm_CapLine': 56, 'm_MeanLine': 60, 'm_Baseline': 64, 'm_DescentLine': 68, 'm_SuperscriptOffset': 72, 'm_SuperscriptSize': 76, 'm_SubscriptOffset': 80, 'm_SubscriptSize': 84, 'm_UnderlineOffset': 88, 'm_UnderlineThickness': 92, 'm_StrikethroughOffset': 96, 'm_StrikethroughThickness': 100, 'm_TabWidth': 104}    
    def __init__(self, m_FaceIndex: System.Int32, m_FamilyName: System.String, m_StyleName: System.String, m_PointSize: System.Int32, m_Scale: System.Single, m_LineHeight: System.Single, m_AscentLine: System.Single, m_CapLine: System.Single, m_MeanLine: System.Single, m_Baseline: System.Single, m_DescentLine: System.Single, m_SuperscriptOffset: System.Single, m_SuperscriptSize: System.Single, m_SubscriptOffset: System.Single, m_SubscriptSize: System.Single, m_UnderlineOffset: System.Single, m_UnderlineThickness: System.Single, m_StrikethroughOffset: System.Single, m_StrikethroughThickness: System.Single, m_TabWidth: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_FaceIndex = m_FaceIndex
		self.m_FamilyName = m_FamilyName
		self.m_StyleName = m_StyleName
		self.m_PointSize = m_PointSize
		self.m_Scale = m_Scale
		self.m_LineHeight = m_LineHeight
		self.m_AscentLine = m_AscentLine
		self.m_CapLine = m_CapLine
		self.m_MeanLine = m_MeanLine
		self.m_Baseline = m_Baseline
		self.m_DescentLine = m_DescentLine
		self.m_SuperscriptOffset = m_SuperscriptOffset
		self.m_SuperscriptSize = m_SuperscriptSize
		self.m_SubscriptOffset = m_SubscriptOffset
		self.m_SubscriptSize = m_SubscriptSize
		self.m_UnderlineOffset = m_UnderlineOffset
		self.m_UnderlineThickness = m_UnderlineThickness
		self.m_StrikethroughOffset = m_StrikethroughOffset
		self.m_StrikethroughThickness = m_StrikethroughThickness
		self.m_TabWidth = m_TabWidth


class Glyph:

    offsets = {'m_Index': 16, 'm_Metrics': 20, 'm_GlyphRect': 40, 'm_Scale': 56, 'm_AtlasIndex': 60}    
    def __init__(self, m_Index: System.UInt32, m_Metrics: UnityEngine.TextCore.GlyphMetrics, m_GlyphRect: UnityEngine.TextCore.GlyphRect, m_Scale: System.Single, m_AtlasIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Index = m_Index
		self.m_Metrics = m_Metrics
		self.m_GlyphRect = m_GlyphRect
		self.m_Scale = m_Scale
		self.m_AtlasIndex = m_AtlasIndex


class GlyphMetrics:

    offsets = {'m_Width': 16, 'm_Height': 20, 'm_HorizontalBearingX': 24, 'm_HorizontalBearingY': 28, 'm_HorizontalAdvance': 32}    
    def __init__(self, m_Width: System.Single, m_Height: System.Single, m_HorizontalBearingX: System.Single, m_HorizontalBearingY: System.Single, m_HorizontalAdvance: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Width = m_Width
		self.m_Height = m_Height
		self.m_HorizontalBearingX = m_HorizontalBearingX
		self.m_HorizontalBearingY = m_HorizontalBearingY
		self.m_HorizontalAdvance = m_HorizontalAdvance


class GlyphRect:
	s_ZeroGlyphRect: UnityEngine.TextCore.GlyphRect
    offsets = {'s_ZeroGlyphRect': 0, 'm_X': 16, 'm_Y': 20, 'm_Width': 24, 'm_Height': 28}    
    def __init__(self, s_ZeroGlyphRect: UnityEngine.TextCore.GlyphRect, m_X: System.Int32, m_Y: System.Int32, m_Width: System.Int32, m_Height: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.s_ZeroGlyphRect = s_ZeroGlyphRect
		self.m_X = m_X
		self.m_Y = m_Y
		self.m_Width = m_Width
		self.m_Height = m_Height


class FontEngine:

    offsets = {'s_GlyphLookupDictionary': 64}    
    def __init__(self, s_GlyphLookupDictionary: System.Collections.Generic.Dictionary<System.UInt32,UnityEngine.TextCore.Glyph>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_GlyphLookupDictionary = s_GlyphLookupDictionary


class FontEngineError:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class FontEngineUtilities:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FontFeatureLookupFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GlyphAdjustmentRecord:

    offsets = {'m_GlyphIndex': 16, 'm_GlyphValueRecord': 20}    
    def __init__(self, m_GlyphIndex: System.UInt32, m_GlyphValueRecord: UnityEngine.TextCore.LowLevel.GlyphValueRecord, **kwargs):
        super().__init__(self, **kwargs)
		self.m_GlyphIndex = m_GlyphIndex
		self.m_GlyphValueRecord = m_GlyphValueRecord


class GlyphLoadFlags:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GlyphMarshallingStruct:

    offsets = {'index': 16, 'metrics': 20, 'glyphRect': 40, 'scale': 56, 'atlasIndex': 60}    
    def __init__(self, index: System.UInt32, metrics: UnityEngine.TextCore.GlyphMetrics, glyphRect: UnityEngine.TextCore.GlyphRect, scale: System.Single, atlasIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.index = index
		self.metrics = metrics
		self.glyphRect = glyphRect
		self.scale = scale
		self.atlasIndex = atlasIndex


class GlyphPackingMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GlyphPairAdjustmentRecord:

    offsets = {'m_FirstAdjustmentRecord': 16, 'm_SecondAdjustmentRecord': 36, 'm_FeatureLookupFlags': 56}    
    def __init__(self, m_FirstAdjustmentRecord: UnityEngine.TextCore.LowLevel.GlyphAdjustmentRecord, m_SecondAdjustmentRecord: UnityEngine.TextCore.LowLevel.GlyphAdjustmentRecord, m_FeatureLookupFlags: UnityEngine.TextCore.LowLevel.FontFeatureLookupFlags, **kwargs):
        super().__init__(self, **kwargs)
		self.m_FirstAdjustmentRecord = m_FirstAdjustmentRecord
		self.m_SecondAdjustmentRecord = m_SecondAdjustmentRecord
		self.m_FeatureLookupFlags = m_FeatureLookupFlags


class GlyphRenderMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GlyphValueRecord:

    offsets = {'m_XPlacement': 16, 'm_YPlacement': 20, 'm_XAdvance': 24, 'm_YAdvance': 28}    
    def __init__(self, m_XPlacement: System.Single, m_YPlacement: System.Single, m_XAdvance: System.Single, m_YAdvance: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_XPlacement = m_XPlacement
		self.m_YPlacement = m_YPlacement
		self.m_XAdvance = m_XAdvance
		self.m_YAdvance = m_YAdvance