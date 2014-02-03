# config.py

from authomatic.providers import oauth2
import authomatic

CONFIG = {
    
      'fb': {
           
        'class_': oauth2.Facebook,
        
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '1394422184150859',
        'consumer_secret': '#########################',
        'id': authomatic.provider_id(),
        
        # We need the "publish_stream" scope to post to users timeline,
        # the "offline_access" scope to be able to refresh credentials,
        # and the other scopes to get user info.
        'scope': ['publish_stream', 'offline_access', 'user_about_me', 'email'],
    },
	
	'google':{
	'class_':oauth2.Google,

	'consumer_key': '942211030823-ramlps084p89tema8if877gl5makqlt1.apps.googleusercontent.com',
        'consumer_secret': '#########################',

        'id': authomatic.provider_id(),
        'scope': oauth2.Google.user_info_scope + [
            'https://www.googleapis.com/auth/calendar',
            'https://mail.google.com/mail/feed/atom',
            'https://www.googleapis.com/auth/drive',
            'https://gdata.youtube.com'],
        '_apis': {
            'List your calendars': ('GET', 'https://www.googleapis.com/calendar/v3/users/me/calendarList'),
            'List your YouTube playlists': ('GET', 'https://gdata.youtube.com/feeds/api/users/default/playlists?alt=json'),
        },
    },
    
    'linkedin': {
        'class_': oauth2.LinkedIn,
        'consumer_key': '75ozdhmmkfr9bm',
        'consumer_secret': '################',
        'id': authomatic.provider_id(),
        'scope': oauth2.LinkedIn.user_info_scope + ['rw_nus', 'r_network'],
        '_name': 'LinkedIn',
        '_apis': {
                  'List your connections': ('GET', 'https://api.linkedin.com/v1/people/~/connections'),
        },
    }
}
