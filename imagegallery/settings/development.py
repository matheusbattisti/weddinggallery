from imagegallery.settings.common import *

ALLOWED_HOSTS = ['*']

SECRET_KEY = '1bdo6#r7t$jw#i#tdzok+#_xite@dbi$+v%d-%&+gwve$8$#@f'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'imagegallery',
        'HOST': "localhost",
        'PORT': 27017, 
        # 'USER': 'matheus',
        # 'PASSWORD': 'This1s4H4rdPassW0rd',
        'AUTH_SOURCE': 'admin',
    }
}

# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'imagegallery')