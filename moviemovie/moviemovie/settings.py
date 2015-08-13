"""
Django settings for moviemovie project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bu(=(bbnpufzhmvkbohn#2777b0yvgsk$e@e8sf=5d1rpfd4+8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'payment',
    'movie_signin',
    'location',
    'thirdauth',
    'homepage',
    'search',
    'discussion',
    'moviedatabase',
    'news',
    'commenting',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'moviemovie.urls'

WSGI_APPLICATION = 'moviemovie.wsgi.application'

LOGIN_REDIRECT_URL = '/' #add a LOGIN_REDIRECT_URL parameter to settings (to prevent the default /account/profile from raising a 404)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#STATIC_ROOT = '/home/yulicheng/moviemovie/static/' #make it work when in server and run python manage.py collectstatic!!!
STATIC_URL = '/moviemovie/static/'
MEDIA_URL = '/moviemovie/media/'
#MEDIA_ROOT = '/home/yulicheng/moviemovie/media/'
ADMIN_MEDIA_PREFIX = '/moviemovie/admin-media/'

#Paypal payment
PAYPAL_MODE='sandbox'
PAYPAL_CLIENT_ID='ASZPNhCr8VeZ_ng8RAW9u-qAAk-qWe3V4c5f7xmN5mGbyzQ4fXqZFJ9nqn5X'
PAYPAL_CLIENT_SECRET='EJ5SRBAFlxvnOjXC1Y0zYtwcEuF8g5fxmoQ6r4yRz3G6iflGhzPmyK5ZopYn'
#Facebook Login
SOCIAL_AUTH_FACEBOOK_KEY = '687123041353714'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f96b4830313489abbf68c81641dee7c9'
#Google Login
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '955599797064-2pabi4ks5tooqncefkmr3o5806srf3cq.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'DrkvJ2pQ3t5Qyd9-NS8mEDgT'
#Twitter login
SOCIAL_AUTH_TWITTER_KEY = 'vePean4wkULoEKsju16jRU1Th'
SOCIAL_AUTH_TWITTER_SECRET = 'vFxK5gzvgITCG4iiF5pGKmFMlV0N47cRvQKGKDa59ByJagHLXU'
