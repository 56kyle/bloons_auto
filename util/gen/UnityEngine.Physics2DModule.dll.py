


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Collider2D:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Collision2D:

    offsets = {'m_Collider': 16, 'm_OtherCollider': 20, 'm_Rigidbody': 24, 'm_OtherRigidbody': 28, 'm_RelativeVelocity': 32, 'm_Enabled': 40, 'm_ContactCount': 44}    
    def __init__(self, m_Collider: System.Int32, m_OtherCollider: System.Int32, m_Rigidbody: System.Int32, m_OtherRigidbody: System.Int32, m_RelativeVelocity: UnityEngine.Vector2, m_Enabled: System.Int32, m_ContactCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Collider = m_Collider
		self.m_OtherCollider = m_OtherCollider
		self.m_Rigidbody = m_Rigidbody
		self.m_OtherRigidbody = m_OtherRigidbody
		self.m_RelativeVelocity = m_RelativeVelocity
		self.m_Enabled = m_Enabled
		self.m_ContactCount = m_ContactCount


class ContactFilter2D:

    offsets = {'useTriggers': 16, 'useLayerMask': 17, 'useDepth': 18, 'useOutsideDepth': 19, 'useNormalAngle': 20, 'useOutsideNormalAngle': 21, 'layerMask': 24, 'minDepth': 28, 'maxDepth': 32, 'minNormalAngle': 36, 'maxNormalAngle': 40}    
    def __init__(self, useTriggers: System.Boolean, useLayerMask: System.Boolean, useDepth: System.Boolean, useOutsideDepth: System.Boolean, useNormalAngle: System.Boolean, useOutsideNormalAngle: System.Boolean, layerMask: UnityEngine.LayerMask, minDepth: System.Single, maxDepth: System.Single, minNormalAngle: System.Single, maxNormalAngle: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.useTriggers = useTriggers
		self.useLayerMask = useLayerMask
		self.useDepth = useDepth
		self.useOutsideDepth = useOutsideDepth
		self.useNormalAngle = useNormalAngle
		self.useOutsideNormalAngle = useOutsideNormalAngle
		self.layerMask = layerMask
		self.minDepth = minDepth
		self.maxDepth = maxDepth
		self.minNormalAngle = minNormalAngle
		self.maxNormalAngle = maxNormalAngle


class ContactPoint2D:

    offsets = {'m_Point': 16, 'm_Normal': 24, 'm_RelativeVelocity': 32, 'm_Separation': 40, 'm_NormalImpulse': 44, 'm_TangentImpulse': 48, 'm_Collider': 52, 'm_OtherCollider': 56, 'm_Rigidbody': 60, 'm_OtherRigidbody': 64, 'm_Enabled': 68}    
    def __init__(self, m_Point: UnityEngine.Vector2, m_Normal: UnityEngine.Vector2, m_RelativeVelocity: UnityEngine.Vector2, m_Separation: System.Single, m_NormalImpulse: System.Single, m_TangentImpulse: System.Single, m_Collider: System.Int32, m_OtherCollider: System.Int32, m_Rigidbody: System.Int32, m_OtherRigidbody: System.Int32, m_Enabled: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Point = m_Point
		self.m_Normal = m_Normal
		self.m_RelativeVelocity = m_RelativeVelocity
		self.m_Separation = m_Separation
		self.m_NormalImpulse = m_NormalImpulse
		self.m_TangentImpulse = m_TangentImpulse
		self.m_Collider = m_Collider
		self.m_OtherCollider = m_OtherCollider
		self.m_Rigidbody = m_Rigidbody
		self.m_OtherRigidbody = m_OtherRigidbody
		self.m_Enabled = m_Enabled


class Physics2D:
	m_LastDisabledRigidbody2D: System.Collections.Generic.List<UnityEngine.Rigidbody2D>
    offsets = {'m_LastDisabledRigidbody2D': 0}    
    def __init__(self, m_LastDisabledRigidbody2D: System.Collections.Generic.List<UnityEngine.Rigidbody2D>, **kwargs):
        super().__init__(self, **kwargs)
		self.m_LastDisabledRigidbody2D = m_LastDisabledRigidbody2D


class PhysicsScene2D:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class RaycastHit2D:

    offsets = {'m_Centroid': 16, 'm_Point': 24, 'm_Normal': 32, 'm_Distance': 40, 'm_Fraction': 44, 'm_Collider': 48}    
    def __init__(self, m_Centroid: UnityEngine.Vector2, m_Point: UnityEngine.Vector2, m_Normal: UnityEngine.Vector2, m_Distance: System.Single, m_Fraction: System.Single, m_Collider: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Centroid = m_Centroid
		self.m_Point = m_Point
		self.m_Normal = m_Normal
		self.m_Distance = m_Distance
		self.m_Fraction = m_Fraction
		self.m_Collider = m_Collider


class Rigidbody2D:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
