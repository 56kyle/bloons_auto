


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EventPropagation:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class LifeCycleStatus:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DispatchContext:

    offsets = {'m_GateCount': 16, 'm_Queue': 24}    
    def __init__(self, m_GateCount: System.UInt32, m_Queue: System.Collections.Generic.Queue<UnityEngine.UIElements.EventDispatcher.EventRecord>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_GateCount = m_GateCount
		self.m_Queue = m_Queue


class EventRecord:

    offsets = {'m_Event': 16, 'm_Panel': 24}    
    def __init__(self, m_Event: UnityEngine.UIElements.EventBase, m_Panel: UnityEngine.UIElements.IPanel, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Event = m_Event
		self.m_Panel = m_Panel


class FocusedElement:

    offsets = {'m_SubTreeRoot': 16, 'm_FocusedElement': 24}    
    def __init__(self, m_SubTreeRoot: UnityEngine.UIElements.VisualElement, m_FocusedElement: UnityEngine.UIElements.Focusable, **kwargs):
        super().__init__(self, **kwargs)
		self.m_SubTreeRoot = m_SubTreeRoot
		self.m_FocusedElement = m_FocusedElement


class GUIGlobals:

    offsets = {'matrix': 16, 'color': 80, 'contentColor': 96, 'backgroundColor': 112, 'enabled': 128, 'changed': 129, 'displayIndex': 132}    
    def __init__(self, matrix: UnityEngine.Matrix4x4, color: UnityEngine.Color, contentColor: UnityEngine.Color, backgroundColor: UnityEngine.Color, enabled: System.Boolean, changed: System.Boolean, displayIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.matrix = matrix
		self.color = color
		self.contentColor = contentColor
		self.backgroundColor = backgroundColor
		self.enabled = enabled
		self.changed = changed
		self.displayIndex = displayIndex


class EventBehavior:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Type:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SheetHandleKey:

    offsets = {'sheetInstanceID': 16, 'index': 20}    
    def __init__(self, sheetInstanceID: System.Int32, index: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.sheetInstanceID = sheetInstanceID
		self.index = index


class SheetHandleKeyComparer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GPUBuffer<T>:

    offsets = {'buffer': 0}    
    def __init__(self, buffer: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.buffer = buffer


class Hierarchy:

    offsets = {'m_Owner': 16}    
    def __init__(self, m_Owner: UnityEngine.UIElements.VisualElement, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Owner = m_Owner


class UpdaterArray:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class BaseVisualElementPanel:

    offsets = {'m_PixelsPerPoint': 16, '<duringLayoutPhase>k__BackingField': 20, '<repaintData>k__BackingField': 24, '<disposed>k__BackingField': 32, 'm_TopElementUnderPointers': 40}    
    def __init__(self, m_PixelsPerPoint: System.Single, <duringLayoutPhase>k__BackingField: System.Boolean, <repaintData>k__BackingField: UnityEngine.UIElements.RepaintData, <disposed>k__BackingField: System.Boolean, m_TopElementUnderPointers: UnityEngine.UIElements.ElementUnderPointer, **kwargs):
        super().__init__(self, **kwargs)
		self.m_PixelsPerPoint = m_PixelsPerPoint
		self.<duringLayoutPhase>k__BackingField = <duringLayoutPhase>k__BackingField
		self.<repaintData>k__BackingField = <repaintData>k__BackingField
		self.<disposed>k__BackingField = <disposed>k__BackingField
		self.m_TopElementUnderPointers = m_TopElementUnderPointers


class BlurEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CallbackEventHandler:

    offsets = {'m_CallbackRegistry': 16}    
    def __init__(self, m_CallbackRegistry: UnityEngine.UIElements.EventCallbackRegistry, **kwargs):
        super().__init__(self, **kwargs)
		self.m_CallbackRegistry = m_CallbackRegistry


class CallbackPhase:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class CommandEventBase<T>:

    offsets = {'m_CommandName': 0}    
    def __init__(self, m_CommandName: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_CommandName = m_CommandName


class CommandEventDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ComputedStyle:

    offsets = {'m_Element': 16}    
    def __init__(self, m_Element: UnityEngine.UIElements.VisualElement, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Element = m_Element


class ContextClickEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ContextType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DefaultDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DispatchMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DisplayStyle:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class DragAndDropEventBase<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DragEnterEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DragExitedEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DragLeaveEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DragPerformEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DragUpdatedEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ElementUnderPointer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EventBase:
	s_LastTypeId: System.Int64
    offsets = {'s_LastTypeId': 0, 's_NextEventId': 8, '<timestamp>k__BackingField': 16, '<eventId>k__BackingField': 24, '<triggerEventId>k__BackingField': 32, '<propagation>k__BackingField': 40, 'm_Path': 48, '<lifeCycleStatus>k__BackingField': 56, '<leafTarget>k__BackingField': 64, 'm_Target': 72, '<skipElements>k__BackingField': 80, '<propagationPhase>k__BackingField': 88, 'm_CurrentTarget': 96, 'm_ImguiEvent': 104, '<originalMousePosition>k__BackingField': 112}    
    def __init__(self, s_LastTypeId: System.Int64, s_NextEventId: System.UInt64, <timestamp>k__BackingField: System.Int64, <eventId>k__BackingField: System.UInt64, <triggerEventId>k__BackingField: System.UInt64, <propagation>k__BackingField: UnityEngine.UIElements.EventBase.EventPropagation, m_Path: UnityEngine.UIElements.PropagationPaths, <lifeCycleStatus>k__BackingField: UnityEngine.UIElements.EventBase.LifeCycleStatus, <leafTarget>k__BackingField: UnityEngine.UIElements.IEventHandler, m_Target: UnityEngine.UIElements.IEventHandler, <skipElements>k__BackingField: System.Collections.Generic.List<UnityEngine.UIElements.IEventHandler>, <propagationPhase>k__BackingField: UnityEngine.UIElements.PropagationPhase, m_CurrentTarget: UnityEngine.UIElements.IEventHandler, m_ImguiEvent: UnityEngine.Event, <originalMousePosition>k__BackingField: UnityEngine.Vector2, **kwargs):
        super().__init__(self, **kwargs)
		self.s_LastTypeId = s_LastTypeId
		self.s_NextEventId = s_NextEventId
		self.<timestamp>k__BackingField = <timestamp>k__BackingField
		self.<eventId>k__BackingField = <eventId>k__BackingField
		self.<triggerEventId>k__BackingField = <triggerEventId>k__BackingField
		self.<propagation>k__BackingField = <propagation>k__BackingField
		self.m_Path = m_Path
		self.<lifeCycleStatus>k__BackingField = <lifeCycleStatus>k__BackingField
		self.<leafTarget>k__BackingField = <leafTarget>k__BackingField
		self.m_Target = m_Target
		self.<skipElements>k__BackingField = <skipElements>k__BackingField
		self.<propagationPhase>k__BackingField = <propagationPhase>k__BackingField
		self.m_CurrentTarget = m_CurrentTarget
		self.m_ImguiEvent = m_ImguiEvent
		self.<originalMousePosition>k__BackingField = <originalMousePosition>k__BackingField


class EventBase<T>:
	s_TypeId: System.Int64
    offsets = {'s_TypeId': 0, 's_Pool': 0, 'm_RefCount': 0}    
    def __init__(self, s_TypeId: System.Int64, s_Pool: UnityEngine.UIElements.ObjectPool<T>, m_RefCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.s_TypeId = s_TypeId
		self.s_Pool = s_Pool
		self.m_RefCount = m_RefCount


class EventCallbackFunctorBase:

    offsets = {'<phase>k__BackingField': 16}    
    def __init__(self, <phase>k__BackingField: UnityEngine.UIElements.CallbackPhase, **kwargs):
        super().__init__(self, **kwargs)
		self.<phase>k__BackingField = <phase>k__BackingField


class EventCallbackList:

    offsets = {'m_List': 16, '<trickleDownCallbackCount>k__BackingField': 24, '<bubbleUpCallbackCount>k__BackingField': 28}    
    def __init__(self, m_List: System.Collections.Generic.List<UnityEngine.UIElements.EventCallbackFunctorBase>, <trickleDownCallbackCount>k__BackingField: System.Int32, <bubbleUpCallbackCount>k__BackingField: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_List = m_List
		self.<trickleDownCallbackCount>k__BackingField = <trickleDownCallbackCount>k__BackingField
		self.<bubbleUpCallbackCount>k__BackingField = <bubbleUpCallbackCount>k__BackingField


class EventCallbackListPool:

    offsets = {'m_Stack': 16}    
    def __init__(self, m_Stack: System.Collections.Generic.Stack<UnityEngine.UIElements.EventCallbackList>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Stack = m_Stack


class EventCallbackRegistry:
	s_ListPool: UnityEngine.UIElements.EventCallbackListPool
    offsets = {'s_ListPool': 0, 'm_Callbacks': 16, 'm_TemporaryCallbacks': 24, 'm_IsInvoking': 32}    
    def __init__(self, s_ListPool: UnityEngine.UIElements.EventCallbackListPool, m_Callbacks: UnityEngine.UIElements.EventCallbackList, m_TemporaryCallbacks: UnityEngine.UIElements.EventCallbackList, m_IsInvoking: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.s_ListPool = s_ListPool
		self.m_Callbacks = m_Callbacks
		self.m_TemporaryCallbacks = m_TemporaryCallbacks
		self.m_IsInvoking = m_IsInvoking


class EventDebugger:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EventDebuggerLogExecuteDefaultAction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EventDebuggerLogIMGUICall:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EventDispatchUtilities:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EventDispatcher:
	k_EventQueuePool: UnityEngine.UIElements.ObjectPool<System.Collections.Generic.Queue<UnityEngine.UIElements.EventDispatcher.EventRecord>>
    offsets = {'k_EventQueuePool': 0, 'm_DispatchingStrategies': 16, 'm_Queue': 24, '<pointerState>k__BackingField': 32, 'm_GateCount': 40, 'm_DispatchContexts': 48, 'm_Immediate': 56}    
    def __init__(self, k_EventQueuePool: UnityEngine.UIElements.ObjectPool<System.Collections.Generic.Queue<UnityEngine.UIElements.EventDispatcher.EventRecord>>, m_DispatchingStrategies: System.Collections.Generic.List<UnityEngine.UIElements.IEventDispatchingStrategy>, m_Queue: System.Collections.Generic.Queue<UnityEngine.UIElements.EventDispatcher.EventRecord>, <pointerState>k__BackingField: UnityEngine.UIElements.PointerDispatchState, m_GateCount: System.UInt32, m_DispatchContexts: System.Collections.Generic.Stack<UnityEngine.UIElements.EventDispatcher.DispatchContext>, m_Immediate: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.k_EventQueuePool = k_EventQueuePool
		self.m_DispatchingStrategies = m_DispatchingStrategies
		self.m_Queue = m_Queue
		self.<pointerState>k__BackingField = <pointerState>k__BackingField
		self.m_GateCount = m_GateCount
		self.m_DispatchContexts = m_DispatchContexts
		self.m_Immediate = m_Immediate


class EventDispatcherGate:

    offsets = {'m_Dispatcher': 16}    
    def __init__(self, m_Dispatcher: UnityEngine.UIElements.EventDispatcher, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Dispatcher = m_Dispatcher


class ExecuteCommandEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FocusChangeDirection:
	<unspecified>k__BackingField: UnityEngine.UIElements.FocusChangeDirection
    offsets = {'<unspecified>k__BackingField': 0, '<none>k__BackingField': 8, '<lastValue>k__BackingField': 16, 'm_Value': 16}    
    def __init__(self, <unspecified>k__BackingField: UnityEngine.UIElements.FocusChangeDirection, <none>k__BackingField: UnityEngine.UIElements.FocusChangeDirection, <lastValue>k__BackingField: UnityEngine.UIElements.FocusChangeDirection, m_Value: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<unspecified>k__BackingField = <unspecified>k__BackingField
		self.<none>k__BackingField = <none>k__BackingField
		self.<lastValue>k__BackingField = <lastValue>k__BackingField
		self.m_Value = m_Value


class FocusController:

    offsets = {'<focusRing>k__BackingField': 16, 'm_FocusedElements': 24, '<imguiKeyboardControl>k__BackingField': 32}    
    def __init__(self, <focusRing>k__BackingField: UnityEngine.UIElements.IFocusRing, m_FocusedElements: System.Collections.Generic.List<UnityEngine.UIElements.FocusController.FocusedElement>, <imguiKeyboardControl>k__BackingField: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<focusRing>k__BackingField = <focusRing>k__BackingField
		self.m_FocusedElements = m_FocusedElements
		self.<imguiKeyboardControl>k__BackingField = <imguiKeyboardControl>k__BackingField


class FocusEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FocusEventBase<T>:

    offsets = {'<relatedTarget>k__BackingField': 0, '<direction>k__BackingField': 0, '<focusController>k__BackingField': 0}    
    def __init__(self, <relatedTarget>k__BackingField: UnityEngine.UIElements.Focusable, <direction>k__BackingField: UnityEngine.UIElements.FocusChangeDirection, <focusController>k__BackingField: UnityEngine.UIElements.FocusController, **kwargs):
        super().__init__(self, **kwargs)
		self.<relatedTarget>k__BackingField = <relatedTarget>k__BackingField
		self.<direction>k__BackingField = <direction>k__BackingField
		self.<focusController>k__BackingField = <focusController>k__BackingField


class FocusInEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class FocusOutEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Focusable:

    offsets = {'<focusable>k__BackingField': 24, 'isIMGUIContainer': 25}    
    def __init__(self, <focusable>k__BackingField: System.Boolean, isIMGUIContainer: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<focusable>k__BackingField = <focusable>k__BackingField
		self.isIMGUIContainer = isIMGUIContainer


class ICommandEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IEventDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IEventHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IFocusRing:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IKeyboardEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IMGUIContainer:
	ussClassName: System.String
    offsets = {'ussClassName': 0, 'm_OnGUIHandler': 352, 'm_ObjectGUIState': 360, 'useOwnerObjectGUIState': 368, '<lastWorldClip>k__BackingField': 372, 'm_Cache': 392, 'm_CachedClippingRect': 400, 'm_CachedTransform': 416, '<contextType>k__BackingField': 480, 'lostFocus': 484, 'receivedFocus': 485, 'focusChangeDirection': 488, 'hasFocusableControls': 496, 'newKeyboardFocusControlID': 500, '<focusOnlyIfHasFocusableControls>k__BackingField': 504, 'm_GUIGlobals': 508}    
    def __init__(self, ussClassName: System.String, m_OnGUIHandler: System.Action, m_ObjectGUIState: UnityEngine.ObjectGUIState, useOwnerObjectGUIState: System.Boolean, <lastWorldClip>k__BackingField: UnityEngine.Rect, m_Cache: UnityEngine.GUILayoutUtility.LayoutCache, m_CachedClippingRect: UnityEngine.Rect, m_CachedTransform: UnityEngine.Matrix4x4, <contextType>k__BackingField: UnityEngine.UIElements.ContextType, lostFocus: System.Boolean, receivedFocus: System.Boolean, focusChangeDirection: UnityEngine.UIElements.FocusChangeDirection, hasFocusableControls: System.Boolean, newKeyboardFocusControlID: System.Int32, <focusOnlyIfHasFocusableControls>k__BackingField: System.Boolean, m_GUIGlobals: UnityEngine.UIElements.IMGUIContainer.GUIGlobals, **kwargs):
        super().__init__(self, **kwargs)
		self.ussClassName = ussClassName
		self.m_OnGUIHandler = m_OnGUIHandler
		self.m_ObjectGUIState = m_ObjectGUIState
		self.useOwnerObjectGUIState = useOwnerObjectGUIState
		self.<lastWorldClip>k__BackingField = <lastWorldClip>k__BackingField
		self.m_Cache = m_Cache
		self.m_CachedClippingRect = m_CachedClippingRect
		self.m_CachedTransform = m_CachedTransform
		self.<contextType>k__BackingField = <contextType>k__BackingField
		self.lostFocus = lostFocus
		self.receivedFocus = receivedFocus
		self.focusChangeDirection = focusChangeDirection
		self.hasFocusableControls = hasFocusableControls
		self.newKeyboardFocusControlID = newKeyboardFocusControlID
		self.<focusOnlyIfHasFocusableControls>k__BackingField = <focusOnlyIfHasFocusableControls>k__BackingField
		self.m_GUIGlobals = m_GUIGlobals


class IMGUIEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IMGUIEventDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IMouseEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IMouseEventInternal:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPanel:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPointerEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IPointerEventInternal:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IResolvedStyle:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IStyleValue<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ITransform:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IVisualTreeUpdater:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class KeyDownEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class KeyUpEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class KeyboardEventBase<T>:

    offsets = {'<modifiers>k__BackingField': 0, '<character>k__BackingField': 0, '<keyCode>k__BackingField': 0}    
    def __init__(self, <modifiers>k__BackingField: UnityEngine.EventModifiers, <character>k__BackingField: System.Char, <keyCode>k__BackingField: UnityEngine.KeyCode, **kwargs):
        super().__init__(self, **kwargs)
		self.<modifiers>k__BackingField = <modifiers>k__BackingField
		self.<character>k__BackingField = <character>k__BackingField
		self.<keyCode>k__BackingField = <keyCode>k__BackingField


class KeyboardEventDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Length:

    offsets = {'m_Value': 16, 'm_Unit': 20}    
    def __init__(self, m_Value: System.Single, m_Unit: UnityEngine.UIElements.LengthUnit, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Value = m_Value
		self.m_Unit = m_Unit


class LengthUnit:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class MouseCaptureController:
	m_IsMouseCapturedWarningEmitted: System.Boolean
    offsets = {'m_IsMouseCapturedWarningEmitted': 0, 'm_ReleaseMouseWarningEmitted': 1}    
    def __init__(self, m_IsMouseCapturedWarningEmitted: System.Boolean, m_ReleaseMouseWarningEmitted: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_IsMouseCapturedWarningEmitted = m_IsMouseCapturedWarningEmitted
		self.m_ReleaseMouseWarningEmitted = m_ReleaseMouseWarningEmitted


class MouseCaptureDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseCaptureEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseCaptureEventBase<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseCaptureOutEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseDownEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseEnterEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseEnterWindowEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseEventBase<T>:

    offsets = {'<modifiers>k__BackingField': 0, '<mousePosition>k__BackingField': 0, '<localMousePosition>k__BackingField': 0, '<mouseDelta>k__BackingField': 0, '<clickCount>k__BackingField': 0, '<button>k__BackingField': 0, '<pressedButtons>k__BackingField': 0, '<UnityEngine.UIElements.IMouseEventInternal.triggeredByOS>k__BackingField': 0, '<UnityEngine.UIElements.IMouseEventInternal.recomputeTopElementUnderMouse>k__BackingField': 0, '<UnityEngine.UIElements.IMouseEventInternal.sourcePointerEvent>k__BackingField': 0}    
    def __init__(self, <modifiers>k__BackingField: UnityEngine.EventModifiers, <mousePosition>k__BackingField: UnityEngine.Vector2, <localMousePosition>k__BackingField: UnityEngine.Vector2, <mouseDelta>k__BackingField: UnityEngine.Vector2, <clickCount>k__BackingField: System.Int32, <button>k__BackingField: System.Int32, <pressedButtons>k__BackingField: System.Int32, <UnityEngine.UIElements.IMouseEventInternal.triggeredByOS>k__BackingField: System.Boolean, <UnityEngine.UIElements.IMouseEventInternal.recomputeTopElementUnderMouse>k__BackingField: System.Boolean, <UnityEngine.UIElements.IMouseEventInternal.sourcePointerEvent>k__BackingField: UnityEngine.UIElements.IPointerEvent, **kwargs):
        super().__init__(self, **kwargs)
		self.<modifiers>k__BackingField = <modifiers>k__BackingField
		self.<mousePosition>k__BackingField = <mousePosition>k__BackingField
		self.<localMousePosition>k__BackingField = <localMousePosition>k__BackingField
		self.<mouseDelta>k__BackingField = <mouseDelta>k__BackingField
		self.<clickCount>k__BackingField = <clickCount>k__BackingField
		self.<button>k__BackingField = <button>k__BackingField
		self.<pressedButtons>k__BackingField = <pressedButtons>k__BackingField
		self.<UnityEngine.UIElements.IMouseEventInternal.triggeredByOS>k__BackingField = <UnityEngine.UIElements.IMouseEventInternal.triggeredByOS>k__BackingField
		self.<UnityEngine.UIElements.IMouseEventInternal.recomputeTopElementUnderMouse>k__BackingField = <UnityEngine.UIElements.IMouseEventInternal.recomputeTopElementUnderMouse>k__BackingField
		self.<UnityEngine.UIElements.IMouseEventInternal.sourcePointerEvent>k__BackingField = <UnityEngine.UIElements.IMouseEventInternal.sourcePointerEvent>k__BackingField


class MouseEventDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseEventsHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseLeaveEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseLeaveWindowEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseMoveEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseOutEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseOverEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MouseUpEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ObjectPool<T>:

    offsets = {'m_Stack': 0, 'm_MaxSize': 0}    
    def __init__(self, m_Stack: System.Collections.Generic.Stack<T>, m_MaxSize: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Stack = m_Stack
		self.m_MaxSize = m_MaxSize


class Overflow:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Panel:
	s_MarkerPickAll: Unity.Profiling.ProfilerMarker
    offsets = {'s_MarkerPickAll': 0, 'm_RootContainer': 48, 'm_VisualTreeUpdater': 56, 'm_Version': 64, 'm_RepaintVersion': 68, 'm_MarkerUpdate': 72, '<dispatcher>k__BackingField': 80, '<ownerObject>k__BackingField': 88, '<contextType>k__BackingField': 96, '<focusController>k__BackingField': 104, '<IMGUIEventInterests>k__BackingField': 112, '<IMGUIContainersCount>k__BackingField': 116, '<rootIMGUIContainer>k__BackingField': 120, 'm_ValidatingLayout': 128}    
    def __init__(self, s_MarkerPickAll: Unity.Profiling.ProfilerMarker, m_RootContainer: UnityEngine.UIElements.VisualElement, m_VisualTreeUpdater: UnityEngine.UIElements.VisualTreeUpdater, m_Version: System.UInt32, m_RepaintVersion: System.UInt32, m_MarkerUpdate: Unity.Profiling.ProfilerMarker, <dispatcher>k__BackingField: UnityEngine.UIElements.EventDispatcher, <ownerObject>k__BackingField: UnityEngine.ScriptableObject, <contextType>k__BackingField: UnityEngine.UIElements.ContextType, <focusController>k__BackingField: UnityEngine.UIElements.FocusController, <IMGUIEventInterests>k__BackingField: UnityEngine.EventInterests, <IMGUIContainersCount>k__BackingField: System.Int32, <rootIMGUIContainer>k__BackingField: UnityEngine.UIElements.IMGUIContainer, m_ValidatingLayout: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.s_MarkerPickAll = s_MarkerPickAll
		self.m_RootContainer = m_RootContainer
		self.m_VisualTreeUpdater = m_VisualTreeUpdater
		self.m_Version = m_Version
		self.m_RepaintVersion = m_RepaintVersion
		self.m_MarkerUpdate = m_MarkerUpdate
		self.<dispatcher>k__BackingField = <dispatcher>k__BackingField
		self.<ownerObject>k__BackingField = <ownerObject>k__BackingField
		self.<contextType>k__BackingField = <contextType>k__BackingField
		self.<focusController>k__BackingField = <focusController>k__BackingField
		self.<IMGUIEventInterests>k__BackingField = <IMGUIEventInterests>k__BackingField
		self.<IMGUIContainersCount>k__BackingField = <IMGUIContainersCount>k__BackingField
		self.<rootIMGUIContainer>k__BackingField = <rootIMGUIContainer>k__BackingField
		self.m_ValidatingLayout = m_ValidatingLayout


class PickingMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PointerCancelEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerCaptureDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerCaptureEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerCaptureEventBase<T>:

    offsets = {'<relatedTarget>k__BackingField': 0, '<pointerId>k__BackingField': 0}    
    def __init__(self, <relatedTarget>k__BackingField: UnityEngine.UIElements.IEventHandler, <pointerId>k__BackingField: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<relatedTarget>k__BackingField = <relatedTarget>k__BackingField
		self.<pointerId>k__BackingField = <pointerId>k__BackingField


class PointerCaptureHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerCaptureOutEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerDeviceState:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerDispatchState:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerDownEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerEnterEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerEventBase<T>:

    offsets = {'<pointerId>k__BackingField': 0, '<pointerType>k__BackingField': 0, '<isPrimary>k__BackingField': 0, '<button>k__BackingField': 0, '<pressedButtons>k__BackingField': 0, '<position>k__BackingField': 0, '<localPosition>k__BackingField': 0, '<deltaPosition>k__BackingField': 0, '<deltaTime>k__BackingField': 0, '<clickCount>k__BackingField': 0, '<pressure>k__BackingField': 0, '<tangentialPressure>k__BackingField': 0, '<altitudeAngle>k__BackingField': 0, '<azimuthAngle>k__BackingField': 0, '<twist>k__BackingField': 0, '<radius>k__BackingField': 0, '<radiusVariance>k__BackingField': 0, '<modifiers>k__BackingField': 0, '<UnityEngine.UIElements.IPointerEventInternal.triggeredByOS>k__BackingField': 0, '<UnityEngine.UIElements.IPointerEventInternal.recomputeTopElementUnderPointer>k__BackingField': 0}    
    def __init__(self, <pointerId>k__BackingField: System.Int32, <pointerType>k__BackingField: System.String, <isPrimary>k__BackingField: System.Boolean, <button>k__BackingField: System.Int32, <pressedButtons>k__BackingField: System.Int32, <position>k__BackingField: UnityEngine.Vector3, <localPosition>k__BackingField: UnityEngine.Vector3, <deltaPosition>k__BackingField: UnityEngine.Vector3, <deltaTime>k__BackingField: System.Single, <clickCount>k__BackingField: System.Int32, <pressure>k__BackingField: System.Single, <tangentialPressure>k__BackingField: System.Single, <altitudeAngle>k__BackingField: System.Single, <azimuthAngle>k__BackingField: System.Single, <twist>k__BackingField: System.Single, <radius>k__BackingField: UnityEngine.Vector2, <radiusVariance>k__BackingField: UnityEngine.Vector2, <modifiers>k__BackingField: UnityEngine.EventModifiers, <UnityEngine.UIElements.IPointerEventInternal.triggeredByOS>k__BackingField: System.Boolean, <UnityEngine.UIElements.IPointerEventInternal.recomputeTopElementUnderPointer>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<pointerId>k__BackingField = <pointerId>k__BackingField
		self.<pointerType>k__BackingField = <pointerType>k__BackingField
		self.<isPrimary>k__BackingField = <isPrimary>k__BackingField
		self.<button>k__BackingField = <button>k__BackingField
		self.<pressedButtons>k__BackingField = <pressedButtons>k__BackingField
		self.<position>k__BackingField = <position>k__BackingField
		self.<localPosition>k__BackingField = <localPosition>k__BackingField
		self.<deltaPosition>k__BackingField = <deltaPosition>k__BackingField
		self.<deltaTime>k__BackingField = <deltaTime>k__BackingField
		self.<clickCount>k__BackingField = <clickCount>k__BackingField
		self.<pressure>k__BackingField = <pressure>k__BackingField
		self.<tangentialPressure>k__BackingField = <tangentialPressure>k__BackingField
		self.<altitudeAngle>k__BackingField = <altitudeAngle>k__BackingField
		self.<azimuthAngle>k__BackingField = <azimuthAngle>k__BackingField
		self.<twist>k__BackingField = <twist>k__BackingField
		self.<radius>k__BackingField = <radius>k__BackingField
		self.<radiusVariance>k__BackingField = <radiusVariance>k__BackingField
		self.<modifiers>k__BackingField = <modifiers>k__BackingField
		self.<UnityEngine.UIElements.IPointerEventInternal.triggeredByOS>k__BackingField = <UnityEngine.UIElements.IPointerEventInternal.triggeredByOS>k__BackingField
		self.<UnityEngine.UIElements.IPointerEventInternal.recomputeTopElementUnderPointer>k__BackingField = <UnityEngine.UIElements.IPointerEventInternal.recomputeTopElementUnderPointer>k__BackingField


class PointerEventDispatchingStrategy:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerEventsHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerId:
	maxPointers: System.Int32
    offsets = {'maxPointers': 0, 'invalidPointerId': 4, 'mousePointerId': 8, 'touchPointerIdBase': 12, 'touchPointerCount': 16, 'penPointerIdBase': 20, 'penPointerCount': 24}    
    def __init__(self, maxPointers: System.Int32, invalidPointerId: System.Int32, mousePointerId: System.Int32, touchPointerIdBase: System.Int32, touchPointerCount: System.Int32, penPointerIdBase: System.Int32, penPointerCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.maxPointers = maxPointers
		self.invalidPointerId = invalidPointerId
		self.mousePointerId = mousePointerId
		self.touchPointerIdBase = touchPointerIdBase
		self.touchPointerCount = touchPointerCount
		self.penPointerIdBase = penPointerIdBase
		self.penPointerCount = penPointerCount


class PointerLeaveEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerMoveEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerOutEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerOverEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PointerType:
	mouse: System.String
    offsets = {'mouse': 0, 'touch': 8, 'pen': 16, 'unknown': 24}    
    def __init__(self, mouse: System.String, touch: System.String, pen: System.String, unknown: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.mouse = mouse
		self.touch = touch
		self.pen = pen
		self.unknown = unknown


class PointerUpEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PropagationPaths:
	s_Pool: UnityEngine.UIElements.ObjectPool<UnityEngine.UIElements.PropagationPaths>
    offsets = {'s_Pool': 0, 'trickleDownPath': 16, 'targetElements': 24, 'bubbleUpPath': 32}    
    def __init__(self, s_Pool: UnityEngine.UIElements.ObjectPool<UnityEngine.UIElements.PropagationPaths>, trickleDownPath: System.Collections.Generic.List<UnityEngine.UIElements.VisualElement>, targetElements: System.Collections.Generic.List<UnityEngine.UIElements.VisualElement>, bubbleUpPath: System.Collections.Generic.List<UnityEngine.UIElements.VisualElement>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Pool = s_Pool
		self.trickleDownPath = trickleDownPath
		self.targetElements = targetElements
		self.bubbleUpPath = bubbleUpPath


class PropagationPhase:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PseudoStates:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RepaintData:

    offsets = {'<currentOffset>k__BackingField': 16, '<repaintEvent>k__BackingField': 80}    
    def __init__(self, <currentOffset>k__BackingField: UnityEngine.Matrix4x4, <repaintEvent>k__BackingField: UnityEngine.Event, **kwargs):
        super().__init__(self, **kwargs)
		self.<currentOffset>k__BackingField = <currentOffset>k__BackingField
		self.<repaintEvent>k__BackingField = <repaintEvent>k__BackingField


class RuntimePanel:

    offsets = {'targetTexture': 136}    
    def __init__(self, targetTexture: UnityEngine.RenderTexture, **kwargs):
        super().__init__(self, **kwargs)
		self.targetTexture = targetTexture


class StyleColor:

    offsets = {'m_Keyword': 16, 'm_Value': 20, 'm_Specificity': 36}    
    def __init__(self, m_Keyword: UnityEngine.UIElements.StyleKeyword, m_Value: UnityEngine.Color, m_Specificity: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Keyword = m_Keyword
		self.m_Value = m_Value
		self.m_Specificity = m_Specificity


class StyleEnum<T>:

    offsets = {'m_Keyword': 0, 'm_Value': 0, 'm_Specificity': 0}    
    def __init__(self, m_Keyword: UnityEngine.UIElements.StyleKeyword, m_Value: T, m_Specificity: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Keyword = m_Keyword
		self.m_Value = m_Value
		self.m_Specificity = m_Specificity


class StyleFloat:

    offsets = {'m_Keyword': 16, 'm_Value': 20, 'm_Specificity': 24}    
    def __init__(self, m_Keyword: UnityEngine.UIElements.StyleKeyword, m_Value: System.Single, m_Specificity: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Keyword = m_Keyword
		self.m_Value = m_Value
		self.m_Specificity = m_Specificity


class StyleFont:

    offsets = {'m_Keyword': 16, 'm_Value': 24, 'm_Specificity': 32}    
    def __init__(self, m_Keyword: UnityEngine.UIElements.StyleKeyword, m_Value: UnityEngine.Font, m_Specificity: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Keyword = m_Keyword
		self.m_Value = m_Value
		self.m_Specificity = m_Specificity


class StyleInt:

    offsets = {'m_Keyword': 16, 'm_Value': 20, 'm_Specificity': 24}    
    def __init__(self, m_Keyword: UnityEngine.UIElements.StyleKeyword, m_Value: System.Int32, m_Specificity: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Keyword = m_Keyword
		self.m_Value = m_Value
		self.m_Specificity = m_Specificity


class StyleKeyword:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class StyleLength:

    offsets = {'m_Keyword': 16, 'm_Value': 20, 'm_Specificity': 28}    
    def __init__(self, m_Keyword: UnityEngine.UIElements.StyleKeyword, m_Value: UnityEngine.UIElements.Length, m_Specificity: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Keyword = m_Keyword
		self.m_Value = m_Value
		self.m_Specificity = m_Specificity


class StyleValueExtensions:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UIElementsRuntimeUtility:
	s_RuntimeDispatcher: UnityEngine.UIElements.EventDispatcher
    offsets = {'s_RuntimeDispatcher': 0, 's_RegisteredPlayerloopCallback': 8, 'panelsIteration': 16, 's_RepaintProfilerMarkerName': 24, 's_RepaintProfilerMarker': 32}    
    def __init__(self, s_RuntimeDispatcher: UnityEngine.UIElements.EventDispatcher, s_RegisteredPlayerloopCallback: System.Boolean, panelsIteration: System.Collections.Generic.List<UnityEngine.UIElements.Panel>, s_RepaintProfilerMarkerName: System.String, s_RepaintProfilerMarker: Unity.Profiling.ProfilerMarker, **kwargs):
        super().__init__(self, **kwargs)
		self.s_RuntimeDispatcher = s_RuntimeDispatcher
		self.s_RegisteredPlayerloopCallback = s_RegisteredPlayerloopCallback
		self.panelsIteration = panelsIteration
		self.s_RepaintProfilerMarkerName = s_RepaintProfilerMarkerName
		self.s_RepaintProfilerMarker = s_RepaintProfilerMarker


class UIElementsUtility:
	s_ContainerStack: System.Collections.Generic.Stack<UnityEngine.UIElements.IMGUIContainer>
    offsets = {'s_ContainerStack': 0, 's_UIElementsCache': 8, 's_EventInstance': 16, 'editorPlayModeTintColor': 24, 's_RepaintProfilerMarkerName': 40, 's_EventProfilerMarkerName': 48, 's_RepaintProfilerMarker': 56, 's_EventProfilerMarker': 64}    
    def __init__(self, s_ContainerStack: System.Collections.Generic.Stack<UnityEngine.UIElements.IMGUIContainer>, s_UIElementsCache: System.Collections.Generic.Dictionary<System.Int32,UnityEngine.UIElements.Panel>, s_EventInstance: UnityEngine.Event, editorPlayModeTintColor: UnityEngine.Color, s_RepaintProfilerMarkerName: System.String, s_EventProfilerMarkerName: System.String, s_RepaintProfilerMarker: Unity.Profiling.ProfilerMarker, s_EventProfilerMarker: Unity.Profiling.ProfilerMarker, **kwargs):
        super().__init__(self, **kwargs)
		self.s_ContainerStack = s_ContainerStack
		self.s_UIElementsCache = s_UIElementsCache
		self.s_EventInstance = s_EventInstance
		self.editorPlayModeTintColor = editorPlayModeTintColor
		self.s_RepaintProfilerMarkerName = s_RepaintProfilerMarkerName
		self.s_EventProfilerMarkerName = s_EventProfilerMarkerName
		self.s_RepaintProfilerMarker = s_RepaintProfilerMarker
		self.s_EventProfilerMarker = s_EventProfilerMarker


class ValidateCommandEvent:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VersionChangeType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Visibility:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VisualElement:
	s_EmptyClassList: System.Collections.Generic.List<System.String>
    offsets = {'s_EmptyClassList': 0, 'userDataPropertyKey': 8, 'disabledUssClassName': 16, 's_InfiniteRect': 24, 's_EmptyList': 40, '<isCompositeRoot>k__BackingField': 32, 'm_Position': 36, 'm_Rotation': 48, 'm_Scale': 64, '<isLayoutManual>k__BackingField': 76, 'm_Layout': 80, 'isBoundingBoxDirty': 96, 'm_BoundingBox': 100, 'isWorldBoundingBoxDirty': 116, 'm_WorldBoundingBox': 120, '<isWorldTransformDirty>k__BackingField': 136, '<isWorldTransformInverseDirty>k__BackingField': 137, 'm_WorldTransformCache': 140, 'm_WorldTransformInverseCache': 204, 'm_PseudoStates': 268, '<pickingMode>k__BackingField': 272, '<yogaNode>k__BackingField': 280, 'm_Style': 288, 'm_InheritedStylesData': 296, '<computedStyle>k__BackingField': 304, 'imguiContainerDescendantCount': 312, '<hierarchy>k__BackingField': 320, 'm_PhysicalParent': 328, 'm_Children': 336, '<elementPanel>k__BackingField': 344}    
    def __init__(self, s_EmptyClassList: System.Collections.Generic.List<System.String>, userDataPropertyKey: UnityEngine.PropertyName, disabledUssClassName: System.String, s_InfiniteRect: UnityEngine.Rect, s_EmptyList: System.Collections.Generic.List<UnityEngine.UIElements.VisualElement>, <isCompositeRoot>k__BackingField: System.Boolean, m_Position: UnityEngine.Vector3, m_Rotation: UnityEngine.Quaternion, m_Scale: UnityEngine.Vector3, <isLayoutManual>k__BackingField: System.Boolean, m_Layout: UnityEngine.Rect, isBoundingBoxDirty: System.Boolean, m_BoundingBox: UnityEngine.Rect, isWorldBoundingBoxDirty: System.Boolean, m_WorldBoundingBox: UnityEngine.Rect, <isWorldTransformDirty>k__BackingField: System.Boolean, <isWorldTransformInverseDirty>k__BackingField: System.Boolean, m_WorldTransformCache: UnityEngine.Matrix4x4, m_WorldTransformInverseCache: UnityEngine.Matrix4x4, m_PseudoStates: UnityEngine.UIElements.PseudoStates, <pickingMode>k__BackingField: UnityEngine.UIElements.PickingMode, <yogaNode>k__BackingField: UnityEngine.Yoga.YogaNode, m_Style: UnityEngine.UIElements.StyleSheets.VisualElementStylesData, m_InheritedStylesData: UnityEngine.UIElements.StyleSheets.InheritedStylesData, <computedStyle>k__BackingField: UnityEngine.UIElements.ComputedStyle, imguiContainerDescendantCount: System.Int32, <hierarchy>k__BackingField: UnityEngine.UIElements.VisualElement.Hierarchy, m_PhysicalParent: UnityEngine.UIElements.VisualElement, m_Children: System.Collections.Generic.List<UnityEngine.UIElements.VisualElement>, <elementPanel>k__BackingField: UnityEngine.UIElements.BaseVisualElementPanel, **kwargs):
        super().__init__(self, **kwargs)
		self.s_EmptyClassList = s_EmptyClassList
		self.userDataPropertyKey = userDataPropertyKey
		self.disabledUssClassName = disabledUssClassName
		self.s_InfiniteRect = s_InfiniteRect
		self.s_EmptyList = s_EmptyList
		self.<isCompositeRoot>k__BackingField = <isCompositeRoot>k__BackingField
		self.m_Position = m_Position
		self.m_Rotation = m_Rotation
		self.m_Scale = m_Scale
		self.<isLayoutManual>k__BackingField = <isLayoutManual>k__BackingField
		self.m_Layout = m_Layout
		self.isBoundingBoxDirty = isBoundingBoxDirty
		self.m_BoundingBox = m_BoundingBox
		self.isWorldBoundingBoxDirty = isWorldBoundingBoxDirty
		self.m_WorldBoundingBox = m_WorldBoundingBox
		self.<isWorldTransformDirty>k__BackingField = <isWorldTransformDirty>k__BackingField
		self.<isWorldTransformInverseDirty>k__BackingField = <isWorldTransformInverseDirty>k__BackingField
		self.m_WorldTransformCache = m_WorldTransformCache
		self.m_WorldTransformInverseCache = m_WorldTransformInverseCache
		self.m_PseudoStates = m_PseudoStates
		self.<pickingMode>k__BackingField = <pickingMode>k__BackingField
		self.<yogaNode>k__BackingField = <yogaNode>k__BackingField
		self.m_Style = m_Style
		self.m_InheritedStylesData = m_InheritedStylesData
		self.<computedStyle>k__BackingField = <computedStyle>k__BackingField
		self.imguiContainerDescendantCount = imguiContainerDescendantCount
		self.<hierarchy>k__BackingField = <hierarchy>k__BackingField
		self.m_PhysicalParent = m_PhysicalParent
		self.m_Children = m_Children
		self.<elementPanel>k__BackingField = <elementPanel>k__BackingField


class VisualElementExtensions:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VisualElementFocusChangeDirection:
	s_Left: UnityEngine.UIElements.VisualElementFocusChangeDirection
    offsets = {'s_Left': 0, 's_Right': 8}    
    def __init__(self, s_Left: UnityEngine.UIElements.VisualElementFocusChangeDirection, s_Right: UnityEngine.UIElements.VisualElementFocusChangeDirection, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Left = s_Left
		self.s_Right = s_Right


class VisualElementListPool:
	pool: UnityEngine.UIElements.ObjectPool<System.Collections.Generic.List<UnityEngine.UIElements.VisualElement>>
    offsets = {'pool': 0}    
    def __init__(self, pool: UnityEngine.UIElements.ObjectPool<System.Collections.Generic.List<UnityEngine.UIElements.VisualElement>>, **kwargs):
        super().__init__(self, **kwargs)
		self.pool = pool


class VisualTreeUpdatePhase:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class VisualTreeUpdater:

    offsets = {'m_UpdaterArray': 16}    
    def __init__(self, m_UpdaterArray: UnityEngine.UIElements.VisualTreeUpdater.UpdaterArray, **kwargs):
        super().__init__(self, **kwargs)
		self.m_UpdaterArray = m_UpdaterArray


class WheelEvent:

    offsets = {'<delta>k__BackingField': 184}    
    def __init__(self, <delta>k__BackingField: UnityEngine.Vector3, **kwargs):
        super().__init__(self, **kwargs)
		self.<delta>k__BackingField = <delta>k__BackingField


class InheritedStylesData:
	none: UnityEngine.UIElements.StyleSheets.InheritedStylesData
    offsets = {'none': 0, 'color': 16, 'font': 40, 'fontSize': 64, 'unityFontStyle': 80, 'unityTextAlign': 92, 'visibility': 104, 'whiteSpace': 116}    
    def __init__(self, none: UnityEngine.UIElements.StyleSheets.InheritedStylesData, color: UnityEngine.UIElements.StyleColor, font: UnityEngine.UIElements.StyleFont, fontSize: UnityEngine.UIElements.StyleLength, unityFontStyle: UnityEngine.UIElements.StyleInt, unityTextAlign: UnityEngine.UIElements.StyleInt, visibility: UnityEngine.UIElements.StyleInt, whiteSpace: UnityEngine.UIElements.StyleInt, **kwargs):
        super().__init__(self, **kwargs)
		self.none = none
		self.color = color
		self.font = font
		self.fontSize = fontSize
		self.unityFontStyle = unityFontStyle
		self.unityTextAlign = unityTextAlign
		self.visibility = visibility
		self.whiteSpace = whiteSpace


class StylePropertyID:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class StyleSheetCache:
	s_Comparer: UnityEngine.UIElements.StyleSheets.StyleSheetCache.SheetHandleKeyComparer
    offsets = {'s_Comparer': 0, 's_EnumToIntCache': 8, 's_NameToIDCache': 24, 's_DeprecatedNames': 40}    
    def __init__(self, s_Comparer: UnityEngine.UIElements.StyleSheets.StyleSheetCache.SheetHandleKeyComparer, s_EnumToIntCache: System.Collections.Generic.Dictionary<UnityEngine.UIElements.StyleSheets.StyleSheetCache.SheetHandleKey,System.Int32>, s_NameToIDCache: System.Collections.Generic.Dictionary<System.String,UnityEngine.UIElements.StyleSheets.StylePropertyID>, s_DeprecatedNames: System.Collections.Generic.Dictionary<System.String,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_Comparer = s_Comparer
		self.s_EnumToIntCache = s_EnumToIntCache
		self.s_NameToIDCache = s_NameToIDCache
		self.s_DeprecatedNames = s_DeprecatedNames


class StyleValue:

    offsets = {'id': 16, 'keyword': 20, 'number': 24, 'length': 24, 'color': 24, 'resource': 24}    
    def __init__(self, id: UnityEngine.UIElements.StyleSheets.StylePropertyID, keyword: UnityEngine.UIElements.StyleKeyword, number: System.Single, length: UnityEngine.UIElements.Length, color: UnityEngine.Color, resource: System.Runtime.InteropServices.GCHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.id = id
		self.keyword = keyword
		self.number = number
		self.length = length
		self.color = color
		self.resource = resource


class StyleValuePropertyReader:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VisualElementStylesData:
	s_StyleValuePropertyReader: UnityEngine.UIElements.StyleSheets.StyleValuePropertyReader
    offsets = {'s_StyleValuePropertyReader': 0, 'none': 8, 'isShared': 16, 'width': 20, 'height': 36, 'maxWidth': 52, 'maxHeight': 68, 'minWidth': 84, 'minHeight': 100, 'flexBasis': 116, 'flexShrink': 132, 'flexGrow': 144, 'overflow': 156, 'left': 168, 'top': 184, 'right': 200, 'bottom': 216, 'alignSelf': 232, 'color': 244, 'unityBackgroundImageTintColor': 268, 'alignItems': 292, 'alignContent': 304, 'borderLeftColor': 316, 'borderTopColor': 340, 'borderRightColor': 364, 'borderBottomColor': 388, 'opacity': 412, 'visibility': 424, 'display': 436, 'dpiScaling': 448}    
    def __init__(self, s_StyleValuePropertyReader: UnityEngine.UIElements.StyleSheets.StyleValuePropertyReader, none: UnityEngine.UIElements.StyleSheets.VisualElementStylesData, isShared: System.Boolean, width: UnityEngine.UIElements.StyleLength, height: UnityEngine.UIElements.StyleLength, maxWidth: UnityEngine.UIElements.StyleLength, maxHeight: UnityEngine.UIElements.StyleLength, minWidth: UnityEngine.UIElements.StyleLength, minHeight: UnityEngine.UIElements.StyleLength, flexBasis: UnityEngine.UIElements.StyleLength, flexShrink: UnityEngine.UIElements.StyleFloat, flexGrow: UnityEngine.UIElements.StyleFloat, overflow: UnityEngine.UIElements.StyleInt, left: UnityEngine.UIElements.StyleLength, top: UnityEngine.UIElements.StyleLength, right: UnityEngine.UIElements.StyleLength, bottom: UnityEngine.UIElements.StyleLength, alignSelf: UnityEngine.UIElements.StyleInt, color: UnityEngine.UIElements.StyleColor, unityBackgroundImageTintColor: UnityEngine.UIElements.StyleColor, alignItems: UnityEngine.UIElements.StyleInt, alignContent: UnityEngine.UIElements.StyleInt, borderLeftColor: UnityEngine.UIElements.StyleColor, borderTopColor: UnityEngine.UIElements.StyleColor, borderRightColor: UnityEngine.UIElements.StyleColor, borderBottomColor: UnityEngine.UIElements.StyleColor, opacity: UnityEngine.UIElements.StyleFloat, visibility: UnityEngine.UIElements.StyleInt, display: UnityEngine.UIElements.StyleInt, dpiScaling: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.s_StyleValuePropertyReader = s_StyleValuePropertyReader
		self.none = none
		self.isShared = isShared
		self.width = width
		self.height = height
		self.maxWidth = maxWidth
		self.maxHeight = maxHeight
		self.minWidth = minWidth
		self.minHeight = minHeight
		self.flexBasis = flexBasis
		self.flexShrink = flexShrink
		self.flexGrow = flexGrow
		self.overflow = overflow
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom
		self.alignSelf = alignSelf
		self.color = color
		self.unityBackgroundImageTintColor = unityBackgroundImageTintColor
		self.alignItems = alignItems
		self.alignContent = alignContent
		self.borderLeftColor = borderLeftColor
		self.borderTopColor = borderTopColor
		self.borderRightColor = borderRightColor
		self.borderBottomColor = borderBottomColor
		self.opacity = opacity
		self.visibility = visibility
		self.display = display
		self.dpiScaling = dpiScaling


class Utility:
	GraphicsResourcesRecreate: System.Action<System.Boolean>
    offsets = {'GraphicsResourcesRecreate': 0, 'EngineUpdate': 8, 'FlushPendingResources': 16, 's_MarkerRaiseEngineUpdate': 24}    
    def __init__(self, GraphicsResourcesRecreate: System.Action<System.Boolean>, EngineUpdate: System.Action, FlushPendingResources: System.Action, s_MarkerRaiseEngineUpdate: Unity.Profiling.ProfilerMarker, **kwargs):
        super().__init__(self, **kwargs)
		self.GraphicsResourcesRecreate = GraphicsResourcesRecreate
		self.EngineUpdate = EngineUpdate
		self.FlushPendingResources = FlushPendingResources
		self.s_MarkerRaiseEngineUpdate = s_MarkerRaiseEngineUpdate


class BaselineFunction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MeasureFunction:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Native:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class YogaMeasureMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class YogaNode:

    offsets = {'_ygNode': 16, '_measureFunction': 24, '_baselineFunction': 32}    
    def __init__(self, _ygNode: System.IntPtr, _measureFunction: UnityEngine.Yoga.MeasureFunction, _baselineFunction: UnityEngine.Yoga.BaselineFunction, **kwargs):
        super().__init__(self, **kwargs)
		self._ygNode = _ygNode
		self._measureFunction = _measureFunction
		self._baselineFunction = _baselineFunction


class YogaSize:

    offsets = {'width': 16, 'height': 20}    
    def __init__(self, width: System.Single, height: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.width = width
		self.height = height