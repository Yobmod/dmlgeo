"""https://docs.djangoproject.com/en/2.0/topics/settings/
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
# import dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # src
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)) # dmlgeodjango
GIT_DIR = os.path.dirname(BASE_DIR)


SECRET_KEY = os.environ['SECRET_KEY']
LOCALE = os.environ['LOCALE']  # ; print(LOCALE)
SITE_ID = 1


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'django_extensions',
    'rest_framework',

    'dmlgeo',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'dmlgeodjango.urls'
WSGI_APPLICATION = 'dmlgeodjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'dmlgeo',
         'USER': 'yobmod',
    },
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

if LOCALE == 'linux':
    ALLOWED_HOSTS = ['LOCALHOST', '0.0.0.0', '127.0.0.1']
    DEBUG = True


elif LOCALE == 'windows':
    ALLOWED_HOSTS = ['LOCALHOST', '0.0.0.0', '127.0.0.1']
    # GDAL_LIBRARY_PATH = R'C:\OSGeo4W\bin\gdal111.dll'
    GDAL_LIBRARY_PATH = os.getenv(R'GDAL_LIBRARY_PATH')  #; print(GDAL_LIBRARY_PATH)
    GEOS_LIBRARY_PATH = os.getenv(R'GEOS_LIBRARY_PATH')  #; print(GEOS_LIBRARY_PATH)
    DEBUG = True


elif LOCALE == 'heroku':
    ALLOWED_HOSTS = ['dmlgeo.herokuapp.com']  
    GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
    GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')
    DEBUG = False
    DATABASES['default'] = dj_database_url.config()
    #DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

else: 
    DEBUG == False


MEDIA_ROOT = os.path.join(GIT_DIR, "media_cdn")
STATIC_ROOT = os.path.join(GIT_DIR, "static_cdn")
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


