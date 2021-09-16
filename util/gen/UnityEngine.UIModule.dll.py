


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WillRenderCanvases:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SampleType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AdditionalCanvasShaderChannels:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Canvas:
	preWillRenderCanvases: UnityEngine.Canvas.WillRenderCanvases
    offsets = {'preWillRenderCanvases': 0, 'willRenderCanvases': 8}    
    def __init__(self, preWillRenderCanvases: UnityEngine.Canvas.WillRenderCanvases, willRenderCanvases: UnityEngine.Canvas.WillRenderCanvases, **kwargs):
        super().__init__(self, **kwargs)
		self.preWillRenderCanvases = preWillRenderCanvases
		self.willRenderCanvases = willRenderCanvases


class CanvasGroup:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CanvasRenderer:

    offsets = {'<isMask>k__BackingField': 24}    
    def __init__(self, <isMask>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<isMask>k__BackingField = <isMask>k__BackingField


class ICanvasRaycastFilter:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RectTransformUtility:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RenderMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class UISystemProfilerApi:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
