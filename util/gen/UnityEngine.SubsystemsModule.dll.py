


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ISubsystem:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ISubsystemDescriptor:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ISubsystemDescriptorImpl:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IntegratedSubsystem:

    offsets = {'m_Ptr': 16, 'm_subsystemDescriptor': 24}    
    def __init__(self, m_Ptr: System.IntPtr, m_subsystemDescriptor: UnityEngine.ISubsystemDescriptor, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_subsystemDescriptor = m_subsystemDescriptor


class IntegratedSubsystem<TSubsystemDescriptor>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IntegratedSubsystemDescriptor:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class IntegratedSubsystemDescriptor<TSubsystem>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Internal_SubsystemDescriptors:
	s_IntegratedSubsystemDescriptors: System.Collections.Generic.List<UnityEngine.ISubsystemDescriptorImpl>
    offsets = {'s_IntegratedSubsystemDescriptors': 0, 's_StandaloneSubsystemDescriptors': 8}    
    def __init__(self, s_IntegratedSubsystemDescriptors: System.Collections.Generic.List<UnityEngine.ISubsystemDescriptorImpl>, s_StandaloneSubsystemDescriptors: System.Collections.Generic.List<UnityEngine.ISubsystemDescriptor>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_IntegratedSubsystemDescriptors = s_IntegratedSubsystemDescriptors
		self.s_StandaloneSubsystemDescriptors = s_StandaloneSubsystemDescriptors


class Internal_SubsystemInstances:
	s_IntegratedSubsystemInstances: System.Collections.Generic.List<UnityEngine.ISubsystem>
    offsets = {'s_IntegratedSubsystemInstances': 0, 's_StandaloneSubsystemInstances': 8}    
    def __init__(self, s_IntegratedSubsystemInstances: System.Collections.Generic.List<UnityEngine.ISubsystem>, s_StandaloneSubsystemInstances: System.Collections.Generic.List<UnityEngine.ISubsystem>, **kwargs):
        super().__init__(self, **kwargs)
		self.s_IntegratedSubsystemInstances = s_IntegratedSubsystemInstances
		self.s_StandaloneSubsystemInstances = s_StandaloneSubsystemInstances


class SubsystemDescriptor:

    offsets = {'<id>k__BackingField': 16}    
    def __init__(self, <id>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<id>k__BackingField = <id>k__BackingField


class SubsystemManager:
	reloadSubsytemsStarted: System.Action
    offsets = {'reloadSubsytemsStarted': 0, 'reloadSubsytemsCompleted': 8}    
    def __init__(self, reloadSubsytemsStarted: System.Action, reloadSubsytemsCompleted: System.Action, **kwargs):
        super().__init__(self, **kwargs)
		self.reloadSubsytemsStarted = reloadSubsytemsStarted
		self.reloadSubsytemsCompleted = reloadSubsytemsCompleted