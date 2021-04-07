'''Use this for production'''

from .base import *

DEBUG = True
ALLOWED_HOSTS = ["134.209.115.172",]


WSGI_APPLICATION = 'djfilter.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'LandScrap',
        'USER': 'LandScrap',
        'PASSWORD': 'w87zhetrhgxdvo21',
        'HOST': 'db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS =os.path.join(BASE_DIR, 'static_in_env/')



STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
