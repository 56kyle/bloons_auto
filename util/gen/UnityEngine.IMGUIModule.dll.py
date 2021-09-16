


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Scope:

    offsets = {'m_Disposed': 16}    
    def __init__(self, m_Disposed: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Disposed = m_Disposed


class WindowFunction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ParentClipScope:

    offsets = {'m_Disposed': 16}    
    def __init__(self, m_Disposed: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Disposed = m_Disposed


class HorizontalScope:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Type:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LayoutCache:

    offsets = {'topLevel': 16, 'layoutGroups': 24, 'windows': 32}    
    def __init__(self, topLevel: UnityEngine.GUILayoutGroup, layoutGroups: UnityEngineInternal.GenericStack, windows: UnityEngine.GUILayoutGroup, **kwargs):
        super().__init__(self, **kwargs)
		self.topLevel = topLevel
		self.layoutGroups = layoutGroups
		self.windows = windows


class SkinChangedDelegate:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DblClickSnapping:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Event:
	s_Current: UnityEngine.Event
    offsets = {'s_Current': 0, 's_MasterEvent': 8, 'm_Ptr': 16}    
    def __init__(self, s_Current: UnityEngine.Event, s_MasterEvent: UnityEngine.Event, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Current = s_Current
		self.s_MasterEvent = s_MasterEvent
		self.m_Ptr = m_Ptr


class EventInterests:

    offsets = {'<wantsMouseMove>k__BackingField': 16, '<wantsMouseEnterLeaveWindow>k__BackingField': 17}    
    def __init__(self, <wantsMouseMove>k__BackingField: System.Boolean, <wantsMouseEnterLeaveWindow>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<wantsMouseMove>k__BackingField = <wantsMouseMove>k__BackingField
		self.<wantsMouseEnterLeaveWindow>k__BackingField = <wantsMouseEnterLeaveWindow>k__BackingField


class EventModifiers:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class EventType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ExitGUIException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FocusType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class GUI:
	s_ScrollControlId: System.Int32
    offsets = {'s_ScrollControlId': 0, 's_HotTextField': 4, 's_BoxHash': 8, 's_ButonHash': 12, 's_RepeatButtonHash': 16, 's_ToggleHash': 20, 's_ButtonGridHash': 24, 's_SliderHash': 28, 's_BeginGroupHash': 32, 's_ScrollviewHash': 36, '<scrollTroughSide>k__BackingField': 40, '<nextScrollStepTime>k__BackingField': 48, 's_Skin': 56, '<scrollViewStates>k__BackingField': 64}    
    def __init__(self, s_ScrollControlId: System.Int32, s_HotTextField: System.Int32, s_BoxHash: System.Int32, s_ButonHash: System.Int32, s_RepeatButtonHash: System.Int32, s_ToggleHash: System.Int32, s_ButtonGridHash: System.Int32, s_SliderHash: System.Int32, s_BeginGroupHash: System.Int32, s_ScrollviewHash: System.Int32, <scrollTroughSide>k__BackingField: System.Int32, <nextScrollStepTime>k__BackingField: System.DateTime, s_Skin: UnityEngine.GUISkin, <scrollViewStates>k__BackingField: UnityEngineInternal.GenericStack, **kwargs):
        super().__init__(self, **kwargs)
		self.s_ScrollControlId = s_ScrollControlId
		self.s_HotTextField = s_HotTextField
		self.s_BoxHash = s_BoxHash
		self.s_ButonHash = s_ButonHash
		self.s_RepeatButtonHash = s_RepeatButtonHash
		self.s_ToggleHash = s_ToggleHash
		self.s_ButtonGridHash = s_ButtonGridHash
		self.s_SliderHash = s_SliderHash
		self.s_BeginGroupHash = s_BeginGroupHash
		self.s_ScrollviewHash = s_ScrollviewHash
		self.<scrollTroughSide>k__BackingField = <scrollTroughSide>k__BackingField
		self.<nextScrollStepTime>k__BackingField = <nextScrollStepTime>k__BackingField
		self.s_Skin = s_Skin
		self.<scrollViewStates>k__BackingField = <scrollViewStates>k__BackingField


class GUIClip:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GUIContent:
	s_Text: UnityEngine.GUIContent
    offsets = {'s_Text': 0, 's_Image': 8, 's_TextImage': 16, 'none': 24, 'm_Text': 16, 'm_Image': 24, 'm_Tooltip': 32}    
    def __init__(self, s_Text: UnityEngine.GUIContent, s_Image: UnityEngine.GUIContent, s_TextImage: UnityEngine.GUIContent, none: UnityEngine.GUIContent, m_Text: System.String, m_Image: UnityEngine.Texture, m_Tooltip: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Text = s_Text
		self.s_Image = s_Image
		self.s_TextImage = s_TextImage
		self.none = none
		self.m_Text = m_Text
		self.m_Image = m_Image
		self.m_Tooltip = m_Tooltip


class GUILayout:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GUILayoutEntry:
	kDummyRect: UnityEngine.Rect
    offsets = {'kDummyRect': 0, 'indent': 16, 'minWidth': 16, 'maxWidth': 20, 'minHeight': 24, 'maxHeight': 28, 'rect': 32, 'stretchWidth': 48, 'stretchHeight': 52, 'consideredForMargin': 56, 'm_Style': 64}    
    def __init__(self, kDummyRect: UnityEngine.Rect, indent: System.Int32, minWidth: System.Single, maxWidth: System.Single, minHeight: System.Single, maxHeight: System.Single, rect: UnityEngine.Rect, stretchWidth: System.Int32, stretchHeight: System.Int32, consideredForMargin: System.Boolean, m_Style: UnityEngine.GUIStyle, **kwargs):
        super().__init__(self, **kwargs)
		self.kDummyRect = kDummyRect
		self.indent = indent
		self.minWidth = minWidth
		self.maxWidth = maxWidth
		self.minHeight = minHeight
		self.maxHeight = maxHeight
		self.rect = rect
		self.stretchWidth = stretchWidth
		self.stretchHeight = stretchHeight
		self.consideredForMargin = consideredForMargin
		self.m_Style = m_Style


class GUILayoutGroup:

    offsets = {'entries': 72, 'isVertical': 80, 'resetCoords': 81, 'spacing': 84, 'sameSize': 88, 'isWindow': 89, 'windowID': 92, 'm_Cursor': 96, 'm_StretchableCountX': 100, 'm_StretchableCountY': 104, 'm_UserSpecifiedWidth': 108, 'm_UserSpecifiedHeight': 109, 'm_ChildMinWidth': 112, 'm_ChildMaxWidth': 116, 'm_ChildMinHeight': 120, 'm_ChildMaxHeight': 124, 'm_MarginLeft': 128, 'm_MarginRight': 132, 'm_MarginTop': 136, 'm_MarginBottom': 140}    
    def __init__(self, entries: System.Collections.Generic.List<UnityEngine.GUILayoutEntry>, isVertical: System.Boolean, resetCoords: System.Boolean, spacing: System.Single, sameSize: System.Boolean, isWindow: System.Boolean, windowID: System.Int32, m_Cursor: System.Int32, m_StretchableCountX: System.Int32, m_StretchableCountY: System.Int32, m_UserSpecifiedWidth: System.Boolean, m_UserSpecifiedHeight: System.Boolean, m_ChildMinWidth: System.Single, m_ChildMaxWidth: System.Single, m_ChildMinHeight: System.Single, m_ChildMaxHeight: System.Single, m_MarginLeft: System.Int32, m_MarginRight: System.Int32, m_MarginTop: System.Int32, m_MarginBottom: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.entries = entries
		self.isVertical = isVertical
		self.resetCoords = resetCoords
		self.spacing = spacing
		self.sameSize = sameSize
		self.isWindow = isWindow
		self.windowID = windowID
		self.m_Cursor = m_Cursor
		self.m_StretchableCountX = m_StretchableCountX
		self.m_StretchableCountY = m_StretchableCountY
		self.m_UserSpecifiedWidth = m_UserSpecifiedWidth
		self.m_UserSpecifiedHeight = m_UserSpecifiedHeight
		self.m_ChildMinWidth = m_ChildMinWidth
		self.m_ChildMaxWidth = m_ChildMaxWidth
		self.m_ChildMinHeight = m_ChildMinHeight
		self.m_ChildMaxHeight = m_ChildMaxHeight
		self.m_MarginLeft = m_MarginLeft
		self.m_MarginRight = m_MarginRight
		self.m_MarginTop = m_MarginTop
		self.m_MarginBottom = m_MarginBottom


class GUILayoutOption:

    offsets = {'type': 16, 'value': 24}    
    def __init__(self, type: UnityEngine.GUILayoutOption.Type, value: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.type = type
		self.value = value


class GUILayoutUtility:
	s_StoredLayouts: System.Collections.Generic.Dictionary<System.Int32,UnityEngine.GUILayoutUtility.LayoutCache>
    offsets = {'s_StoredLayouts': 0, 's_StoredWindows': 8, 'current': 16, 'kDummyRect': 24, 's_SpaceStyle': 40}    
    def __init__(self, s_StoredLayouts: System.Collections.Generic.Dictionary<System.Int32,UnityEngine.GUILayoutUtility.LayoutCache>, s_StoredWindows: System.Collections.Generic.Dictionary<System.Int32,UnityEngine.GUILayoutUtility.LayoutCache>, current: UnityEngine.GUILayoutUtility.LayoutCache, kDummyRect: UnityEngine.Rect, s_SpaceStyle: UnityEngine.GUIStyle, **kwargs):
        super().__init__(self, **kwargs)
		self.s_StoredLayouts = s_StoredLayouts
		self.s_StoredWindows = s_StoredWindows
		self.current = current
		self.kDummyRect = kDummyRect
		self.s_SpaceStyle = s_SpaceStyle


class GUIScrollGroup:

    offsets = {'calcMinWidth': 144, 'calcMaxWidth': 148, 'calcMinHeight': 152, 'calcMaxHeight': 156, 'clientWidth': 160, 'clientHeight': 164, 'allowHorizontalScroll': 168, 'allowVerticalScroll': 169, 'needsHorizontalScrollbar': 170, 'needsVerticalScrollbar': 171, 'horizontalScrollbar': 176, 'verticalScrollbar': 184}    
    def __init__(self, calcMinWidth: System.Single, calcMaxWidth: System.Single, calcMinHeight: System.Single, calcMaxHeight: System.Single, clientWidth: System.Single, clientHeight: System.Single, allowHorizontalScroll: System.Boolean, allowVerticalScroll: System.Boolean, needsHorizontalScrollbar: System.Boolean, needsVerticalScrollbar: System.Boolean, horizontalScrollbar: UnityEngine.GUIStyle, verticalScrollbar: UnityEngine.GUIStyle, **kwargs):
        super().__init__(self, **kwargs)
		self.calcMinWidth = calcMinWidth
		self.calcMaxWidth = calcMaxWidth
		self.calcMinHeight = calcMinHeight
		self.calcMaxHeight = calcMaxHeight
		self.clientWidth = clientWidth
		self.clientHeight = clientHeight
		self.allowHorizontalScroll = allowHorizontalScroll
		self.allowVerticalScroll = allowVerticalScroll
		self.needsHorizontalScrollbar = needsHorizontalScrollbar
		self.needsVerticalScrollbar = needsVerticalScrollbar
		self.horizontalScrollbar = horizontalScrollbar
		self.verticalScrollbar = verticalScrollbar


class GUISettings:

    offsets = {'m_DoubleClickSelectsWord': 16, 'm_TripleClickSelectsLine': 17, 'm_CursorColor': 20, 'm_CursorFlashSpeed': 36, 'm_SelectionColor': 40}    
    def __init__(self, m_DoubleClickSelectsWord: System.Boolean, m_TripleClickSelectsLine: System.Boolean, m_CursorColor: UnityEngine.Color, m_CursorFlashSpeed: System.Single, m_SelectionColor: UnityEngine.Color, **kwargs):
        super().__init__(self, **kwargs)
		self.m_DoubleClickSelectsWord = m_DoubleClickSelectsWord
		self.m_TripleClickSelectsLine = m_TripleClickSelectsLine
		self.m_CursorColor = m_CursorColor
		self.m_CursorFlashSpeed = m_CursorFlashSpeed
		self.m_SelectionColor = m_SelectionColor


class GUISkin:
	ms_Error: UnityEngine.GUIStyle
    offsets = {'ms_Error': 0, 'm_SkinChanged': 8, 'current': 16, 'm_Font': 24, 'm_box': 32, 'm_button': 40, 'm_toggle': 48, 'm_label': 56, 'm_textField': 64, 'm_textArea': 72, 'm_window': 80, 'm_horizontalSlider': 88, 'm_horizontalSliderThumb': 96, 'm_horizontalSliderThumbExtent': 104, 'm_verticalSlider': 112, 'm_verticalSliderThumb': 120, 'm_verticalSliderThumbExtent': 128, 'm_horizontalScrollbar': 136, 'm_horizontalScrollbarThumb': 144, 'm_horizontalScrollbarLeftButton': 152, 'm_horizontalScrollbarRightButton': 160, 'm_verticalScrollbar': 168, 'm_verticalScrollbarThumb': 176, 'm_verticalScrollbarUpButton': 184, 'm_verticalScrollbarDownButton': 192, 'm_ScrollView': 200, 'm_Settings': 216, 'm_Styles': 224}    
    def __init__(self, ms_Error: UnityEngine.GUIStyle, m_SkinChanged: UnityEngine.GUISkin.SkinChangedDelegate, current: UnityEngine.GUISkin, m_Font: UnityEngine.Font, m_box: UnityEngine.GUIStyle, m_button: UnityEngine.GUIStyle, m_toggle: UnityEngine.GUIStyle, m_label: UnityEngine.GUIStyle, m_textField: UnityEngine.GUIStyle, m_textArea: UnityEngine.GUIStyle, m_window: UnityEngine.GUIStyle, m_horizontalSlider: UnityEngine.GUIStyle, m_horizontalSliderThumb: UnityEngine.GUIStyle, m_horizontalSliderThumbExtent: UnityEngine.GUIStyle, m_verticalSlider: UnityEngine.GUIStyle, m_verticalSliderThumb: UnityEngine.GUIStyle, m_verticalSliderThumbExtent: UnityEngine.GUIStyle, m_horizontalScrollbar: UnityEngine.GUIStyle, m_horizontalScrollbarThumb: UnityEngine.GUIStyle, m_horizontalScrollbarLeftButton: UnityEngine.GUIStyle, m_horizontalScrollbarRightButton: UnityEngine.GUIStyle, m_verticalScrollbar: UnityEngine.GUIStyle, m_verticalScrollbarThumb: UnityEngine.GUIStyle, m_verticalScrollbarUpButton: UnityEngine.GUIStyle, m_verticalScrollbarDownButton: UnityEngine.GUIStyle, m_ScrollView: UnityEngine.GUIStyle, m_Settings: UnityEngine.GUISettings, m_Styles: System.Collections.Generic.Dictionary<System.String,UnityEngine.GUIStyle>, **kwargs):
        super().__init__(self, **kwargs)
		self.ms_Error = ms_Error
		self.m_SkinChanged = m_SkinChanged
		self.current = current
		self.m_Font = m_Font
		self.m_box = m_box
		self.m_button = m_button
		self.m_toggle = m_toggle
		self.m_label = m_label
		self.m_textField = m_textField
		self.m_textArea = m_textArea
		self.m_window = m_window
		self.m_horizontalSlider = m_horizontalSlider
		self.m_horizontalSliderThumb = m_horizontalSliderThumb
		self.m_horizontalSliderThumbExtent = m_horizontalSliderThumbExtent
		self.m_verticalSlider = m_verticalSlider
		self.m_verticalSliderThumb = m_verticalSliderThumb
		self.m_verticalSliderThumbExtent = m_verticalSliderThumbExtent
		self.m_horizontalScrollbar = m_horizontalScrollbar
		self.m_horizontalScrollbarThumb = m_horizontalScrollbarThumb
		self.m_horizontalScrollbarLeftButton = m_horizontalScrollbarLeftButton
		self.m_horizontalScrollbarRightButton = m_horizontalScrollbarRightButton
		self.m_verticalScrollbar = m_verticalScrollbar
		self.m_verticalScrollbarThumb = m_verticalScrollbarThumb
		self.m_verticalScrollbarUpButton = m_verticalScrollbarUpButton
		self.m_verticalScrollbarDownButton = m_verticalScrollbarDownButton
		self.m_ScrollView = m_ScrollView
		self.m_Settings = m_Settings
		self.m_Styles = m_Styles


class GUIStateObjects:
	s_StateCache: System.Collections.Generic.Dictionary<System.Int32,System.Object>
    offsets = {'s_StateCache': 0}    
    def __init__(self, s_StateCache: System.Collections.Generic.Dictionary<System.Int32,System.Object>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_StateCache = s_StateCache


class GUIStyle:
	showKeyboardFocus: System.Boolean
    offsets = {'showKeyboardFocus': 0, 's_None': 8, 'm_Ptr': 16, 'm_Normal': 24, 'm_Hover': 32, 'm_Active': 40, 'm_Focused': 48, 'm_OnNormal': 56, 'm_OnHover': 64, 'm_OnActive': 72, 'm_OnFocused': 80, 'm_Border': 88, 'm_Padding': 96, 'm_Margin': 104, 'm_Overflow': 112, 'm_Name': 120}    
    def __init__(self, showKeyboardFocus: System.Boolean, s_None: UnityEngine.GUIStyle, m_Ptr: System.IntPtr, m_Normal: UnityEngine.GUIStyleState, m_Hover: UnityEngine.GUIStyleState, m_Active: UnityEngine.GUIStyleState, m_Focused: UnityEngine.GUIStyleState, m_OnNormal: UnityEngine.GUIStyleState, m_OnHover: UnityEngine.GUIStyleState, m_OnActive: UnityEngine.GUIStyleState, m_OnFocused: UnityEngine.GUIStyleState, m_Border: UnityEngine.RectOffset, m_Padding: UnityEngine.RectOffset, m_Margin: UnityEngine.RectOffset, m_Overflow: UnityEngine.RectOffset, m_Name: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.showKeyboardFocus = showKeyboardFocus
		self.s_None = s_None
		self.m_Ptr = m_Ptr
		self.m_Normal = m_Normal
		self.m_Hover = m_Hover
		self.m_Active = m_Active
		self.m_Focused = m_Focused
		self.m_OnNormal = m_OnNormal
		self.m_OnHover = m_OnHover
		self.m_OnActive = m_OnActive
		self.m_OnFocused = m_OnFocused
		self.m_Border = m_Border
		self.m_Padding = m_Padding
		self.m_Margin = m_Margin
		self.m_Overflow = m_Overflow
		self.m_Name = m_Name


class GUIStyleState:

    offsets = {'m_Ptr': 16, 'm_SourceStyle': 24}    
    def __init__(self, m_Ptr: System.IntPtr, m_SourceStyle: UnityEngine.GUIStyle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_SourceStyle = m_SourceStyle


class GUITargetAttribute:

    offsets = {'displayMask': 16}    
    def __init__(self, displayMask: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.displayMask = displayMask


class GUIUtility:
	s_SkinMode: System.Int32
    offsets = {'s_SkinMode': 0, 's_OriginalID': 4, 'takeCapture': 8, 'releaseCapture': 16, 'processEvent': 24, 'cleanupRoots': 32, 'endContainerGUIFromException': 40, 'guiChanged': 48, '<guiIsExiting>k__BackingField': 56, 's_HasCurrentWindowKeyFocusFunc': 64}    
    def __init__(self, s_SkinMode: System.Int32, s_OriginalID: System.Int32, takeCapture: System.Action, releaseCapture: System.Action, processEvent: System.Func<System.Int32,System.IntPtr,System.Boolean>, cleanupRoots: System.Action, endContainerGUIFromException: System.Func<System.Exception,System.Boolean>, guiChanged: System.Action, <guiIsExiting>k__BackingField: System.Boolean, s_HasCurrentWindowKeyFocusFunc: System.Func<System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_SkinMode = s_SkinMode
		self.s_OriginalID = s_OriginalID
		self.takeCapture = takeCapture
		self.releaseCapture = releaseCapture
		self.processEvent = processEvent
		self.cleanupRoots = cleanupRoots
		self.endContainerGUIFromException = endContainerGUIFromException
		self.guiChanged = guiChanged
		self.<guiIsExiting>k__BackingField = <guiIsExiting>k__BackingField
		self.s_HasCurrentWindowKeyFocusFunc = s_HasCurrentWindowKeyFocusFunc


class GUIWordWrapSizer:

    offsets = {'m_Content': 72, 'm_ForcedMinHeight': 80, 'm_ForcedMaxHeight': 84}    
    def __init__(self, m_Content: UnityEngine.GUIContent, m_ForcedMinHeight: System.Single, m_ForcedMaxHeight: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Content = m_Content
		self.m_ForcedMinHeight = m_ForcedMinHeight
		self.m_ForcedMaxHeight = m_ForcedMaxHeight


class ImagePosition:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ObjectGUIState:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class PointerType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ScaleMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ScrollViewState:

    offsets = {'position': 16, 'visibleRect': 32, 'viewRect': 48, 'scrollPosition': 64, 'apply': 72}    
    def __init__(self, position: UnityEngine.Rect, visibleRect: UnityEngine.Rect, viewRect: UnityEngine.Rect, scrollPosition: UnityEngine.Vector2, apply: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.position = position
		self.visibleRect = visibleRect
		self.viewRect = viewRect
		self.scrollPosition = scrollPosition
		self.apply = apply


class SliderHandler:

    offsets = {'position': 16, 'currentValue': 32, 'size': 36, 'start': 40, 'end': 44, 'slider': 48, 'thumb': 56, 'thumbExtent': 64, 'horiz': 72, 'id': 76}    
    def __init__(self, position: UnityEngine.Rect, currentValue: System.Single, size: System.Single, start: System.Single, end: System.Single, slider: UnityEngine.GUIStyle, thumb: UnityEngine.GUIStyle, thumbExtent: UnityEngine.GUIStyle, horiz: System.Boolean, id: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.position = position
		self.currentValue = currentValue
		self.size = size
		self.start = start
		self.end = end
		self.slider = slider
		self.thumb = thumb
		self.thumbExtent = thumbExtent
		self.horiz = horiz
		self.id = id


class SliderState:

    offsets = {'dragStartPos': 16, 'dragStartValue': 20, 'isDragging': 24}    
    def __init__(self, dragStartPos: System.Single, dragStartValue: System.Single, isDragging: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.dragStartPos = dragStartPos
		self.dragStartValue = dragStartValue
		self.isDragging = isDragging


class TextEditor:

    offsets = {'keyboardOnScreen': 16, 'controlID': 24, 'style': 32, 'multiline': 40, 'hasHorizontalCursorPos': 41, 'isPasswordField': 42, 'scrollOffset': 44, 'm_Content': 56, 'm_Position': 64, 'm_CursorIndex': 80, 'm_SelectIndex': 84, 'm_RevealCursor': 88, 'm_MouseDragSelectsWholeWords': 89, 'm_DblClickInitPos': 92, 'm_DblClickSnap': 96, 'm_bJustSelected': 97, 'm_iAltCursorPos': 100}    
    def __init__(self, keyboardOnScreen: UnityEngine.TouchScreenKeyboard, controlID: System.Int32, style: UnityEngine.GUIStyle, multiline: System.Boolean, hasHorizontalCursorPos: System.Boolean, isPasswordField: System.Boolean, scrollOffset: UnityEngine.Vector2, m_Content: UnityEngine.GUIContent, m_Position: UnityEngine.Rect, m_CursorIndex: System.Int32, m_SelectIndex: System.Int32, m_RevealCursor: System.Boolean, m_MouseDragSelectsWholeWords: System.Boolean, m_DblClickInitPos: System.Int32, m_DblClickSnap: UnityEngine.TextEditor.DblClickSnapping, m_bJustSelected: System.Boolean, m_iAltCursorPos: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.keyboardOnScreen = keyboardOnScreen
		self.controlID = controlID
		self.style = style
		self.multiline = multiline
		self.hasHorizontalCursorPos = hasHorizontalCursorPos
		self.isPasswordField = isPasswordField
		self.scrollOffset = scrollOffset
		self.m_Content = m_Content
		self.m_Position = m_Position
		self.m_CursorIndex = m_CursorIndex
		self.m_SelectIndex = m_SelectIndex
		self.m_RevealCursor = m_RevealCursor
		self.m_MouseDragSelectsWholeWords = m_MouseDragSelectsWholeWords
		self.m_DblClickInitPos = m_DblClickInitPos
		self.m_DblClickSnap = m_DblClickSnap
		self.m_bJustSelected = m_bJustSelected
		self.m_iAltCursorPos = m_iAltCursorPos