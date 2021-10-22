"""
Django settings for quartsite project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/

Ulyses: 
Tutorial for deploying to heroku : 

1) https://www.youtube.com/watch?v=kBwhtEIXGII (Worked well)

"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#For local BASE_DIR=C:\Users\1098350515\Documents\quart\webSiteQuart
BASE_DIR = Path(__file__).resolve().parent.parent
print('This is BASE_DIR:',str(BASE_DIR))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#0gu39zl-*&yty0mmx38lkw-lyta2rh!vqn2j!cu^=mq_74u1s'

# SECURITY WARNING: don't run with debug turned on in production!
#For local host DEBUG=True, For Go daddy (production) DEBUG =False
#For localhost testing use DEBUG=TRUE so it will take the static files from each static folder in each folder app
#For Production , use DEBUG = FALSE and it will take all static files from staticfiles main folder for all sites
DEBUG = True

# "*" means all hosts allowed
#Tutorial to domain setup : https://www.youtube.com/watch?v=yFd-YhG6N2g
#For Go daddy: ALLOWED_HOSTS is the list of servers accepted to get the web site, then, for practical things keep it with '*' or add all the urls that will get the web site
#If you don't change this value for the correct web sites, like go daddy, it will return a BAD REQUEST
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appQuart.apps.AppquartConfig',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'quartsite.urls'

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

WSGI_APPLICATION = 'quartsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7vvujncq3os5s',
        'USER': 'acanhvmrdorzis',
        'PASSWORD': 'e4a2d5e50f22dd51728eff619d70c9b172317f7e89d767c34f3b2aba91c0f339',
        'HOST': 'ec2-23-23-164-251.compute-1.amazonaws.com',
        'PORT':'5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATIC_ROOT is the folder where all static files for all apps will live
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
print('STATIC_ROOT:',str(STATIC_ROOT))
#STATIC_URL is for each app static folder, so this indicates every app will have a folder called "/static/"
#where static files (css,etc) will be s
STATIC_URL = '/static/'



