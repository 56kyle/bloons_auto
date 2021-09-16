


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AssetFileNameExtensionAttribute:

    offsets = {'<preferredExtension>k__BackingField': 16, '<otherExtensions>k__BackingField': 24}    
    def __init__(self, <preferredExtension>k__BackingField: System.String, <otherExtensions>k__BackingField: System.Collections.Generic.IEnumerable<System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.<preferredExtension>k__BackingField = <preferredExtension>k__BackingField
		self.<otherExtensions>k__BackingField = <otherExtensions>k__BackingField


class NativeClassAttribute:

    offsets = {'<QualifiedNativeName>k__BackingField': 16, '<Declaration>k__BackingField': 24}    
    def __init__(self, <QualifiedNativeName>k__BackingField: System.String, <Declaration>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<QualifiedNativeName>k__BackingField = <QualifiedNativeName>k__BackingField
		self.<Declaration>k__BackingField = <Declaration>k__BackingField


class ThreadAndSerializationSafeAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityEngineModuleAssembly:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityString:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WritableAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CodegenOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class FreeFunctionAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IgnoreAttribute:

    offsets = {'<DoesNotContributeToSize>k__BackingField': 16}    
    def __init__(self, <DoesNotContributeToSize>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<DoesNotContributeToSize>k__BackingField = <DoesNotContributeToSize>k__BackingField


class NativeAsStructAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NativeConditionalAttribute:

    offsets = {'<Condition>k__BackingField': 16, '<Enabled>k__BackingField': 24}    
    def __init__(self, <Condition>k__BackingField: System.String, <Enabled>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<Condition>k__BackingField = <Condition>k__BackingField
		self.<Enabled>k__BackingField = <Enabled>k__BackingField


class NativeHeaderAttribute:

    offsets = {'<Header>k__BackingField': 16}    
    def __init__(self, <Header>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Header>k__BackingField = <Header>k__BackingField


class NativeMethodAttribute:

    offsets = {'<Name>k__BackingField': 16, '<IsThreadSafe>k__BackingField': 24, '<IsFreeFunction>k__BackingField': 25, '<ThrowsException>k__BackingField': 26, '<HasExplicitThis>k__BackingField': 27}    
    def __init__(self, <Name>k__BackingField: System.String, <IsThreadSafe>k__BackingField: System.Boolean, <IsFreeFunction>k__BackingField: System.Boolean, <ThrowsException>k__BackingField: System.Boolean, <HasExplicitThis>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<Name>k__BackingField = <Name>k__BackingField
		self.<IsThreadSafe>k__BackingField = <IsThreadSafe>k__BackingField
		self.<IsFreeFunction>k__BackingField = <IsFreeFunction>k__BackingField
		self.<ThrowsException>k__BackingField = <ThrowsException>k__BackingField
		self.<HasExplicitThis>k__BackingField = <HasExplicitThis>k__BackingField


class NativeNameAttribute:

    offsets = {'<Name>k__BackingField': 16}    
    def __init__(self, <Name>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Name>k__BackingField = <Name>k__BackingField


class NativePropertyAttribute:

    offsets = {'<TargetType>k__BackingField': 32}    
    def __init__(self, <TargetType>k__BackingField: UnityEngine.Bindings.TargetType, **kwargs):
        super().__init__(self, **kwargs)
		self.<TargetType>k__BackingField = <TargetType>k__BackingField


class NativeThrowsAttribute:

    offsets = {'<ThrowsException>k__BackingField': 16}    
    def __init__(self, <ThrowsException>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<ThrowsException>k__BackingField = <ThrowsException>k__BackingField


class NativeTypeAttribute:

    offsets = {'<Header>k__BackingField': 16, '<IntermediateScriptingStructName>k__BackingField': 24, '<CodegenOptions>k__BackingField': 32}    
    def __init__(self, <Header>k__BackingField: System.String, <IntermediateScriptingStructName>k__BackingField: System.String, <CodegenOptions>k__BackingField: UnityEngine.Bindings.CodegenOptions, **kwargs):
        super().__init__(self, **kwargs)
		self.<Header>k__BackingField = <Header>k__BackingField
		self.<IntermediateScriptingStructName>k__BackingField = <IntermediateScriptingStructName>k__BackingField
		self.<CodegenOptions>k__BackingField = <CodegenOptions>k__BackingField


class NativeWritableSelfAttribute:

    offsets = {'<WritableSelf>k__BackingField': 16}    
    def __init__(self, <WritableSelf>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<WritableSelf>k__BackingField = <WritableSelf>k__BackingField


class NotNullAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class StaticAccessorAttribute:

    offsets = {'<Name>k__BackingField': 16, '<Type>k__BackingField': 24}    
    def __init__(self, <Name>k__BackingField: System.String, <Type>k__BackingField: UnityEngine.Bindings.StaticAccessorType, **kwargs):
        super().__init__(self, **kwargs)
		self.<Name>k__BackingField = <Name>k__BackingField
		self.<Type>k__BackingField = <Type>k__BackingField


class StaticAccessorType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class TargetType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ThreadSafeAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnmarshalledAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class VisibleToOtherModulesAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GeneratedByOldBindingsGeneratorAttribute:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class RequiredByNativeCodeAttribute:

    offsets = {'<Name>k__BackingField': 16, '<Optional>k__BackingField': 24, '<GenerateProxy>k__BackingField': 25}    
    def __init__(self, <Name>k__BackingField: System.String, <Optional>k__BackingField: System.Boolean, <GenerateProxy>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.<Name>k__BackingField = <Name>k__BackingField
		self.<Optional>k__BackingField = <Optional>k__BackingField
		self.<GenerateProxy>k__BackingField = <GenerateProxy>k__BackingField


class UsedByNativeCodeAttribute:

    offsets = {'<Name>k__BackingField': 16}    
    def __init__(self, <Name>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Name>k__BackingField = <Name>k__BackingField