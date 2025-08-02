
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-287a%ie-w@c1xu5$8^3ek4h7vo@sl54p)ev9of!36_2dnj7pa_'


DEBUG = True

ALLOWED_HOSTS = ["*"]

CUSTOM_APPS = [
    'content',
    'home',
    'support',
    'about_direction',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'drf_spectacular',
]


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'content',

    # 'support',
    'about_direction',

    'account',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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
AUTH_USER_MODEL = 'account.User'

STATIC_URL = 'back_static/'
STATIC_ROOT = BASE_DIR / STATIC_URL

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'locale_static',
]

MEDIA_URL = '/back_media/'
MEDIA_ROOT = BASE_DIR / 'back_media'


LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Russian'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'register': '5/hour',  # Максимум 5 регистраций в час
    }
}
