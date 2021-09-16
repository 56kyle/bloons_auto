


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <PrivateImplementationDetails>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NamespaceDeclaration:

    offsets = {'prefix': 16, 'ns': 24, 'scope': 32, 'prev': 40}    
    def __init__(self, prefix: System.String, ns: System.Xml.Linq.XNamespace, scope: System.Int32, prev: System.Xml.Linq.NamespaceResolver.NamespaceDeclaration, **kwargs):
        super().__init__(self, **kwargs)
		self.prefix = prefix
		self.ns = ns
		self.scope = scope
		self.prev = prev


class <Nodes>d__18:

    offsets = {'<>1__state': 16, '<>2__current': 24, '<>l__initialThreadId': 32, '<>4__this': 40, '<n>5__1': 48}    
    def __init__(self, <>1__state: System.Int32, <>2__current: System.Xml.Linq.XNode, <>l__initialThreadId: System.Int32, <>4__this: System.Xml.Linq.XContainer, <n>5__1: System.Xml.Linq.XNode, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.<>4__this = <>4__this
		self.<n>5__1 = <n>5__1


class <GetAttributes>d__105:

    offsets = {'<>1__state': 16, '<>2__current': 24, '<>l__initialThreadId': 32, '<>4__this': 40, '<a>5__1': 48, 'name': 56, '<>3__name': 64}    
    def __init__(self, <>1__state: System.Int32, <>2__current: System.Xml.Linq.XAttribute, <>l__initialThreadId: System.Int32, <>4__this: System.Xml.Linq.XElement, <a>5__1: System.Xml.Linq.XAttribute, name: System.Xml.Linq.XName, <>3__name: System.Xml.Linq.XName, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.<>4__this = <>4__this
		self.<a>5__1 = <a>5__1
		self.name = name
		self.<>3__name = <>3__name


class ExtractKeyDelegate<TValue>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Entry<TValue>:

    offsets = {'Value': 0, 'HashCode': 0, 'Next': 0}    
    def __init__(self, Value: TValue, HashCode: System.Int32, Next: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.Value = Value
		self.HashCode = HashCode
		self.Next = Next


class XHashtableState<TValue>:

    offsets = {'numEntries': 0, 'extractKey': 0}    
    def __init__(self, numEntries: System.Int32, extractKey: System.Xml.Linq.XHashtable.ExtractKeyDelegate<TValue>, **kwargs):
        super().__init__(self, **kwargs)
		self.numEntries = numEntries
		self.extractKey = extractKey


class <Annotations>d__16<T>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, '<>4__this': 0, '<i>5__2': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: T, <>l__initialThreadId: System.Int32, <>4__this: System.Xml.Linq.XObject, <i>5__2: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.<>4__this = <>4__this
		self.<i>5__2 = <i>5__2


class XTypeDescriptionProvider<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ElementWriter:

    offsets = {'writer': 16, 'resolver': 24}    
    def __init__(self, writer: System.Xml.XmlWriter, resolver: System.Xml.Linq.NamespaceResolver, **kwargs):
        super().__init__(self, **kwargs)
		self.writer = writer
		self.resolver = resolver


class LineInfoAnnotation:

    offsets = {'lineNumber': 16, 'linePosition': 20}    
    def __init__(self, lineNumber: System.Int32, linePosition: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.lineNumber = lineNumber
		self.linePosition = linePosition


class NameSerializer:

    offsets = {'expandedName': 16}    
    def __init__(self, expandedName: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.expandedName = expandedName


class NamespaceResolver:

    offsets = {'scope': 16, 'declaration': 24, 'rover': 32}    
    def __init__(self, scope: System.Int32, declaration: System.Xml.Linq.NamespaceResolver.NamespaceDeclaration, rover: System.Xml.Linq.NamespaceResolver.NamespaceDeclaration, **kwargs):
        super().__init__(self, **kwargs)
		self.scope = scope
		self.declaration = declaration
		self.rover = rover


class Res:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SaveOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class XAttribute:

    offsets = {'next': 32, 'name': 40, 'value': 48}    
    def __init__(self, next: System.Xml.Linq.XAttribute, name: System.Xml.Linq.XName, value: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.next = next
		self.name = name
		self.value = value


class XCData:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class XComment:

    offsets = {'value': 40}    
    def __init__(self, value: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value


class XContainer:

    offsets = {'content': 40}    
    def __init__(self, content: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.content = content


class XDeclaration:

    offsets = {'version': 16, 'encoding': 24, 'standalone': 32}    
    def __init__(self, version: System.String, encoding: System.String, standalone: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.version = version
		self.encoding = encoding
		self.standalone = standalone


class XDocument:

    offsets = {'declaration': 48}    
    def __init__(self, declaration: System.Xml.Linq.XDeclaration, **kwargs):
        super().__init__(self, **kwargs)
		self.declaration = declaration


class XDocumentType:

    offsets = {'name': 40, 'publicId': 48, 'systemId': 56, 'internalSubset': 64, 'dtdInfo': 72}    
    def __init__(self, name: System.String, publicId: System.String, systemId: System.String, internalSubset: System.String, dtdInfo: System.Xml.IDtdInfo, **kwargs):
        super().__init__(self, **kwargs)
		self.name = name
		self.publicId = publicId
		self.systemId = systemId
		self.internalSubset = internalSubset
		self.dtdInfo = dtdInfo


class XElement:

    offsets = {'name': 48, 'lastAttr': 56}    
    def __init__(self, name: System.Xml.Linq.XName, lastAttr: System.Xml.Linq.XAttribute, **kwargs):
        super().__init__(self, **kwargs)
		self.name = name
		self.lastAttr = lastAttr


class XHashtable<TValue>:

    offsets = {'state': 0}    
    def __init__(self, state: System.Xml.Linq.XHashtable.XHashtableState<TValue>, **kwargs):
        super().__init__(self, **kwargs)
		self.state = state


class XName:

    offsets = {'ns': 16, 'localName': 24, 'hashCode': 32}    
    def __init__(self, ns: System.Xml.Linq.XNamespace, localName: System.String, hashCode: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.ns = ns
		self.localName = localName
		self.hashCode = hashCode


class XNamespace:
	namespaces: System.Xml.Linq.XHashtable<System.WeakReference>
    offsets = {'namespaces': 0, 'refNone': 8, 'refXml': 16, 'refXmlns': 24, 'namespaceName': 16, 'hashCode': 24, 'names': 32}    
    def __init__(self, namespaces: System.Xml.Linq.XHashtable<System.WeakReference>, refNone: System.WeakReference, refXml: System.WeakReference, refXmlns: System.WeakReference, namespaceName: System.String, hashCode: System.Int32, names: System.Xml.Linq.XHashtable<System.Xml.Linq.XName>, **kwargs):
        super().__init__(self, **kwargs)
		self.namespaces = namespaces
		self.refNone = refNone
		self.refXml = refXml
		self.refXmlns = refXmlns
		self.namespaceName = namespaceName
		self.hashCode = hashCode
		self.names = names


class XNode:

    offsets = {'next': 32}    
    def __init__(self, next: System.Xml.Linq.XNode, **kwargs):
        super().__init__(self, **kwargs)
		self.next = next


class XObject:

    offsets = {'parent': 16, 'annotations': 24}    
    def __init__(self, parent: System.Xml.Linq.XContainer, annotations: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.parent = parent
		self.annotations = annotations


class XObjectChange:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class XObjectChangeAnnotation:

    offsets = {'changing': 16, 'changed': 24}    
    def __init__(self, changing: System.EventHandler<System.Xml.Linq.XObjectChangeEventArgs>, changed: System.EventHandler<System.Xml.Linq.XObjectChangeEventArgs>, **kwargs):
        super().__init__(self, **kwargs)
		self.changing = changing
		self.changed = changed


class XObjectChangeEventArgs:
	Add: System.Xml.Linq.XObjectChangeEventArgs
    offsets = {'Add': 0, 'Remove': 8, 'Name': 16, 'Value': 24, 'objectChange': 16}    
    def __init__(self, Add: System.Xml.Linq.XObjectChangeEventArgs, Remove: System.Xml.Linq.XObjectChangeEventArgs, Name: System.Xml.Linq.XObjectChangeEventArgs, Value: System.Xml.Linq.XObjectChangeEventArgs, objectChange: System.Xml.Linq.XObjectChange, **kwargs):
        super().__init__(self, **kwargs)
		self.Add = Add
		self.Remove = Remove
		self.Name = Name
		self.Value = Value
		self.objectChange = objectChange


class XProcessingInstruction:

    offsets = {'target': 40, 'data': 48}    
    def __init__(self, target: System.String, data: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.target = target
		self.data = data


class XStreamingElement:

    offsets = {'name': 16, 'content': 24}    
    def __init__(self, name: System.Xml.Linq.XName, content: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.name = name
		self.content = content


class XText:

    offsets = {'text': 40}    
    def __init__(self, text: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.text = text


class ThrowStub:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
