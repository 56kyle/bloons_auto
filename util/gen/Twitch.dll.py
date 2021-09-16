


class <>f__AnonymousType0<<data>j__TPar>:

    offsets = {'<data>i__Field': 0}    
    def __init__(self, <data>i__Field: <data>j__TPar, **kwargs):
        super().__init__(self, **kwargs)
		self.<data>i__Field = <data>i__Field


class <>f__AnonymousType1<<id>j__TPar,<broadcaster_id>j__TPar,<status>j__TPar>:

    offsets = {'<id>i__Field': 0, '<broadcaster_id>i__Field': 0, '<status>i__Field': 0}    
    def __init__(self, <id>i__Field: <id>j__TPar, <broadcaster_id>i__Field: <broadcaster_id>j__TPar, <status>i__Field: <status>j__TPar, **kwargs):
        super().__init__(self, **kwargs)
		self.<id>i__Field = <id>i__Field
		self.<broadcaster_id>i__Field = <broadcaster_id>i__Field
		self.<status>i__Field = <status>i__Field


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Authentication:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c:
	<>9: Assets.Twitch.Authenticator.<>c
    offsets = {'<>9': 0, '<>9__8_0': 8}    
    def __init__(self, <>9: Assets.Twitch.Authenticator.<>c, <>9__8_0: System.Func<System.String,System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__8_0 = <>9__8_0


class <GetAuthentication>d__8:

    offsets = {'<>1__state': 16, '<>t__builder': 24, 'httpContext': 48, '<>4__this': 56, '<reader>5__2': 64, '<requestContent>5__3': 72, '<>u__1': 80, '<>u__2': 88, '<>7__wrap3': 96, '<>u__3': 104}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<Assets.Twitch.Models.Authentication>, httpContext: System.Net.HttpListenerContext, <>4__this: Assets.Twitch.Authenticator, <reader>5__2: System.IO.StreamReader, <requestContent>5__3: System.String, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<System.String>, <>u__2: System.Runtime.CompilerServices.TaskAwaiter, <>7__wrap3: System.Collections.Generic.IEnumerator<System.String>, <>u__3: System.Runtime.CompilerServices.TaskAwaiter<Assets.Twitch.Models.Authentication>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.httpContext = httpContext
		self.<>4__this = <>4__this
		self.<reader>5__2 = <reader>5__2
		self.<requestContent>5__3 = <requestContent>5__3
		self.<>u__1 = <>u__1
		self.<>u__2 = <>u__2
		self.<>7__wrap3 = <>7__wrap3
		self.<>u__3 = <>u__3


class <LoadHtml>d__7:

    offsets = {'<>1__state': 16, '<>t__builder': 24, 'htmlContent': 48, 'httpResponse': 56, '<output>5__2': 64, '<>u__1': 72}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, htmlContent: System.String, httpResponse: System.Net.HttpListenerResponse, <output>5__2: System.IO.Stream, <>u__1: System.Runtime.CompilerServices.TaskAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.htmlContent = htmlContent
		self.httpResponse = httpResponse
		self.<output>5__2 = <output>5__2
		self.<>u__1 = <>u__1


class <SetBroadcasterType>d__9:

    offsets = {'<>1__state': 16, '<>t__builder': 24, 'authentication': 48, '<>4__this': 56, '<url>5__2': 64, '<webRequest>5__3': 72, '<>u__1': 80}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, authentication: Assets.Twitch.Models.Authentication, <>4__this: Assets.Twitch.Authenticator, <url>5__2: System.String, <webRequest>5__3: UnityEngine.Networking.UnityWebRequest, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<System.Collections.Generic.List<Assets.Twitch.Models.User>>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.authentication = authentication
		self.<>4__this = <>4__this
		self.<url>5__2 = <url>5__2
		self.<webRequest>5__3 = <webRequest>5__3
		self.<>u__1 = <>u__1


class <SignIn>d__5:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, '<>7__wrap1': 64, '<>u__1': 72, '<>u__2': 80, '<authentication>5__3': 88, '<>u__3': 96}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<Assets.Twitch.Models.Authentication>, <>4__this: Assets.Twitch.Authenticator, <>7__wrap1: System.Net.HttpListener, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<System.Net.HttpListenerContext>, <>u__2: System.Runtime.CompilerServices.TaskAwaiter, <authentication>5__3: Assets.Twitch.Models.Authentication, <>u__3: System.Runtime.CompilerServices.TaskAwaiter<Assets.Twitch.Models.Authentication>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.<>7__wrap1 = <>7__wrap1
		self.<>u__1 = <>u__1
		self.<>u__2 = <>u__2
		self.<authentication>5__3 = <authentication>5__3
		self.<>u__3 = <>u__3


class <SignOut>d__4:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, '<webRequest>5__2': 56, '<startTime>5__3': 64, '<>u__1': 72}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, <>4__this: Assets.Twitch.Authenticator, <webRequest>5__2: UnityEngine.Networking.UnityWebRequest, <startTime>5__3: System.DateTime, <>u__1: System.Runtime.CompilerServices.YieldAwaitable.YieldAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.<webRequest>5__2 = <webRequest>5__2
		self.<startTime>5__3 = <startTime>5__3
		self.<>u__1 = <>u__1


class <ValidateToken>d__11:

    offsets = {'<>1__state': 16, '<>t__builder': 24, 'token': 48, '<>4__this': 56, '<httpClient>5__2': 64, '<twitchResponse>5__3': 72, '<>u__1': 80, '<>u__2': 88}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<Assets.Twitch.Models.Authentication>, token: System.String, <>4__this: Assets.Twitch.Authenticator, <httpClient>5__2: System.Net.Http.HttpClient, <twitchResponse>5__3: System.Net.Http.HttpResponseMessage, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<System.Net.Http.HttpResponseMessage>, <>u__2: System.Runtime.CompilerServices.TaskAwaiter<System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.token = token
		self.<>4__this = <>4__this
		self.<httpClient>5__2 = <httpClient>5__2
		self.<twitchResponse>5__3 = <twitchResponse>5__3
		self.<>u__1 = <>u__1
		self.<>u__2 = <>u__2


class <SendWebRequest>d__29<T>:

    offsets = {'<>1__state': 0, '<>t__builder': 0, 'webRequest': 0, 'canceller': 0, '<>4__this': 0, '<startTime>5__2': 0, '<>u__1': 0}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<System.Collections.Generic.List<T>>, webRequest: UnityEngine.Networking.UnityWebRequest, canceller: System.Threading.CancellationTokenSource, <>4__this: Assets.Twitch.Client, <startTime>5__2: System.DateTime, <>u__1: System.Runtime.CompilerServices.YieldAwaitable.YieldAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.webRequest = webRequest
		self.canceller = canceller
		self.<>4__this = <>4__this
		self.<startTime>5__2 = <startTime>5__2
		self.<>u__1 = <>u__1


class <SignIn>d__28:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, '<>u__1': 64}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, <>4__this: Assets.Twitch.Client, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<Assets.Twitch.Models.Authentication>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.<>u__1 = <>u__1


class <SignOut>d__27:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, '<>u__1': 56}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, <>4__this: Assets.Twitch.Client, <>u__1: System.Runtime.CompilerServices.TaskAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.<>u__1 = <>u__1


class <>c:
	<>9: Assets.Twitch.Models.TwitchScopeExtensions.<>c
    offsets = {'<>9': 0, '<>9__0_0': 8}    
    def __init__(self, <>9: Assets.Twitch.Models.TwitchScopeExtensions.<>c, <>9__0_0: System.Func<Assets.Twitch.Models.Scope,System.Collections.Generic.IEnumerable<System.String>>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__0_0 = <>9__0_0


class <>c:
	<>9: Assets.Twitch.Polls.<>c
    offsets = {'<>9': 0, '<>9__29_0': 8, '<>9__30_0': 16, '<>9__30_1': 24, '<>9__30_2': 32, '<>9__30_3': 40, '<>9__32_0': 48, '<>9__34_0': 56, '<>9__34_1': 64, '<>9__34_3': 72, '<>9__34_4': 80, '<>9__35_0': 88, '<>9__37_0': 96}    
    def __init__(self, <>9: Assets.Twitch.Polls.<>c, <>9__29_0: System.Func<Assets.Twitch.Models.SubPoll,System.Boolean>, <>9__30_0: System.Func<Assets.Twitch.Models.SubPoll,System.Boolean>, <>9__30_1: System.Func<Assets.Twitch.Models.PollItem,System.Boolean>, <>9__30_2: System.Func<Assets.Twitch.Models.PollItem,System.String>, <>9__30_3: System.Func<Assets.Twitch.Models.SubPoll,System.Boolean>, <>9__32_0: System.Func<Assets.Twitch.Models.PollItem,System.String>, <>9__34_0: System.Func<Assets.Twitch.Models.SubPoll,System.Collections.Generic.IEnumerable<Assets.Twitch.Models.PollItem>>, <>9__34_1: System.Func<Assets.Twitch.Models.PollItem,System.UInt32>, <>9__34_3: System.Func<Assets.Twitch.Models.PollItem,System.Boolean>, <>9__34_4: System.Func<Assets.Twitch.Models.PollItem,System.Boolean>, <>9__35_0: System.Func<Assets.Twitch.Models.PollItem,System.Boolean>, <>9__37_0: System.Func<System.String,Assets.Twitch.Models.ChoiceBase>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__29_0 = <>9__29_0
		self.<>9__30_0 = <>9__30_0
		self.<>9__30_1 = <>9__30_1
		self.<>9__30_2 = <>9__30_2
		self.<>9__30_3 = <>9__30_3
		self.<>9__32_0 = <>9__32_0
		self.<>9__34_0 = <>9__34_0
		self.<>9__34_1 = <>9__34_1
		self.<>9__34_3 = <>9__34_3
		self.<>9__34_4 = <>9__34_4
		self.<>9__35_0 = <>9__35_0
		self.<>9__37_0 = <>9__37_0


class <>c__DisplayClass33_0:

    offsets = {'choice': 16}    
    def __init__(self, choice: Assets.Twitch.Models.Choice, **kwargs):
        super().__init__(self, **kwargs)
		self.choice = choice


class <>c__DisplayClass34_0:

    offsets = {'pollItem': 16}    
    def __init__(self, pollItem: Assets.Twitch.Models.PollItem, **kwargs):
        super().__init__(self, **kwargs)
		self.pollItem = pollItem


class <CancelPoll>d__29:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, '<webRequest>5__2': 56, '<>u__1': 64}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, <>4__this: Assets.Twitch.Polls, <webRequest>5__2: UnityEngine.Networking.UnityWebRequest, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<System.Collections.Generic.List<Assets.Twitch.Models.Poll>>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.<webRequest>5__2 = <webRequest>5__2
		self.<>u__1 = <>u__1


class <CreatePoll>d__37:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, 'choiceTitles': 56, 'name': 64, 'duration': 72, 'canBitVote': 80, 'bitVotePrice': 84, 'canPointVote': 88, 'pointVotePrice': 92, '<webRequest>5__2': 96, '<>u__1': 104}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<Assets.Twitch.Models.Poll>, <>4__this: Assets.Twitch.Polls, choiceTitles: System.Collections.Generic.IEnumerable<System.String>, name: System.String, duration: System.TimeSpan, canBitVote: System.Boolean, bitVotePrice: System.UInt32, canPointVote: System.Boolean, pointVotePrice: System.UInt32, <webRequest>5__2: UnityEngine.Networking.UnityWebRequest, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<System.Collections.Generic.List<Assets.Twitch.Models.Poll>>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.choiceTitles = choiceTitles
		self.name = name
		self.duration = duration
		self.canBitVote = canBitVote
		self.bitVotePrice = bitVotePrice
		self.canPointVote = canPointVote
		self.pointVotePrice = pointVotePrice
		self.<webRequest>5__2 = <webRequest>5__2
		self.<>u__1 = <>u__1


class <GetPoll>d__38:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, 'id': 56, '<webRequest>5__2': 64, '<>u__1': 72}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder<Assets.Twitch.Models.Poll>, <>4__this: Assets.Twitch.Polls, id: System.String, <webRequest>5__2: UnityEngine.Networking.UnityWebRequest, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<System.Collections.Generic.List<Assets.Twitch.Models.Poll>>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.id = id
		self.<webRequest>5__2 = <webRequest>5__2
		self.<>u__1 = <>u__1


class <GetPollTask>d__30:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, 'name': 56, 'duration': 64, 'canBitVote': 72, 'bitVotePrice': 76, 'canPointVote': 80, 'pointVotePrice': 84, 'maxWinners': 88, '<>7__wrap1': 96, '<subPoll>5__3': 120, '<attemptCount>5__4': 128, '<isLastRetry>5__5': 132, '<>7__wrap5': 136, '<>7__wrap6': 144, '<>u__1': 152, '<>u__2': 160}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, <>4__this: Assets.Twitch.Polls, name: System.String, duration: System.TimeSpan, canBitVote: System.Boolean, bitVotePrice: System.UInt32, canPointVote: System.Boolean, pointVotePrice: System.UInt32, maxWinners: System.Int32, <>7__wrap1: System.Collections.Generic.List.Enumerator<Assets.Twitch.Models.SubPoll>, <subPoll>5__3: Assets.Twitch.Models.SubPoll, <attemptCount>5__4: System.Int32, <isLastRetry>5__5: System.Boolean, <>7__wrap5: System.Object, <>7__wrap6: System.Int32, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<Assets.Twitch.Models.Poll>, <>u__2: System.Runtime.CompilerServices.TaskAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.name = name
		self.duration = duration
		self.canBitVote = canBitVote
		self.bitVotePrice = bitVotePrice
		self.canPointVote = canPointVote
		self.pointVotePrice = pointVotePrice
		self.maxWinners = maxWinners
		self.<>7__wrap1 = <>7__wrap1
		self.<subPoll>5__3 = <subPoll>5__3
		self.<attemptCount>5__4 = <attemptCount>5__4
		self.<isLastRetry>5__5 = <isLastRetry>5__5
		self.<>7__wrap5 = <>7__wrap5
		self.<>7__wrap6 = <>7__wrap6
		self.<>u__1 = <>u__1
		self.<>u__2 = <>u__2


class <RefreshPoll>d__33:

    offsets = {'<>1__state': 16, '<>t__builder': 24, 'subPoll': 48, '<>4__this': 56, '<twitchPoll>5__2': 64, '<>u__1': 72, '<>u__2': 80}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, subPoll: Assets.Twitch.Models.SubPoll, <>4__this: Assets.Twitch.Polls, <twitchPoll>5__2: Assets.Twitch.Models.Poll, <>u__1: System.Runtime.CompilerServices.TaskAwaiter<Assets.Twitch.Models.Poll>, <>u__2: System.Runtime.CompilerServices.TaskAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.subPoll = subPoll
		self.<>4__this = <>4__this
		self.<twitchPoll>5__2 = <twitchPoll>5__2
		self.<>u__1 = <>u__1
		self.<>u__2 = <>u__2


class <StartPoll>d__28:

    offsets = {'<>1__state': 16, '<>t__builder': 24, '<>4__this': 48, 'pollItems': 56, 'maxWinners': 64, 'name': 72, 'duration': 80, 'canBitVote': 88, 'bitVotePrice': 92, 'canPointVote': 96, 'pointVotePrice': 100, '<>u__1': 104}    
    def __init__(self, <>1__state: System.Int32, <>t__builder: System.Runtime.CompilerServices.AsyncTaskMethodBuilder, <>4__this: Assets.Twitch.Polls, pollItems: System.Collections.Generic.List<Assets.Twitch.Models.PollItem>, maxWinners: System.Int32, name: System.String, duration: System.TimeSpan, canBitVote: System.Boolean, bitVotePrice: System.UInt32, canPointVote: System.Boolean, pointVotePrice: System.UInt32, <>u__1: System.Runtime.CompilerServices.TaskAwaiter, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>t__builder = <>t__builder
		self.<>4__this = <>4__this
		self.pollItems = pollItems
		self.maxWinners = maxWinners
		self.name = name
		self.duration = duration
		self.canBitVote = canBitVote
		self.bitVotePrice = bitVotePrice
		self.canPointVote = canPointVote
		self.pointVotePrice = pointVotePrice
		self.<>u__1 = <>u__1


class ApiEndpoints:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AuthenticationHtml:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Authenticator:

    offsets = {'client': 16, 'redirectUrl': 24, 'httpListener': 32}    
    def __init__(self, client: Assets.Twitch.Client, redirectUrl: System.String, httpListener: System.Net.HttpListener, **kwargs):
        super().__init__(self, **kwargs)
		self.client = client
		self.redirectUrl = redirectUrl
		self.httpListener = httpListener


class Client:
	<Instance>k__BackingField: Assets.Twitch.Client
    offsets = {'<Instance>k__BackingField': 0, 'OnAuthenticationChanged': 16, 'clientId': 24, 'webRequestTimeout': 32, '<Storage>k__BackingField': 40, '<Authenticator>k__BackingField': 48, '<Polls>k__BackingField': 56, '_authentication': 64}    
    def __init__(self, <Instance>k__BackingField: Assets.Twitch.Client, OnAuthenticationChanged: System.Action, clientId: System.String, webRequestTimeout: System.TimeSpan, <Storage>k__BackingField: NinjaKiwi.Common.StorageManager, <Authenticator>k__BackingField: Assets.Twitch.Authenticator, <Polls>k__BackingField: Assets.Twitch.Polls, _authentication: Assets.Twitch.Models.Authentication, **kwargs):
        super().__init__(self, **kwargs)
		self.<Instance>k__BackingField = <Instance>k__BackingField
		self.OnAuthenticationChanged = OnAuthenticationChanged
		self.clientId = clientId
		self.webRequestTimeout = webRequestTimeout
		self.<Storage>k__BackingField = <Storage>k__BackingField
		self.<Authenticator>k__BackingField = <Authenticator>k__BackingField
		self.<Polls>k__BackingField = <Polls>k__BackingField
		self._authentication = _authentication


class Polls:

    offsets = {'OnSubPollStarted': 16, 'OnPollsFinished': 24, 'OnPollsFailed': 32, 'OnPollRefreshed': 40, 'OnPollRefreshFailed': 48, 'twitchClient': 56, 'pollRunner': 64, 'pollRunnerCanceller': 72, '<PollItems>k__BackingField': 80, '<SubPolls>k__BackingField': 88}    
    def __init__(self, OnSubPollStarted: System.Action<Assets.Twitch.Models.SubPoll>, OnPollsFinished: System.Action<System.Collections.Generic.List<System.String>>, OnPollsFailed: System.Action<System.Exception>, OnPollRefreshed: System.Action, OnPollRefreshFailed: System.Action, twitchClient: Assets.Twitch.Client, pollRunner: System.Threading.Tasks.Task, pollRunnerCanceller: System.Threading.CancellationTokenSource, <PollItems>k__BackingField: System.Collections.Generic.List<Assets.Twitch.Models.PollItem>, <SubPolls>k__BackingField: System.Collections.Generic.List<Assets.Twitch.Models.SubPoll>, **kwargs):
        super().__init__(self, **kwargs)
		self.OnSubPollStarted = OnSubPollStarted
		self.OnPollsFinished = OnPollsFinished
		self.OnPollsFailed = OnPollsFailed
		self.OnPollRefreshed = OnPollRefreshed
		self.OnPollRefreshFailed = OnPollRefreshFailed
		self.twitchClient = twitchClient
		self.pollRunner = pollRunner
		self.pollRunnerCanceller = pollRunnerCanceller
		self.<PollItems>k__BackingField = <PollItems>k__BackingField
		self.<SubPolls>k__BackingField = <SubPolls>k__BackingField


class TwitchAuthenticationException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TwitchException:

    offsets = {'displayMessage': 136}    
    def __init__(self, displayMessage: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.displayMessage = displayMessage


class TwitchInvalidRequestException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class TimeSpanSecondsConverter:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Authentication:

    offsets = {'userId': 16, 'userName': 24, 'expirationDate': 32, 'token': 48, 'broadcasterType': 56}    
    def __init__(self, userId: System.String, userName: System.String, expirationDate: System.DateTime, token: System.String, broadcasterType: Assets.Twitch.Models.BroadcasterType, **kwargs):
        super().__init__(self, **kwargs)
		self.userId = userId
		self.userName = userName
		self.expirationDate = expirationDate
		self.token = token
		self.broadcasterType = broadcasterType


class BroadcasterType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Choice:

    offsets = {'id': 24, 'votes': 32, 'channel_points_votes': 36, 'bits_votes': 40}    
    def __init__(self, id: System.String, votes: System.UInt32, channel_points_votes: System.UInt32, bits_votes: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.id = id
		self.votes = votes
		self.channel_points_votes = channel_points_votes
		self.bits_votes = bits_votes


class ChoiceBase:

    offsets = {'title': 16}    
    def __init__(self, title: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.title = title


class Poll:

    offsets = {'id': 16, 'userId': 24, 'userName': 32, 'userLogin': 40, 'title': 48, 'canBitVote': 64, 'bitsPerVote': 68, 'canPointVote': 72, 'pointsPerVote': 76, 'status': 80, 'duration': 88, 'startTime': 96, 'endedTime': 104}    
    def __init__(self, id: System.String, userId: System.String, userName: System.String, userLogin: System.String, title: System.String, canBitVote: System.Boolean, bitsPerVote: System.UInt32, canPointVote: System.Boolean, pointsPerVote: System.UInt32, status: Assets.Twitch.Models.PollStatus, duration: System.TimeSpan, startTime: System.DateTime, endedTime: System.DateTime, **kwargs):
        super().__init__(self, **kwargs)
		self.id = id
		self.userId = userId
		self.userName = userName
		self.userLogin = userLogin
		self.title = title
		self.canBitVote = canBitVote
		self.bitsPerVote = bitsPerVote
		self.canPointVote = canPointVote
		self.pointsPerVote = pointsPerVote
		self.status = status
		self.duration = duration
		self.startTime = startTime
		self.endedTime = endedTime


class PollItem:

    offsets = {'id': 16, 'title': 24, 'status': 32, 'votes': 36}    
    def __init__(self, id: System.String, title: System.String, status: Assets.Twitch.Models.PollItemStatus, votes: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.id = id
		self.title = title
		self.status = status
		self.votes = votes


class PollItemStatus:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class PollStatus:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Scope:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class SubPoll:

    offsets = {'id': 16, 'pollItems': 24, 'poll': 32, 'exception': 40, 'updater': 48}    
    def __init__(self, id: System.Int32, pollItems: System.Collections.Generic.List<Assets.Twitch.Models.PollItem>, poll: Assets.Twitch.Models.Poll, exception: System.Exception, updater: System.Threading.Tasks.Task, **kwargs):
        super().__init__(self, **kwargs)
		self.id = id
		self.pollItems = pollItems
		self.poll = poll
		self.exception = exception
		self.updater = updater


class TwitchScopeExtensions:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class User:

    offsets = {'id': 16, 'broadcaster_type': 24}    
    def __init__(self, id: System.String, broadcaster_type: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.id = id
		self.broadcaster_type = broadcaster_type


class PollCreate:

    offsets = {'userId': 16, 'title': 24, 'duration': 40, 'canBitVote': 44, 'bitVotePrice': 48, 'canPointVote': 52, 'pointVotePrice': 56}    
    def __init__(self, userId: System.String, title: System.String, duration: System.UInt32, canBitVote: System.Boolean, bitVotePrice: System.UInt32, canPointVote: System.Boolean, pointVotePrice: System.UInt32, **kwargs):
        super().__init__(self, **kwargs)
		self.userId = userId
		self.title = title
		self.duration = duration
		self.canBitVote = canBitVote
		self.bitVotePrice = bitVotePrice
		self.canPointVote = canPointVote
		self.pointVotePrice = pointVotePrice