


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AndroidJNI:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AndroidJNIHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AndroidJNISafe:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AndroidJavaClass:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AndroidJavaException:

    offsets = {'mJavaStackTrace': 136}    
    def __init__(self, mJavaStackTrace: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.mJavaStackTrace = mJavaStackTrace


class AndroidJavaObject:
	enableDebugPrints: System.Boolean
    offsets = {'enableDebugPrints': 0, 'm_jobject': 16, 'm_jclass': 24}    
    def __init__(self, enableDebugPrints: System.Boolean, m_jobject: UnityEngine.GlobalJavaObjectRef, m_jclass: UnityEngine.GlobalJavaObjectRef, **kwargs):
        super().__init__(self, **kwargs)
		self.enableDebugPrints = enableDebugPrints
		self.m_jobject = m_jobject
		self.m_jclass = m_jclass


class AndroidJavaProxy:
	s_JavaLangSystemClass: UnityEngine.GlobalJavaObjectRef
    offsets = {'s_JavaLangSystemClass': 0, 's_HashCodeMethodID': 8, 'javaInterface': 16, 'proxyObject': 24}    
    def __init__(self, s_JavaLangSystemClass: UnityEngine.GlobalJavaObjectRef, s_HashCodeMethodID: System.IntPtr, javaInterface: UnityEngine.AndroidJavaClass, proxyObject: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.s_JavaLangSystemClass = s_JavaLangSystemClass
		self.s_HashCodeMethodID = s_HashCodeMethodID
		self.javaInterface = javaInterface
		self.proxyObject = proxyObject


class AndroidJavaRunnable:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AndroidJavaRunnableProxy:

    offsets = {'mRunnable': 32}    
    def __init__(self, mRunnable: UnityEngine.AndroidJavaRunnable, **kwargs):
        super().__init__(self, **kwargs)
		self.mRunnable = mRunnable


class AndroidReflection:
	s_ReflectionHelperClass: UnityEngine.GlobalJavaObjectRef
    offsets = {'s_ReflectionHelperClass': 0, 's_ReflectionHelperGetConstructorID': 8, 's_ReflectionHelperGetMethodID': 16, 's_ReflectionHelperGetFieldID': 24, 's_ReflectionHelperGetFieldSignature': 32, 's_ReflectionHelperNewProxyInstance': 40, 's_ReflectionHelperSetNativeExceptionOnProxy': 48, 's_FieldGetDeclaringClass': 56}    
    def __init__(self, s_ReflectionHelperClass: UnityEngine.GlobalJavaObjectRef, s_ReflectionHelperGetConstructorID: System.IntPtr, s_ReflectionHelperGetMethodID: System.IntPtr, s_ReflectionHelperGetFieldID: System.IntPtr, s_ReflectionHelperGetFieldSignature: System.IntPtr, s_ReflectionHelperNewProxyInstance: System.IntPtr, s_ReflectionHelperSetNativeExceptionOnProxy: System.IntPtr, s_FieldGetDeclaringClass: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.s_ReflectionHelperClass = s_ReflectionHelperClass
		self.s_ReflectionHelperGetConstructorID = s_ReflectionHelperGetConstructorID
		self.s_ReflectionHelperGetMethodID = s_ReflectionHelperGetMethodID
		self.s_ReflectionHelperGetFieldID = s_ReflectionHelperGetFieldID
		self.s_ReflectionHelperGetFieldSignature = s_ReflectionHelperGetFieldSignature
		self.s_ReflectionHelperNewProxyInstance = s_ReflectionHelperNewProxyInstance
		self.s_ReflectionHelperSetNativeExceptionOnProxy = s_ReflectionHelperSetNativeExceptionOnProxy
		self.s_FieldGetDeclaringClass = s_FieldGetDeclaringClass


class GlobalJavaObjectRef:

    offsets = {'m_disposed': 16, 'm_jobject': 24}    
    def __init__(self, m_disposed: System.Boolean, m_jobject: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_disposed = m_disposed
		self.m_jobject = m_jobject


class _AndroidJNIHelper:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class jvalue:

    offsets = {'z': 16, 'b': 16, 'c': 16, 's': 16, 'i': 16, 'j': 16, 'f': 16, 'd': 16, 'l': 16}    
    def __init__(self, z: System.Boolean, b: System.SByte, c: System.Char, s: System.Int16, i: System.Int32, j: System.Int64, f: System.Single, d: System.Double, l: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.z = z
		self.b = b
		self.c = c
		self.s = s
		self.i = i
		self.j = j
		self.f = f
		self.d = d
		self.l = l