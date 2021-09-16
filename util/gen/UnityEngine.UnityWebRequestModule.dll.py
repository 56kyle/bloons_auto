


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class UnityWebRequestError:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class UnityWebRequestMethod:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class WWWForm:

    offsets = {'fieldNames': 24, 'fileNames': 32, 'types': 40, 'containsFiles': 56}    
    def __init__(self, fieldNames: System.Collections.Generic.List<System.String>, fileNames: System.Collections.Generic.List<System.String>, types: System.Collections.Generic.List<System.String>, containsFiles: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.fieldNames = fieldNames
		self.fileNames = fileNames
		self.types = types
		self.containsFiles = containsFiles


class WWWTranscoder:

    offsets = {'urlEscapeChar': 16, 'qpEscapeChar': 48}    
    def __init__(self, urlEscapeChar: System.Byte, qpEscapeChar: System.Byte, **kwargs):
        super().__init__(self, **kwargs)
		self.urlEscapeChar = urlEscapeChar
		self.qpEscapeChar = qpEscapeChar


class CertificateHandler:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class DownloadHandler:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class DownloadHandlerBuffer:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IMultipartFormSection:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MultipartFormDataSection:

    offsets = {'name': 16, 'content': 32}    
    def __init__(self, name: System.String, content: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.name = name
		self.content = content


class UnityWebRequest:

    offsets = {'m_Ptr': 16, 'm_DownloadHandler': 24, 'm_UploadHandler': 32, 'm_CertificateHandler': 40, 'm_Uri': 48, '<disposeCertificateHandlerOnDispose>k__BackingField': 56, '<disposeDownloadHandlerOnDispose>k__BackingField': 57, '<disposeUploadHandlerOnDispose>k__BackingField': 58}    
    def __init__(self, m_Ptr: System.IntPtr, m_DownloadHandler: UnityEngine.Networking.DownloadHandler, m_UploadHandler: UnityEngine.Networking.UploadHandler, m_CertificateHandler: UnityEngine.Networking.CertificateHandler, m_Uri: System.Uri, <disposeCertificateHandlerOnDispose>k__BackingField: System.Boolean, <disposeDownloadHandlerOnDispose>k__BackingField: System.Boolean, <disposeUploadHandlerOnDispose>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr
		self.m_DownloadHandler = m_DownloadHandler
		self.m_UploadHandler = m_UploadHandler
		self.m_CertificateHandler = m_CertificateHandler
		self.m_Uri = m_Uri
		self.<disposeCertificateHandlerOnDispose>k__BackingField = <disposeCertificateHandlerOnDispose>k__BackingField
		self.<disposeDownloadHandlerOnDispose>k__BackingField = <disposeDownloadHandlerOnDispose>k__BackingField
		self.<disposeUploadHandlerOnDispose>k__BackingField = <disposeUploadHandlerOnDispose>k__BackingField


class UnityWebRequestAsyncOperation:

    offsets = {'<webRequest>k__BackingField': 32}    
    def __init__(self, <webRequest>k__BackingField: UnityEngine.Networking.UnityWebRequest, **kwargs):
        super().__init__(self, **kwargs)
		self.<webRequest>k__BackingField = <webRequest>k__BackingField


class UploadHandler:

    offsets = {'m_Ptr': 16}    
    def __init__(self, m_Ptr: System.IntPtr, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Ptr = m_Ptr


class UploadHandlerRaw:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class WebRequestUtils:
	domainRegex: System.Text.RegularExpressions.Regex
    offsets = {'domainRegex': 0}    
    def __init__(self, domainRegex: System.Text.RegularExpressions.Regex, **kwargs):
        super().__init__(self, **kwargs)
		self.domainRegex = domainRegex