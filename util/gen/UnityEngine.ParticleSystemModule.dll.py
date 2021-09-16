


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CollisionModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class ColorBySpeedModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class ColorOverLifetimeModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class CustomDataModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class EmissionModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class EmitParams:

    offsets = {'m_Particle': 16, 'm_PositionSet': 148, 'm_VelocitySet': 149, 'm_AxisOfRotationSet': 150, 'm_RotationSet': 151, 'm_AngularVelocitySet': 152, 'm_StartSizeSet': 153, 'm_StartColorSet': 154, 'm_RandomSeedSet': 155, 'm_StartLifetimeSet': 156, 'm_MeshIndexSet': 157, 'm_ApplyShapeToPosition': 158}    
    def __init__(self, m_Particle: UnityEngine.ParticleSystem.Particle, m_PositionSet: System.Boolean, m_VelocitySet: System.Boolean, m_AxisOfRotationSet: System.Boolean, m_RotationSet: System.Boolean, m_AngularVelocitySet: System.Boolean, m_StartSizeSet: System.Boolean, m_StartColorSet: System.Boolean, m_RandomSeedSet: System.Boolean, m_StartLifetimeSet: System.Boolean, m_MeshIndexSet: System.Boolean, m_ApplyShapeToPosition: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Particle = m_Particle
		self.m_PositionSet = m_PositionSet
		self.m_VelocitySet = m_VelocitySet
		self.m_AxisOfRotationSet = m_AxisOfRotationSet
		self.m_RotationSet = m_RotationSet
		self.m_AngularVelocitySet = m_AngularVelocitySet
		self.m_StartSizeSet = m_StartSizeSet
		self.m_StartColorSet = m_StartColorSet
		self.m_RandomSeedSet = m_RandomSeedSet
		self.m_StartLifetimeSet = m_StartLifetimeSet
		self.m_MeshIndexSet = m_MeshIndexSet
		self.m_ApplyShapeToPosition = m_ApplyShapeToPosition


class ExternalForcesModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class ForceOverLifetimeModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class InheritVelocityModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class LightsModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class LimitVelocityOverLifetimeModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class MainModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class MinMaxCurve:

    offsets = {'m_Mode': 16, 'm_CurveMultiplier': 20, 'm_CurveMin': 24, 'm_CurveMax': 32, 'm_ConstantMin': 40, 'm_ConstantMax': 44}    
    def __init__(self, m_Mode: UnityEngine.ParticleSystemCurveMode, m_CurveMultiplier: System.Single, m_CurveMin: UnityEngine.AnimationCurve, m_CurveMax: UnityEngine.AnimationCurve, m_ConstantMin: System.Single, m_ConstantMax: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Mode = m_Mode
		self.m_CurveMultiplier = m_CurveMultiplier
		self.m_CurveMin = m_CurveMin
		self.m_CurveMax = m_CurveMax
		self.m_ConstantMin = m_ConstantMin
		self.m_ConstantMax = m_ConstantMax


class MinMaxGradient:

    offsets = {'m_Mode': 16, 'm_GradientMin': 24, 'm_GradientMax': 32, 'm_ColorMin': 40, 'm_ColorMax': 56}    
    def __init__(self, m_Mode: UnityEngine.ParticleSystemGradientMode, m_GradientMin: UnityEngine.Gradient, m_GradientMax: UnityEngine.Gradient, m_ColorMin: UnityEngine.Color, m_ColorMax: UnityEngine.Color, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Mode = m_Mode
		self.m_GradientMin = m_GradientMin
		self.m_GradientMax = m_GradientMax
		self.m_ColorMin = m_ColorMin
		self.m_ColorMax = m_ColorMax


class NoiseModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class Particle:

    offsets = {'m_Position': 16, 'm_Velocity': 28, 'm_AnimatedVelocity': 40, 'm_InitialVelocity': 52, 'm_AxisOfRotation': 64, 'm_Rotation': 76, 'm_AngularVelocity': 88, 'm_StartSize': 100, 'm_StartColor': 112, 'm_RandomSeed': 116, 'm_ParentRandomSeed': 120, 'm_Lifetime': 124, 'm_StartLifetime': 128, 'm_MeshIndex': 132, 'm_EmitAccumulator0': 136, 'm_EmitAccumulator1': 140, 'm_Flags': 144}    
    def __init__(self, m_Position: UnityEngine.Vector3, m_Velocity: UnityEngine.Vector3, m_AnimatedVelocity: UnityEngine.Vector3, m_InitialVelocity: UnityEngine.Vector3, m_AxisOfRotation: UnityEngine.Vector3, m_Rotation: UnityEngine.Vector3, m_AngularVelocity: UnityEngine.Vector3, m_StartSize: UnityEngine.Vector3, m_StartColor: UnityEngine.Color32, m_RandomSeed: System.UInt32, m_ParentRandomSeed: System.UInt32, m_Lifetime: System.Single, m_StartLifetime: System.Single, m_MeshIndex: System.Int32, m_EmitAccumulator0: System.Single, m_EmitAccumulator1: System.Single, m_Flags: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Position = m_Position
		self.m_Velocity = m_Velocity
		self.m_AnimatedVelocity = m_AnimatedVelocity
		self.m_InitialVelocity = m_InitialVelocity
		self.m_AxisOfRotation = m_AxisOfRotation
		self.m_Rotation = m_Rotation
		self.m_AngularVelocity = m_AngularVelocity
		self.m_StartSize = m_StartSize
		self.m_StartColor = m_StartColor
		self.m_RandomSeed = m_RandomSeed
		self.m_ParentRandomSeed = m_ParentRandomSeed
		self.m_Lifetime = m_Lifetime
		self.m_StartLifetime = m_StartLifetime
		self.m_MeshIndex = m_MeshIndex
		self.m_EmitAccumulator0 = m_EmitAccumulator0
		self.m_EmitAccumulator1 = m_EmitAccumulator1
		self.m_Flags = m_Flags


class PlaybackState:

    offsets = {'m_AccumulatedDt': 16, 'm_StartDelay': 20, 'm_PlaybackTime': 24, 'm_RingBufferIndex': 28, 'm_Emission': 32, 'm_Initial': 56, 'm_Shape': 120, 'm_Force': 212, 'm_Collision': 276, 'm_Noise': 340, 'm_Lights': 344, 'm_Trail': 364}    
    def __init__(self, m_AccumulatedDt: System.Single, m_StartDelay: System.Single, m_PlaybackTime: System.Single, m_RingBufferIndex: System.Int32, m_Emission: UnityEngine.ParticleSystem.PlaybackState.Emission, m_Initial: UnityEngine.ParticleSystem.PlaybackState.Initial, m_Shape: UnityEngine.ParticleSystem.PlaybackState.Shape, m_Force: UnityEngine.ParticleSystem.PlaybackState.Force, m_Collision: UnityEngine.ParticleSystem.PlaybackState.Collision, m_Noise: UnityEngine.ParticleSystem.PlaybackState.Noise, m_Lights: UnityEngine.ParticleSystem.PlaybackState.Lights, m_Trail: UnityEngine.ParticleSystem.PlaybackState.Trail, **kwargs):
        super().__init__(self, **kwargs)
		self.m_AccumulatedDt = m_AccumulatedDt
		self.m_StartDelay = m_StartDelay
		self.m_PlaybackTime = m_PlaybackTime
		self.m_RingBufferIndex = m_RingBufferIndex
		self.m_Emission = m_Emission
		self.m_Initial = m_Initial
		self.m_Shape = m_Shape
		self.m_Force = m_Force
		self.m_Collision = m_Collision
		self.m_Noise = m_Noise
		self.m_Lights = m_Lights
		self.m_Trail = m_Trail


class Collision:

    offsets = {'m_Random': 16}    
    def __init__(self, m_Random: UnityEngine.ParticleSystem.PlaybackState.Seed4, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Random = m_Random


class Emission:

    offsets = {'m_ParticleSpacing': 16, 'm_ToEmitAccumulator': 20, 'm_Random': 24}    
    def __init__(self, m_ParticleSpacing: System.Single, m_ToEmitAccumulator: System.Single, m_Random: UnityEngine.ParticleSystem.PlaybackState.Seed, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSpacing = m_ParticleSpacing
		self.m_ToEmitAccumulator = m_ToEmitAccumulator
		self.m_Random = m_Random


class Force:

    offsets = {'m_Random': 16}    
    def __init__(self, m_Random: UnityEngine.ParticleSystem.PlaybackState.Seed4, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Random = m_Random


class Initial:

    offsets = {'m_Random': 16}    
    def __init__(self, m_Random: UnityEngine.ParticleSystem.PlaybackState.Seed4, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Random = m_Random


class Lights:

    offsets = {'m_Random': 16, 'm_ParticleEmissionCounter': 32}    
    def __init__(self, m_Random: UnityEngine.ParticleSystem.PlaybackState.Seed, m_ParticleEmissionCounter: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Random = m_Random
		self.m_ParticleEmissionCounter = m_ParticleEmissionCounter


class Noise:

    offsets = {'m_ScrollOffset': 16}    
    def __init__(self, m_ScrollOffset: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ScrollOffset = m_ScrollOffset


class Seed:

    offsets = {'x': 16, 'y': 20, 'z': 24, 'w': 28}    
    def __init__(self, x: System.UInt32, y: System.UInt32, z: System.UInt32, w: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.x = x
		self.y = y
		self.z = z
		self.w = w


class Seed4:

    offsets = {'x': 16, 'y': 32, 'z': 48, 'w': 64}    
    def __init__(self, x: UnityEngine.ParticleSystem.PlaybackState.Seed, y: UnityEngine.ParticleSystem.PlaybackState.Seed, z: UnityEngine.ParticleSystem.PlaybackState.Seed, w: UnityEngine.ParticleSystem.PlaybackState.Seed, **kwargs):
        super().__init__(self, **kwargs)
		self.x = x
		self.y = y
		self.z = z
		self.w = w


class Shape:

    offsets = {'m_Random': 16, 'm_RadiusTimer': 80, 'm_RadiusTimerPrev': 84, 'm_ArcTimer': 88, 'm_ArcTimerPrev': 92, 'm_MeshSpawnTimer': 96, 'm_MeshSpawnTimerPrev': 100, 'm_OrderedMeshVertexIndex': 104}    
    def __init__(self, m_Random: UnityEngine.ParticleSystem.PlaybackState.Seed4, m_RadiusTimer: System.Single, m_RadiusTimerPrev: System.Single, m_ArcTimer: System.Single, m_ArcTimerPrev: System.Single, m_MeshSpawnTimer: System.Single, m_MeshSpawnTimerPrev: System.Single, m_OrderedMeshVertexIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Random = m_Random
		self.m_RadiusTimer = m_RadiusTimer
		self.m_RadiusTimerPrev = m_RadiusTimerPrev
		self.m_ArcTimer = m_ArcTimer
		self.m_ArcTimerPrev = m_ArcTimerPrev
		self.m_MeshSpawnTimer = m_MeshSpawnTimer
		self.m_MeshSpawnTimerPrev = m_MeshSpawnTimerPrev
		self.m_OrderedMeshVertexIndex = m_OrderedMeshVertexIndex


class Trail:

    offsets = {'m_Timer': 16}    
    def __init__(self, m_Timer: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Timer = m_Timer


class RotationBySpeedModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class RotationOverLifetimeModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class ShapeModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class SizeBySpeedModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class SizeOverLifetimeModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class SubEmittersModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class TextureSheetAnimationModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class TrailModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class Trails:

    offsets = {'positions': 16, 'frontPositions': 24, 'backPositions': 32, 'positionCounts': 40, 'maxTrailCount': 48, 'maxPositionsPerTrailCount': 52}    
    def __init__(self, positions: System.Collections.Generic.List<UnityEngine.Vector4>, frontPositions: System.Collections.Generic.List<System.Int32>, backPositions: System.Collections.Generic.List<System.Int32>, positionCounts: System.Collections.Generic.List<System.Int32>, maxTrailCount: System.Int32, maxPositionsPerTrailCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.positions = positions
		self.frontPositions = frontPositions
		self.backPositions = backPositions
		self.positionCounts = positionCounts
		self.maxTrailCount = maxTrailCount
		self.maxPositionsPerTrailCount = maxPositionsPerTrailCount


class TriggerModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class VelocityOverLifetimeModule:

    offsets = {'m_ParticleSystem': 16}    
    def __init__(self, m_ParticleSystem: UnityEngine.ParticleSystem, **kwargs):
        super().__init__(self, **kwargs)
		self.m_ParticleSystem = m_ParticleSystem


class Array3:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Array4:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ParticleSystem:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ParticleSystemCurveMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemCustomData:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemGradientMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemRenderMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemRenderSpace:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemRenderer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ParticleSystemScalingMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemSimulationSpace:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemSortMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemStopBehavior:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemVertexStream:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ParticleSystemVertexStreams:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class NativeParticleData:

    offsets = {'count': 16, 'positions': 24, 'velocities': 48, 'rotations': 72, 'rotationalSpeeds': 96, 'sizes': 120, 'customData1': 176, 'customData2': 208}    
    def __init__(self, count: System.Int32, positions: UnityEngine.ParticleSystemJobs.NativeParticleData.Array3, velocities: UnityEngine.ParticleSystemJobs.NativeParticleData.Array3, rotations: UnityEngine.ParticleSystemJobs.NativeParticleData.Array3, rotationalSpeeds: UnityEngine.ParticleSystemJobs.NativeParticleData.Array3, sizes: UnityEngine.ParticleSystemJobs.NativeParticleData.Array3, customData1: UnityEngine.ParticleSystemJobs.NativeParticleData.Array4, customData2: UnityEngine.ParticleSystemJobs.NativeParticleData.Array4, **kwargs):
        super().__init__(self, **kwargs)
		self.count = count
		self.positions = positions
		self.velocities = velocities
		self.rotations = rotations
		self.rotationalSpeeds = rotationalSpeeds
		self.sizes = sizes
		self.customData1 = customData1
		self.customData2 = customData2