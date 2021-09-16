


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <PrivateImplementationDetails>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class __StaticArrayInitTypeSize=127:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CollectionHeaderTypeInfo<T,U>:

    offsets = {'minimalCount': 0, 'separator': 0, 'parser': 0}    
    def __init__(self, minimalCount: System.Int32, separator: System.String, parser: System.Net.Http.Headers.TryParseListDelegate<T>, **kwargs):
        super().__init__(self, **kwargs)
		self.minimalCount = minimalCount
		self.separator = separator
		self.parser = parser


class HeaderTypeInfo<T,U>:

    offsets = {'parser': 0}    
    def __init__(self, parser: System.Net.Http.Headers.TryParseDelegate<T>, **kwargs):
        super().__init__(self, **kwargs)
		self.parser = parser


class <GetEnumerator>d__19:

    offsets = {'<>1__state': 16, '<>2__current': 24, '<>4__this': 40, '<>7__wrap1': 48}    
    def __init__(self, <>1__state: System.Int32, <>2__current: System.Collections.Generic.KeyValuePair<System.String,System.Collections.Generic.IEnumerable<System.String>>, <>4__this: System.Net.Http.Headers.HttpHeaders, <>7__wrap1: System.Collections.Generic.Dictionary.Enumerator<System.String,System.Net.Http.Headers.HttpHeaders.HeaderBucket>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>4__this = <>4__this
		self.<>7__wrap1 = <>7__wrap1


class HeaderBucket:

    offsets = {'Parsed': 16, 'values': 24, 'CustomToString': 32}    
    def __init__(self, Parsed: System.Object, values: System.Collections.Generic.List<System.String>, CustomToString: System.Func<System.Object,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.Parsed = Parsed
		self.values = values
		self.CustomToString = CustomToString


class <>c:
	<>9: System.Net.Http.Headers.HttpRequestHeaders.<>c
    offsets = {'<>9': 0, '<>9__19_0': 8, '<>9__22_0': 16, '<>9__29_0': 24, '<>9__71_0': 32}    
    def __init__(self, <>9: System.Net.Http.Headers.HttpRequestHeaders.<>c, <>9__19_0: System.Predicate<System.String>, <>9__22_0: System.Predicate<System.String>, <>9__29_0: System.Predicate<System.Net.Http.Headers.TransferCodingHeaderValue>, <>9__71_0: System.Predicate<System.Net.Http.Headers.TransferCodingHeaderValue>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__19_0 = <>9__19_0
		self.<>9__22_0 = <>9__22_0
		self.<>9__29_0 = <>9__29_0
		self.<>9__71_0 = <>9__71_0


class <>c:
	<>9: System.Net.Http.Headers.MediaTypeHeaderValue.<>c
    offsets = {'<>9': 0, '<>9__6_0': 8}    
    def __init__(self, <>9: System.Net.Http.Headers.MediaTypeHeaderValue.<>c, <>9__6_0: System.Predicate<System.Net.Http.Headers.NameValueHeaderValue>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__6_0 = <>9__6_0


class DateTime:
	ToString: System.Func<System.Object,System.String>
    offsets = {'ToString': 0}    
    def __init__(self, ToString: System.Func<System.Object,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.ToString = ToString


class <>c:
	<>9: System.Net.Http.Headers.Parser.DateTime.<>c
    offsets = {'<>9': 0}    
    def __init__(self, <>9: System.Net.Http.Headers.Parser.DateTime.<>c, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9


class EmailAddress:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Host:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Int:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Long:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MD5:
	ToString: System.Func<System.Object,System.String>
    offsets = {'ToString': 0}    
    def __init__(self, ToString: System.Func<System.Object,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.ToString = ToString


class <>c:
	<>9: System.Net.Http.Headers.Parser.MD5.<>c
    offsets = {'<>9': 0}    
    def __init__(self, <>9: System.Net.Http.Headers.Parser.MD5.<>c, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9


class TimeSpanSeconds:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Token:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Uri:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Type:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class <SendAsyncWorker>d__47:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, 'cancellationToken': 56, 'request': 64, 'completionOption': 72, '<response>5__1': 80, '<lcts>5__2': 88, '<>u__1': 96, '<>u__2': 112}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<System.Net.Http.HttpResponseMessage>, <>4__this: System.Net.Http.HttpClient, cancellationToken: System.Threading.CancellationToken, request: System.Net.Http.HttpRequestMessage, completionOption: System.Net.Http.HttpCompletionOption, <response>5__1: System.Net.Http.HttpResponseMessage, <lcts>5__2: System.Threading.CancellationTokenSource, <>u__1: System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter<System.Net.Http.HttpResponseMessage>, <>u__2: System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.cancellationToken = cancellationToken
		self.request = request
		self.completionOption = completionOption
		self.<response>5__1 = <response>5__1
		self.<lcts>5__2 = <lcts>5__2
		self.<>u__1 = <>u__1
		self.<>u__2 = <>u__2


class <>c:
	<>9: System.Net.Http.HttpClientHandler.<>c
    offsets = {'<>9': 0, '<>9__61_0': 8, '<>9__64_0': 16}    
    def __init__(self, <>9: System.Net.Http.HttpClientHandler.<>c, <>9__61_0: System.Func<System.String,System.Boolean>, <>9__64_0: System.Action<System.Object>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__61_0 = <>9__61_0
		self.<>9__64_0 = <>9__64_0


class <SendAsync>d__64:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, 'request': 56, 'cancellationToken': 64, '<wrequest>5__1': 72, '<content>5__2': 80, '<stream>5__3': 88, '<wresponse>5__4': 96, '<>7__wrap1': 104, '<>u__1': 128, '<>u__2': 144, '<>u__3': 160, '<>u__4': 176}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<System.Net.Http.HttpResponseMessage>, <>4__this: System.Net.Http.HttpClientHandler, request: System.Net.Http.HttpRequestMessage, cancellationToken: System.Threading.CancellationToken, <wrequest>5__1: System.Net.HttpWebRequest, <content>5__2: System.Net.Http.HttpContent, <stream>5__3: System.IO.Stream, <wresponse>5__4: System.Net.HttpWebResponse, <>7__wrap1: System.Threading.CancellationTokenRegistration, <>u__1: System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter, <>u__2: System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter<System.IO.Stream>, <>u__3: System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter<System.Net.WebResponse>, <>u__4: System.Runtime.CompilerServices.TaskAwaiter<System.Net.Http.HttpResponseMessage>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.request = request
		self.cancellationToken = cancellationToken
		self.<wrequest>5__1 = <wrequest>5__1
		self.<content>5__2 = <content>5__2
		self.<stream>5__3 = <stream>5__3
		self.<wresponse>5__4 = <wresponse>5__4
		self.<>7__wrap1 = <>7__wrap1
		self.<>u__1 = <>u__1
		self.<>u__2 = <>u__2
		self.<>u__3 = <>u__3
		self.<>u__4 = <>u__4


class <LoadIntoBufferAsync>d__17:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, 'maxBufferSize': 56, '<>u__1': 64}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, <>4__this: System.Net.Http.HttpContent, maxBufferSize: System.Int64, <>u__1: System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.maxBufferSize = maxBufferSize
		self.<>u__1 = <>u__1


class <ReadAsStringAsync>d__20:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, '<>u__1': 56}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<System.String>, <>4__this: System.Net.Http.HttpContent, <>u__1: System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.<>u__1 = <>u__1


class FixedMemoryStream:

    offsets = {'maxSize': 80}    
    def __init__(self, maxSize: System.Int64, **kwargs):
        super().__init__(self, **kwargs)
		self.maxSize = maxSize


class HttpClient:
	TimeoutDefault: System.TimeSpan
    offsets = {'TimeoutDefault': 0, 'base_address': 32, 'cts': 40, 'disposed': 48, 'headers': 56, 'buffer_size': 64, 'timeout': 72}    
    def __init__(self, TimeoutDefault: System.TimeSpan, base_address: System.Uri, cts: System.Threading.CancellationTokenSource, disposed: System.Boolean, headers: System.Net.Http.Headers.HttpRequestHeaders, buffer_size: System.Int64, timeout: System.TimeSpan, **kwargs):
        super().__init__(self, **kwargs)
		self.TimeoutDefault = TimeoutDefault
		self.base_address = base_address
		self.cts = cts
		self.disposed = disposed
		self.headers = headers
		self.buffer_size = buffer_size
		self.timeout = timeout


class HttpClientHandler:
	groupCounter: System.Int64
    offsets = {'groupCounter': 0, 'allowAutoRedirect': 16, 'automaticDecompression': 20, 'cookieContainer': 24, 'credentials': 32, 'maxAutomaticRedirections': 40, 'maxRequestContentBufferSize': 48, 'preAuthenticate': 56, 'proxy': 64, 'useCookies': 72, 'useDefaultCredentials': 73, 'useProxy': 74, 'sentRequest': 75, 'connectionGroupName': 80, 'disposed': 88}    
    def __init__(self, groupCounter: System.Int64, allowAutoRedirect: System.Boolean, automaticDecompression: System.Net.DecompressionMethods, cookieContainer: System.Net.CookieContainer, credentials: System.Net.ICredentials, maxAutomaticRedirections: System.Int32, maxRequestContentBufferSize: System.Int64, preAuthenticate: System.Boolean, proxy: System.Net.IWebProxy, useCookies: System.Boolean, useDefaultCredentials: System.Boolean, useProxy: System.Boolean, sentRequest: System.Boolean, connectionGroupName: System.String, disposed: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.groupCounter = groupCounter
		self.allowAutoRedirect = allowAutoRedirect
		self.automaticDecompression = automaticDecompression
		self.cookieContainer = cookieContainer
		self.credentials = credentials
		self.maxAutomaticRedirections = maxAutomaticRedirections
		self.maxRequestContentBufferSize = maxRequestContentBufferSize
		self.preAuthenticate = preAuthenticate
		self.proxy = proxy
		self.useCookies = useCookies
		self.useDefaultCredentials = useDefaultCredentials
		self.useProxy = useProxy
		self.sentRequest = sentRequest
		self.connectionGroupName = connectionGroupName
		self.disposed = disposed


class HttpCompletionOption:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class HttpContent:

    offsets = {'buffer': 16, 'disposed': 24, 'headers': 32}    
    def __init__(self, buffer: System.Net.Http.HttpContent.FixedMemoryStream, disposed: System.Boolean, headers: System.Net.Http.Headers.HttpContentHeaders, **kwargs):
        super().__init__(self, **kwargs)
		self.buffer = buffer
		self.disposed = disposed
		self.headers = headers


class HttpMessageHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class HttpMessageInvoker:

    offsets = {'handler': 16, 'disposeHandler': 24}    
    def __init__(self, handler: System.Net.Http.HttpMessageHandler, disposeHandler: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.handler = handler
		self.disposeHandler = disposeHandler


class HttpMethod:
	delete_method: System.Net.Http.HttpMethod
    offsets = {'delete_method': 0, 'get_method': 8, 'head_method': 16, 'options_method': 24, 'post_method': 32, 'put_method': 40, 'trace_method': 48, 'method': 16}    
    def __init__(self, delete_method: System.Net.Http.HttpMethod, get_method: System.Net.Http.HttpMethod, head_method: System.Net.Http.HttpMethod, options_method: System.Net.Http.HttpMethod, post_method: System.Net.Http.HttpMethod, put_method: System.Net.Http.HttpMethod, trace_method: System.Net.Http.HttpMethod, method: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.delete_method = delete_method
		self.get_method = get_method
		self.head_method = head_method
		self.options_method = options_method
		self.post_method = post_method
		self.put_method = put_method
		self.trace_method = trace_method
		self.method = method


class HttpRequestException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class HttpRequestMessage:

    offsets = {'headers': 16, 'method': 24, 'version': 32, 'uri': 40, 'is_used': 48, 'disposed': 49, '<Content>k__BackingField': 56}    
    def __init__(self, headers: System.Net.Http.Headers.HttpRequestHeaders, method: System.Net.Http.HttpMethod, version: System.Version, uri: System.Uri, is_used: System.Boolean, disposed: System.Boolean, <Content>k__BackingField: System.Net.Http.HttpContent, **kwargs):
        super().__init__(self, **kwargs)
		self.headers = headers
		self.method = method
		self.version = version
		self.uri = uri
		self.is_used = is_used
		self.disposed = disposed
		self.<Content>k__BackingField = <Content>k__BackingField


class HttpResponseMessage:

    offsets = {'headers': 16, 'reasonPhrase': 24, 'statusCode': 32, 'version': 40, 'disposed': 48, '<Content>k__BackingField': 56, '<RequestMessage>k__BackingField': 64}    
    def __init__(self, headers: System.Net.Http.Headers.HttpResponseHeaders, reasonPhrase: System.String, statusCode: System.Net.HttpStatusCode, version: System.Version, disposed: System.Boolean, <Content>k__BackingField: System.Net.Http.HttpContent, <RequestMessage>k__BackingField: System.Net.Http.HttpRequestMessage, **kwargs):
        super().__init__(self, **kwargs)
		self.headers = headers
		self.reasonPhrase = reasonPhrase
		self.statusCode = statusCode
		self.version = version
		self.disposed = disposed
		self.<Content>k__BackingField = <Content>k__BackingField
		self.<RequestMessage>k__BackingField = <RequestMessage>k__BackingField


class StreamContent:

    offsets = {'content': 40, 'bufferSize': 48, 'cancellationToken': 56, 'startPosition': 64, 'contentCopied': 72}    
    def __init__(self, content: System.IO.Stream, bufferSize: System.Int32, cancellationToken: System.Threading.CancellationToken, startPosition: System.Int64, contentCopied: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.content = content
		self.bufferSize = bufferSize
		self.cancellationToken = cancellationToken
		self.startPosition = startPosition
		self.contentCopied = contentCopied


class AuthenticationHeaderValue:

    offsets = {'<Parameter>k__BackingField': 16, '<Scheme>k__BackingField': 24}    
    def __init__(self, <Parameter>k__BackingField: System.String, <Scheme>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Parameter>k__BackingField = <Parameter>k__BackingField
		self.<Scheme>k__BackingField = <Scheme>k__BackingField


class CacheControlHeaderValue:

    offsets = {'extensions': 16, 'no_cache_headers': 24, 'private_headers': 32, '<MaxAge>k__BackingField': 40, '<MaxStale>k__BackingField': 56, '<MaxStaleLimit>k__BackingField': 64, '<MinFresh>k__BackingField': 80, '<MustRevalidate>k__BackingField': 96, '<NoCache>k__BackingField': 97, '<NoStore>k__BackingField': 98, '<NoTransform>k__BackingField': 99, '<OnlyIfCached>k__BackingField': 100, '<Private>k__BackingField': 101, '<ProxyRevalidate>k__BackingField': 102, '<Public>k__BackingField': 103, '<SharedMaxAge>k__BackingField': 104}    
    def __init__(self, extensions: System.Collections.Generic.List<System.Net.Http.Headers.NameValueHeaderValue>, no_cache_headers: System.Collections.Generic.List<System.String>, private_headers: System.Collections.Generic.List<System.String>, <MaxAge>k__BackingField: System.Nullable<System.TimeSpan>, <MaxStale>k__BackingField: System.Boolean, <MaxStaleLimit>k__BackingField: System.Nullable<System.TimeSpan>, <MinFresh>k__BackingField: System.Nullable<System.TimeSpan>, <MustRevalidate>k__BackingField: System.Boolean, <NoCache>k__BackingField: System.Boolean, <NoStore>k__BackingField: System.Boolean, <NoTransform>k__BackingField: System.Boolean, <OnlyIfCached>k__BackingField: System.Boolean, <Private>k__BackingField: System.Boolean, <ProxyRevalidate>k__BackingField: System.Boolean, <Public>k__BackingField: System.Boolean, <SharedMaxAge>k__BackingField: System.Nullable<System.TimeSpan>, **kwargs):
        super().__init__(self, **kwargs)
		self.extensions = extensions
		self.no_cache_headers = no_cache_headers
		self.private_headers = private_headers
		self.<MaxAge>k__BackingField = <MaxAge>k__BackingField
		self.<MaxStale>k__BackingField = <MaxStale>k__BackingField
		self.<MaxStaleLimit>k__BackingField = <MaxStaleLimit>k__BackingField
		self.<MinFresh>k__BackingField = <MinFresh>k__BackingField
		self.<MustRevalidate>k__BackingField = <MustRevalidate>k__BackingField
		self.<NoCache>k__BackingField = <NoCache>k__BackingField
		self.<NoStore>k__BackingField = <NoStore>k__BackingField
		self.<NoTransform>k__BackingField = <NoTransform>k__BackingField
		self.<OnlyIfCached>k__BackingField = <OnlyIfCached>k__BackingField
		self.<Private>k__BackingField = <Private>k__BackingField
		self.<ProxyRevalidate>k__BackingField = <ProxyRevalidate>k__BackingField
		self.<Public>k__BackingField = <Public>k__BackingField
		self.<SharedMaxAge>k__BackingField = <SharedMaxAge>k__BackingField


class CollectionExtensions:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class CollectionParser:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ContentDispositionHeaderValue:

    offsets = {'dispositionType': 16, 'parameters': 24}    
    def __init__(self, dispositionType: System.String, parameters: System.Collections.Generic.List<System.Net.Http.Headers.NameValueHeaderValue>, **kwargs):
        super().__init__(self, **kwargs)
		self.dispositionType = dispositionType
		self.parameters = parameters


class ContentRangeHeaderValue:

    offsets = {'unit': 16, '<From>k__BackingField': 24, '<Length>k__BackingField': 40, '<To>k__BackingField': 56}    
    def __init__(self, unit: System.String, <From>k__BackingField: System.Nullable<System.Int64>, <Length>k__BackingField: System.Nullable<System.Int64>, <To>k__BackingField: System.Nullable<System.Int64>, **kwargs):
        super().__init__(self, **kwargs)
		self.unit = unit
		self.<From>k__BackingField = <From>k__BackingField
		self.<Length>k__BackingField = <Length>k__BackingField
		self.<To>k__BackingField = <To>k__BackingField


class ElementTryParser<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EntityTagHeaderValue:
	any: System.Net.Http.Headers.EntityTagHeaderValue
    offsets = {'any': 0, '<IsWeak>k__BackingField': 16, '<Tag>k__BackingField': 24}    
    def __init__(self, any: System.Net.Http.Headers.EntityTagHeaderValue, <IsWeak>k__BackingField: System.Boolean, <Tag>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.any = any
		self.<IsWeak>k__BackingField = <IsWeak>k__BackingField
		self.<Tag>k__BackingField = <Tag>k__BackingField


class HashCodeCalculator:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class HeaderInfo:

    offsets = {'AllowsMany': 16, 'HeaderKind': 20, 'Name': 24, '<CustomToString>k__BackingField': 32}    
    def __init__(self, AllowsMany: System.Boolean, HeaderKind: System.Net.Http.Headers.HttpHeaderKind, Name: System.String, <CustomToString>k__BackingField: System.Func<System.Object,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.AllowsMany = AllowsMany
		self.HeaderKind = HeaderKind
		self.Name = Name
		self.<CustomToString>k__BackingField = <CustomToString>k__BackingField


class HttpContentHeaders:

    offsets = {'content': 32}    
    def __init__(self, content: System.Net.Http.HttpContent, **kwargs):
        super().__init__(self, **kwargs)
		self.content = content


class HttpHeaderKind:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class HttpHeaderValueCollection<T>:

    offsets = {'list': 0, 'headers': 0, 'headerInfo': 0, 'invalidValues': 0}    
    def __init__(self, list: System.Collections.Generic.List<T>, headers: System.Net.Http.Headers.HttpHeaders, headerInfo: System.Net.Http.Headers.HeaderInfo, invalidValues: System.Collections.Generic.List<System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.list = list
		self.headers = headers
		self.headerInfo = headerInfo
		self.invalidValues = invalidValues


class HttpHeaders:
	known_headers: System.Collections.Generic.Dictionary<System.String,System.Net.Http.Headers.HeaderInfo>
    offsets = {'known_headers': 0, 'headers': 16, 'HeaderKind': 24, 'connectionclose': 28, 'transferEncodingChunked': 30}    
    def __init__(self, known_headers: System.Collections.Generic.Dictionary<System.String,System.Net.Http.Headers.HeaderInfo>, headers: System.Collections.Generic.Dictionary<System.String,System.Net.Http.Headers.HttpHeaders.HeaderBucket>, HeaderKind: System.Net.Http.Headers.HttpHeaderKind, connectionclose: System.Nullable<System.Boolean>, transferEncodingChunked: System.Nullable<System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.known_headers = known_headers
		self.headers = headers
		self.HeaderKind = HeaderKind
		self.connectionclose = connectionclose
		self.transferEncodingChunked = transferEncodingChunked


class HttpRequestHeaders:

    offsets = {'expectContinue': 32}    
    def __init__(self, expectContinue: System.Nullable<System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.expectContinue = expectContinue


class HttpResponseHeaders:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Lexer:

    offsets = {'last_token_char': 8, 's': 16, 'pos': 24}    
    def __init__(self, last_token_char: System.Int32, s: System.String, pos: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.last_token_char = last_token_char
		self.s = s
		self.pos = pos


class MediaTypeHeaderValue:

    offsets = {'parameters': 16, 'media_type': 24}    
    def __init__(self, parameters: System.Collections.Generic.List<System.Net.Http.Headers.NameValueHeaderValue>, media_type: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.parameters = parameters
		self.media_type = media_type


class MediaTypeWithQualityHeaderValue:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NameValueHeaderValue:

    offsets = {'value': 16, '<Name>k__BackingField': 24}    
    def __init__(self, value: System.String, <Name>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.<Name>k__BackingField = <Name>k__BackingField


class NameValueWithParametersHeaderValue:

    offsets = {'parameters': 32}    
    def __init__(self, parameters: System.Collections.Generic.List<System.Net.Http.Headers.NameValueHeaderValue>, **kwargs):
        super().__init__(self, **kwargs)
		self.parameters = parameters


class Parser:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ProductHeaderValue:

    offsets = {'<Name>k__BackingField': 16, '<Version>k__BackingField': 24}    
    def __init__(self, <Name>k__BackingField: System.String, <Version>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Name>k__BackingField = <Name>k__BackingField
		self.<Version>k__BackingField = <Version>k__BackingField


class ProductInfoHeaderValue:

    offsets = {'<Comment>k__BackingField': 16, '<Product>k__BackingField': 24}    
    def __init__(self, <Comment>k__BackingField: System.String, <Product>k__BackingField: System.Net.Http.Headers.ProductHeaderValue, **kwargs):
        super().__init__(self, **kwargs)
		self.<Comment>k__BackingField = <Comment>k__BackingField
		self.<Product>k__BackingField = <Product>k__BackingField


class RangeConditionHeaderValue:

    offsets = {'<Date>k__BackingField': 16, '<EntityTag>k__BackingField': 40}    
    def __init__(self, <Date>k__BackingField: System.Nullable<System.DateTimeOffset>, <EntityTag>k__BackingField: System.Net.Http.Headers.EntityTagHeaderValue, **kwargs):
        super().__init__(self, **kwargs)
		self.<Date>k__BackingField = <Date>k__BackingField
		self.<EntityTag>k__BackingField = <EntityTag>k__BackingField


class RangeHeaderValue:

    offsets = {'ranges': 16, 'unit': 24}    
    def __init__(self, ranges: System.Collections.Generic.List<System.Net.Http.Headers.RangeItemHeaderValue>, unit: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.ranges = ranges
		self.unit = unit


class RangeItemHeaderValue:

    offsets = {'<From>k__BackingField': 16, '<To>k__BackingField': 32}    
    def __init__(self, <From>k__BackingField: System.Nullable<System.Int64>, <To>k__BackingField: System.Nullable<System.Int64>, **kwargs):
        super().__init__(self, **kwargs)
		self.<From>k__BackingField = <From>k__BackingField
		self.<To>k__BackingField = <To>k__BackingField


class RetryConditionHeaderValue:

    offsets = {'<Date>k__BackingField': 16, '<Delta>k__BackingField': 40}    
    def __init__(self, <Date>k__BackingField: System.Nullable<System.DateTimeOffset>, <Delta>k__BackingField: System.Nullable<System.TimeSpan>, **kwargs):
        super().__init__(self, **kwargs)
		self.<Date>k__BackingField = <Date>k__BackingField
		self.<Delta>k__BackingField = <Delta>k__BackingField


class StringWithQualityHeaderValue:

    offsets = {'<Quality>k__BackingField': 16, '<Value>k__BackingField': 32}    
    def __init__(self, <Quality>k__BackingField: System.Nullable<System.Double>, <Value>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Quality>k__BackingField = <Quality>k__BackingField
		self.<Value>k__BackingField = <Value>k__BackingField


class Token:
	Empty: System.Net.Http.Headers.Token
    offsets = {'Empty': 0, 'type': 16, '<StartPosition>k__BackingField': 20, '<EndPosition>k__BackingField': 24}    
    def __init__(self, Empty: System.Net.Http.Headers.Token, type: System.Net.Http.Headers.Token.Type, <StartPosition>k__BackingField: System.Int32, <EndPosition>k__BackingField: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.Empty = Empty
		self.type = type
		self.<StartPosition>k__BackingField = <StartPosition>k__BackingField
		self.<EndPosition>k__BackingField = <EndPosition>k__BackingField


class TransferCodingHeaderValue:

    offsets = {'value': 16, 'parameters': 24}    
    def __init__(self, value: System.String, parameters: System.Collections.Generic.List<System.Net.Http.Headers.NameValueHeaderValue>, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.parameters = parameters


class TransferCodingWithQualityHeaderValue:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TryParseDelegate<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TryParseListDelegate<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ViaHeaderValue:

    offsets = {'<Comment>k__BackingField': 16, '<ProtocolName>k__BackingField': 24, '<ProtocolVersion>k__BackingField': 32, '<ReceivedBy>k__BackingField': 40}    
    def __init__(self, <Comment>k__BackingField: System.String, <ProtocolName>k__BackingField: System.String, <ProtocolVersion>k__BackingField: System.String, <ReceivedBy>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Comment>k__BackingField = <Comment>k__BackingField
		self.<ProtocolName>k__BackingField = <ProtocolName>k__BackingField
		self.<ProtocolVersion>k__BackingField = <ProtocolVersion>k__BackingField
		self.<ReceivedBy>k__BackingField = <ReceivedBy>k__BackingField


class WarningHeaderValue:

    offsets = {'<Agent>k__BackingField': 16, '<Code>k__BackingField': 24, '<Date>k__BackingField': 32, '<Text>k__BackingField': 56}    
    def __init__(self, <Agent>k__BackingField: System.String, <Code>k__BackingField: System.Int32, <Date>k__BackingField: System.Nullable<System.DateTimeOffset>, <Text>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Agent>k__BackingField = <Agent>k__BackingField
		self.<Code>k__BackingField = <Code>k__BackingField
		self.<Date>k__BackingField = <Date>k__BackingField
		self.<Text>k__BackingField = <Text>k__BackingField