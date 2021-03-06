"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6#x1@m7$&k31$@s$58@0#o2m2@5@blkjp^yl2l6*vd^k4*_6zp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',

    'taggit.apps.TaggitAppConfig',
    'taggit_templatetags2',

    'bookmark.apps.BookmarkConfig', # 추가
    'blog.apps.BlogConfig', # 추가'

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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_ex_db',  # 데이터베이스 명
        'HOST': 'localhost',  # 서버 IP
        'PORT': '3306',  # 포트번호
        'USER': 'webuser',  # 사용자 ID
        'PASSWORD': '1234',  # 비밀번호

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]
# 회원가입 사용할 때 패스워드 유효~~~~~~~



# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'
USE_TZ = False
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# 프로젝트 디렉토리 밑에 있다
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


TAGGIT_CASE_INSENSITIVE = True
TAGGIT_LIMIT = 50

# 로그인 관련 URL 디폴트 값
# LOGIN_URL = '/accounts/login/' # 로그인 페이지 URL
# LOGIN_REDIRECT_URL = '/accounts/profile' # 로그인 성공시 리다이렉트할 URL
LOGOUT_REDIRECT_URL = '/accounts/login/' # 로그 아웃시 리다이렉트할 URL
LOGIN_REDIRECT_URL = '/' # 로그인 성공시 리다이렉트할 URL, 첫 페이지가 나을 듯해서 바꾼 거임

#USE_I18N = True

#USE_L10N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
