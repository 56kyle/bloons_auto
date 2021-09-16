


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Enumerator:

    offsets = {'m_Outer': 16, 'm_CurrentIndex': 24}    
    def __init__(self, m_Outer: UnityEngine.Animation, m_CurrentIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Outer = m_Outer
		self.m_CurrentIndex = m_CurrentIndex


class OnOverrideControllerDirtyCallback:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Animation:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AnimationClip:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AnimationCullingType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AnimationEvent:

    offsets = {'m_Time': 16, 'm_FunctionName': 24, 'm_StringParameter': 32, 'm_ObjectReferenceParameter': 40, 'm_FloatParameter': 48, 'm_IntParameter': 52, 'm_MessageOptions': 56, 'm_Source': 60, 'm_StateSender': 64, 'm_AnimatorStateInfo': 72, 'm_AnimatorClipInfo': 108}    
    def __init__(self, m_Time: System.Single, m_FunctionName: System.String, m_StringParameter: System.String, m_ObjectReferenceParameter: UnityEngine.Object, m_FloatParameter: System.Single, m_IntParameter: System.Int32, m_MessageOptions: System.Int32, m_Source: UnityEngine.AnimationEventSource, m_StateSender: UnityEngine.AnimationState, m_AnimatorStateInfo: UnityEngine.AnimatorStateInfo, m_AnimatorClipInfo: UnityEngine.AnimatorClipInfo, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Time = m_Time
		self.m_FunctionName = m_FunctionName
		self.m_StringParameter = m_StringParameter
		self.m_ObjectReferenceParameter = m_ObjectReferenceParameter
		self.m_FloatParameter = m_FloatParameter
		self.m_IntParameter = m_IntParameter
		self.m_MessageOptions = m_MessageOptions
		self.m_Source = m_Source
		self.m_StateSender = m_StateSender
		self.m_AnimatorStateInfo = m_AnimatorStateInfo
		self.m_AnimatorClipInfo = m_AnimatorClipInfo


class AnimationEventSource:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AnimationPlayMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AnimationState:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Animator:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AnimatorClipInfo:

    offsets = {'m_ClipInstanceID': 16, 'm_Weight': 20}    
    def __init__(self, m_ClipInstanceID: System.Int32, m_Weight: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ClipInstanceID = m_ClipInstanceID
		self.m_Weight = m_Weight


class AnimatorControllerParameter:

    offsets = {'m_Name': 16, 'm_Type': 24, 'm_DefaultFloat': 28, 'm_DefaultInt': 32, 'm_DefaultBool': 36}    
    def __init__(self, m_Name: System.String, m_Type: UnityEngine.AnimatorControllerParameterType, m_DefaultFloat: System.Single, m_DefaultInt: System.Int32, m_DefaultBool: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Name = m_Name
		self.m_Type = m_Type
		self.m_DefaultFloat = m_DefaultFloat
		self.m_DefaultInt = m_DefaultInt
		self.m_DefaultBool = m_DefaultBool


class AnimatorControllerParameterType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AnimatorCullingMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AnimatorOverrideController:

    offsets = {'OnOverrideControllerDirty': 24}    
    def __init__(self, OnOverrideControllerDirty: UnityEngine.AnimatorOverrideController.OnOverrideControllerDirtyCallback, **kwargs):
        super().__init__(self, **kwargs)
		self.OnOverrideControllerDirty = OnOverrideControllerDirty


class AnimatorRecorderMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AnimatorStateInfo:

    offsets = {'m_Name': 16, 'm_Path': 20, 'm_FullPath': 24, 'm_NormalizedTime': 28, 'm_Length': 32, 'm_Speed': 36, 'm_SpeedMultiplier': 40, 'm_Tag': 44, 'm_Loop': 48}    
    def __init__(self, m_Name: System.Int32, m_Path: System.Int32, m_FullPath: System.Int32, m_NormalizedTime: System.Single, m_Length: System.Single, m_Speed: System.Single, m_SpeedMultiplier: System.Single, m_Tag: System.Int32, m_Loop: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Name = m_Name
		self.m_Path = m_Path
		self.m_FullPath = m_FullPath
		self.m_NormalizedTime = m_NormalizedTime
		self.m_Length = m_Length
		self.m_Speed = m_Speed
		self.m_SpeedMultiplier = m_SpeedMultiplier
		self.m_Tag = m_Tag
		self.m_Loop = m_Loop


class AnimatorTransitionInfo:

    offsets = {'m_FullPath': 16, 'm_UserName': 20, 'm_Name': 24, 'm_HasFixedDuration': 28, 'm_Duration': 32, 'm_NormalizedTime': 36, 'm_AnyState': 40, 'm_TransitionType': 44}    
    def __init__(self, m_FullPath: System.Int32, m_UserName: System.Int32, m_Name: System.Int32, m_HasFixedDuration: System.Boolean, m_Duration: System.Single, m_NormalizedTime: System.Single, m_AnyState: System.Boolean, m_TransitionType: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_FullPath = m_FullPath
		self.m_UserName = m_UserName
		self.m_Name = m_Name
		self.m_HasFixedDuration = m_HasFixedDuration
		self.m_Duration = m_Duration
		self.m_NormalizedTime = m_NormalizedTime
		self.m_AnyState = m_AnyState
		self.m_TransitionType = m_TransitionType


class AnimatorUpdateMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Avatar:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AvatarIKGoal:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AvatarIKHint:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class AvatarTarget:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class HumanBodyBones:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class HumanBone:

    offsets = {'m_BoneName': 16, 'm_HumanName': 24, 'limit': 32}    
    def __init__(self, m_BoneName: System.String, m_HumanName: System.String, limit: UnityEngine.HumanLimit, **kwargs):
        super().__init__(self, **kwargs)
		self.m_BoneName = m_BoneName
		self.m_HumanName = m_HumanName
		self.limit = limit


class HumanDescription:

    offsets = {'m_ArmTwist': 32, 'm_ForeArmTwist': 36, 'm_UpperLegTwist': 40, 'm_LegTwist': 44, 'm_ArmStretch': 48, 'm_LegStretch': 52, 'm_FeetSpacing': 56, 'm_GlobalScale': 60, 'm_RootMotionBoneName': 64, 'm_HasTranslationDoF': 72, 'm_HasExtraRoot': 73, 'm_SkeletonHasParents': 74}    
    def __init__(self, m_ArmTwist: System.Single, m_ForeArmTwist: System.Single, m_UpperLegTwist: System.Single, m_LegTwist: System.Single, m_ArmStretch: System.Single, m_LegStretch: System.Single, m_FeetSpacing: System.Single, m_GlobalScale: System.Single, m_RootMotionBoneName: System.String, m_HasTranslationDoF: System.Boolean, m_HasExtraRoot: System.Boolean, m_SkeletonHasParents: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ArmTwist = m_ArmTwist
		self.m_ForeArmTwist = m_ForeArmTwist
		self.m_UpperLegTwist = m_UpperLegTwist
		self.m_LegTwist = m_LegTwist
		self.m_ArmStretch = m_ArmStretch
		self.m_LegStretch = m_LegStretch
		self.m_FeetSpacing = m_FeetSpacing
		self.m_GlobalScale = m_GlobalScale
		self.m_RootMotionBoneName = m_RootMotionBoneName
		self.m_HasTranslationDoF = m_HasTranslationDoF
		self.m_HasExtraRoot = m_HasExtraRoot
		self.m_SkeletonHasParents = m_SkeletonHasParents


class HumanLimit:

    offsets = {'m_Min': 16, 'm_Max': 28, 'm_Center': 40, 'm_AxisLength': 52, 'm_UseDefaultValues': 56}    
    def __init__(self, m_Min: UnityEngine.Vector3, m_Max: UnityEngine.Vector3, m_Center: UnityEngine.Vector3, m_AxisLength: System.Single, m_UseDefaultValues: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Min = m_Min
		self.m_Max = m_Max
		self.m_Center = m_Center
		self.m_AxisLength = m_AxisLength
		self.m_UseDefaultValues = m_UseDefaultValues


class HumanTrait:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MatchTargetWeightMask:

    offsets = {'m_PositionXYZWeight': 16, 'm_RotationWeight': 28}    
    def __init__(self, m_PositionXYZWeight: UnityEngine.Vector3, m_RotationWeight: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_PositionXYZWeight = m_PositionXYZWeight
		self.m_RotationWeight = m_RotationWeight


class Motion:

    offsets = {'<isAnimatorMotion>k__BackingField': 24}    
    def __init__(self, <isAnimatorMotion>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<isAnimatorMotion>k__BackingField = <isAnimatorMotion>k__BackingField


class PlayMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class QueueMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RuntimeAnimatorController:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SharedBetweenAnimatorsAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SkeletonBone:

    offsets = {'name': 16, 'parentName': 24, 'position': 32, 'rotation': 44, 'scale': 60}    
    def __init__(self, name: System.String, parentName: System.String, position: UnityEngine.Vector3, rotation: UnityEngine.Quaternion, scale: UnityEngine.Vector3, **kwargs):
        super().__init__(self, **kwargs)
		self.name = name
		self.parentName = parentName
		self.position = position
		self.rotation = rotation
		self.scale = scale


class StateInfoIndex:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class StateMachineBehaviour:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AnimationClipPlayable:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class AnimationHumanStream:

    offsets = {'stream': 16}    
    def __init__(self, stream: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.stream = stream


class AnimationLayerMixerPlayable:
	m_NullPlayable: UnityEngine.Animations.AnimationLayerMixerPlayable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Animations.AnimationLayerMixerPlayable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class AnimationMixerPlayable:
	m_NullPlayable: UnityEngine.Animations.AnimationMixerPlayable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Animations.AnimationMixerPlayable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class AnimationMotionXToDeltaPlayable:
	m_NullPlayable: UnityEngine.Animations.AnimationMotionXToDeltaPlayable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Animations.AnimationMotionXToDeltaPlayable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class AnimationOffsetPlayable:
	m_NullPlayable: UnityEngine.Animations.AnimationOffsetPlayable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Animations.AnimationOffsetPlayable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class AnimationPlayableGraphExtensions:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AnimationPlayableOutput:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: UnityEngine.Playables.PlayableOutputHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class AnimationPosePlayable:
	m_NullPlayable: UnityEngine.Animations.AnimationPosePlayable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Animations.AnimationPosePlayable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class AnimationRemoveScalePlayable:
	m_NullPlayable: UnityEngine.Animations.AnimationRemoveScalePlayable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Animations.AnimationRemoveScalePlayable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class AnimationScriptPlayable:
	m_NullPlayable: UnityEngine.Animations.AnimationScriptPlayable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Animations.AnimationScriptPlayable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class AnimationStream:

    offsets = {'m_AnimatorBindingsVersion': 16, 'constant': 24, 'input': 32, 'output': 40, 'workspace': 48, 'inputStreamAccessor': 56, 'animationHandleBinder': 64}    
    def __init__(self, m_AnimatorBindingsVersion: System.UInt32, constant: System.IntPtr, input: System.IntPtr, output: System.IntPtr, workspace: System.IntPtr, inputStreamAccessor: System.IntPtr, animationHandleBinder: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_AnimatorBindingsVersion = m_AnimatorBindingsVersion
		self.constant = constant
		self.input = input
		self.output = output
		self.workspace = workspace
		self.inputStreamAccessor = inputStreamAccessor
		self.animationHandleBinder = animationHandleBinder


class AnimatorControllerPlayable:
	m_NullPlayable: UnityEngine.Animations.AnimatorControllerPlayable
    offsets = {'m_NullPlayable': 0, 'm_Handle': 16}    
    def __init__(self, m_NullPlayable: UnityEngine.Animations.AnimatorControllerPlayable, m_Handle: UnityEngine.Playables.PlayableHandle, **kwargs):
        super().__init__(self, **kwargs)
		self.m_NullPlayable = m_NullPlayable
		self.m_Handle = m_Handle


class NotKeyableAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
