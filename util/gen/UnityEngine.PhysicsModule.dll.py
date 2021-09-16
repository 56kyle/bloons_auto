


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class BoxCollider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CapsuleCollider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CharacterController:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Collider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Collision:

    offsets = {'m_Impulse': 16, 'm_RelativeVelocity': 28, 'm_Rigidbody': 40, 'm_Collider': 48, 'm_ContactCount': 56}    
    def __init__(self, m_Impulse: UnityEngine.Vector3, m_RelativeVelocity: UnityEngine.Vector3, m_Rigidbody: UnityEngine.Rigidbody, m_Collider: UnityEngine.Collider, m_ContactCount: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Impulse = m_Impulse
		self.m_RelativeVelocity = m_RelativeVelocity
		self.m_Rigidbody = m_Rigidbody
		self.m_Collider = m_Collider
		self.m_ContactCount = m_ContactCount


class ContactPoint:

    offsets = {'m_Point': 16, 'm_Normal': 28, 'm_ThisColliderInstanceID': 40, 'm_OtherColliderInstanceID': 44, 'm_Separation': 48}    
    def __init__(self, m_Point: UnityEngine.Vector3, m_Normal: UnityEngine.Vector3, m_ThisColliderInstanceID: System.Int32, m_OtherColliderInstanceID: System.Int32, m_Separation: System.Single, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Point = m_Point
		self.m_Normal = m_Normal
		self.m_ThisColliderInstanceID = m_ThisColliderInstanceID
		self.m_OtherColliderInstanceID = m_OtherColliderInstanceID
		self.m_Separation = m_Separation


class ControllerColliderHit:

    offsets = {'m_Controller': 16, 'm_Collider': 24, 'm_Point': 32, 'm_Normal': 44, 'm_MoveDirection': 56, 'm_MoveLength': 68, 'm_Push': 72}    
    def __init__(self, m_Controller: UnityEngine.CharacterController, m_Collider: UnityEngine.Collider, m_Point: UnityEngine.Vector3, m_Normal: UnityEngine.Vector3, m_MoveDirection: UnityEngine.Vector3, m_MoveLength: System.Single, m_Push: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Controller = m_Controller
		self.m_Collider = m_Collider
		self.m_Point = m_Point
		self.m_Normal = m_Normal
		self.m_MoveDirection = m_MoveDirection
		self.m_MoveLength = m_MoveLength
		self.m_Push = m_Push


class MeshCollider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MeshColliderCookingOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Physics:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class PhysicsScene:

    offsets = {'m_Handle': 16}    
    def __init__(self, m_Handle: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Handle = m_Handle


class QueryTriggerInteraction:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class RaycastHit:

    offsets = {'m_Point': 16, 'm_Normal': 28, 'm_FaceID': 40, 'm_Distance': 44, 'm_UV': 48, 'm_Collider': 56}    
    def __init__(self, m_Point: UnityEngine.Vector3, m_Normal: UnityEngine.Vector3, m_FaceID: System.UInt32, m_Distance: System.Single, m_UV: UnityEngine.Vector2, m_Collider: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Point = m_Point
		self.m_Normal = m_Normal
		self.m_FaceID = m_FaceID
		self.m_Distance = m_Distance
		self.m_UV = m_UV
		self.m_Collider = m_Collider


class Rigidbody:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SphereCollider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
