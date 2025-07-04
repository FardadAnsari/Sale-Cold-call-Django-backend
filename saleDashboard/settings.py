from datetime import timedelta
from pathlib import Path
import pymysql
import os
OPENAI_API_KEY = os.getenv("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")
pymysql.install_as_MySQLdb()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-nuzd_n&+g_@uk$t$#t(26=uf-27b14a2nl+015q(hun%cgt$#v"


DEBUG = True

ALLOWED_HOSTS = ["https://sale.mega-data.co.uk", "*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # add
    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
    'AiAssisstanceApp',
    'GoogleMapDataApp.apps.GooglemapdataappConfig',
    'HistoryApp.apps.HistoryappConfig',
    'accounts_user.apps.AccountsUserConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'accounts_user.middleware.JsonResponse404Middleware',
]



CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://mega-data.co.uk",
    "https://sale.mega-data.co.uk",

]
CSRF_TRUSTED_ORIGINS = ["https://sale.mega-data.co.uk",]


CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

ROOT_URLCONF = 'saleDashboard.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
        'DIRS': [BASE_DIR / "templates"],
    },
]

WSGI_APPLICATION = 'saleDashboard.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "Sale_dash",
        'USER': "parham_user",
        'PASSWORD': "Rad%%^*%&&tatted$%34%#hj",
        'HOST': "92.205.191.109",
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8'
        },
    },
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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'





REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],


}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=8),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=8),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',)
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'panel R&D dashboard API',
    'DESCRIPTION': 'Sale dashboard API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,

}


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_AGE = 86400



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "accounts_user.SaleUser"