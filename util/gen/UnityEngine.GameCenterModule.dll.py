


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c__DisplayClass10_0:

    offsets = {'callback': 16}    
    def __init__(self, callback: System.Action<System.Boolean,System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.callback = callback


class Social:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ActivePlatform:
	_active: UnityEngine.SocialPlatforms.ISocialPlatform
    offsets = {'_active': 0}    
    def __init__(self, _active: UnityEngine.SocialPlatforms.ISocialPlatform, **kwargs):
        super().__init__(self, **kwargs)
		self._active = _active


class ILocalUser:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IScore:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ISocialPlatform:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IUserProfile:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Local:
	m_LocalUser: UnityEngine.SocialPlatforms.Impl.LocalUser
    offsets = {'m_LocalUser': 0, 'm_Friends': 16, 'm_Users': 24, 'm_AchievementDescriptions': 32, 'm_Achievements': 40, 'm_Leaderboards': 48, 'm_DefaultTexture': 56}    
    def __init__(self, m_LocalUser: UnityEngine.SocialPlatforms.Impl.LocalUser, m_Friends: System.Collections.Generic.List<UnityEngine.SocialPlatforms.Impl.UserProfile>, m_Users: System.Collections.Generic.List<UnityEngine.SocialPlatforms.Impl.UserProfile>, m_AchievementDescriptions: System.Collections.Generic.List<UnityEngine.SocialPlatforms.Impl.AchievementDescription>, m_Achievements: System.Collections.Generic.List<UnityEngine.SocialPlatforms.Impl.Achievement>, m_Leaderboards: System.Collections.Generic.List<UnityEngine.SocialPlatforms.Impl.Leaderboard>, m_DefaultTexture: UnityEngine.Texture2D, **kwargs):
        super().__init__(self, **kwargs)
		self.m_LocalUser = m_LocalUser
		self.m_Friends = m_Friends
		self.m_Users = m_Users
		self.m_AchievementDescriptions = m_AchievementDescriptions
		self.m_Achievements = m_Achievements
		self.m_Leaderboards = m_Leaderboards
		self.m_DefaultTexture = m_DefaultTexture


class Range:

    offsets = {'from': 16, 'count': 20}    
    def __init__(self, from: System.Int32, count: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.from = from
		self.count = count


class TimeScope:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class UserScope:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class UserState:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class Achievement:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AchievementDescription:

    offsets = {'m_Title': 16, 'm_Image': 24, 'm_AchievedDescription': 32, 'm_UnachievedDescription': 40, 'm_Hidden': 48, 'm_Points': 52, '<id>k__BackingField': 56}    
    def __init__(self, m_Title: System.String, m_Image: UnityEngine.Texture2D, m_AchievedDescription: System.String, m_UnachievedDescription: System.String, m_Hidden: System.Boolean, m_Points: System.Int32, <id>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Title = m_Title
		self.m_Image = m_Image
		self.m_AchievedDescription = m_AchievedDescription
		self.m_UnachievedDescription = m_UnachievedDescription
		self.m_Hidden = m_Hidden
		self.m_Points = m_Points
		self.<id>k__BackingField = <id>k__BackingField


class Leaderboard:

    offsets = {'m_Loading': 16, 'm_LocalUserScore': 24, 'm_MaxRange': 32, 'm_Title': 48, '<id>k__BackingField': 64, '<userScope>k__BackingField': 72, '<range>k__BackingField': 76, '<timeScope>k__BackingField': 84}    
    def __init__(self, m_Loading: System.Boolean, m_LocalUserScore: UnityEngine.SocialPlatforms.IScore, m_MaxRange: System.UInt32, m_Title: System.String, <id>k__BackingField: System.String, <userScope>k__BackingField: UnityEngine.SocialPlatforms.UserScope, <range>k__BackingField: UnityEngine.SocialPlatforms.Range, <timeScope>k__BackingField: UnityEngine.SocialPlatforms.TimeScope, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Loading = m_Loading
		self.m_LocalUserScore = m_LocalUserScore
		self.m_MaxRange = m_MaxRange
		self.m_Title = m_Title
		self.<id>k__BackingField = <id>k__BackingField
		self.<userScope>k__BackingField = <userScope>k__BackingField
		self.<range>k__BackingField = <range>k__BackingField
		self.<timeScope>k__BackingField = <timeScope>k__BackingField


class LocalUser:

    offsets = {'m_Authenticated': 72, 'm_Underage': 73}    
    def __init__(self, m_Authenticated: System.Boolean, m_Underage: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Authenticated = m_Authenticated
		self.m_Underage = m_Underage


class Score:

    offsets = {'m_Date': 16, 'm_FormattedValue': 24, 'm_UserID': 32, 'm_Rank': 40, '<leaderboardID>k__BackingField': 48, '<value>k__BackingField': 56}    
    def __init__(self, m_Date: System.DateTime, m_FormattedValue: System.String, m_UserID: System.String, m_Rank: System.Int32, <leaderboardID>k__BackingField: System.String, <value>k__BackingField: System.Int64, **kwargs):
        super().__init__(self, **kwargs)
		self.m_Date = m_Date
		self.m_FormattedValue = m_FormattedValue
		self.m_UserID = m_UserID
		self.m_Rank = m_Rank
		self.<leaderboardID>k__BackingField = <leaderboardID>k__BackingField
		self.<value>k__BackingField = <value>k__BackingField


class UserProfile:

    offsets = {'m_UserName': 16, 'm_ID': 24, 'm_legacyID': 32, 'm_IsFriend': 40, 'm_State': 44, 'm_Image': 48, 'm_gameID': 56}    
    def __init__(self, m_UserName: System.String, m_ID: System.String, m_legacyID: System.String, m_IsFriend: System.Boolean, m_State: UnityEngine.SocialPlatforms.UserState, m_Image: UnityEngine.Texture2D, m_gameID: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.m_UserName = m_UserName
		self.m_ID = m_ID
		self.m_legacyID = m_legacyID
		self.m_IsFriend = m_IsFriend
		self.m_State = m_State
		self.m_Image = m_Image
		self.m_gameID = m_gameID