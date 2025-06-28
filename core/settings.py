"""
Django settings for core project.
Generated for BrainstormerAI on 2025-03-27 11:31:18
"""

from pathlib import Path
import os
from datetime import datetime
from decouple import config, Csv
import pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-your-secret-key-here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notifications.apps.NotificationsConfig',
    'voters.apps.VotersConfig',
    'rangefilter',
    'rest_framework',
    'rest_framework.authtoken',
    'widget_tweaks',
    'passes',
    'news',
    'ckeditor',
    'ckeditor_uploader',
    'events',
    'Media_Management',
    'blogs',
    'invitations',
    'drf_yasg',
    # 'storages',  # Commented out - not using AWS S3
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'core', 'templates'),
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'voters', 'templates'),
            os.path.join(BASE_DIR, 'notifications', 'templates'),
            os.path.join(BASE_DIR, 'events', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database Configuration using environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': config('DB_NAME', default='voter_management'),
        'NAME': config('DB_NAME', default='testnew'),
        #'USER': config('DB_USER', default='voter_admin'),
        'USER': config('DB_USER', default='admin'),
        #'PASSWORD': config('DB_PASSWORD', default='Voter@1234'),
        'PASSWORD': config('DB_PASSWORD', default='Target321h'),
        'HOST': config('DB_HOST', default='mpsahab.c52ygcs8ia06.eu-north-1.rds.amazonaws.com'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
        'TEST': {
            'NAME': 'test_voter_management',
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    }
}

# Password validation
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
LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')
TIME_ZONE = config('TIME_ZONE', default='UTC')
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = config('STATIC_URL', default='static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Whitenoise configuration for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = config('MEDIA_URL', default='/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

CKEDITOR_UPLOAD_PATH = "uploads/"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Admin Site Configuration
ADMIN_SITE_HEADER = "Voter Management System"
ADMIN_SITE_TITLE = "Voter Management System"
ADMIN_INDEX_TITLE = "Welcome to Voter Management System"

# Session Configuration
SESSION_COOKIE_AGE = config('SESSION_COOKIE_AGE', default=86400, cast=int)  # 24 hours
SESSION_SAVE_EVERY_REQUEST = True

EDUMARC_API_KEY = 'clnnab4k2000bj7qx6h14fu7r'
EDUMARC_API_URL = 'https://smsapi.edumarcsms.com/api/v1/sendsms'  # Check if this is the correct URL
EDUMARC_SENDER_ID = 'EDUMRC'  # Replace with your registered sender ID

# Logging settings for better debugging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {asctime} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
            'maxBytes': 5242880,  # 5 MB
            'backupCount': 5,
        },
        'notification_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'notification.log'),
            'formatter': 'verbose',
            'maxBytes': 5242880,  # 5 MB
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'notifications': {
            'handlers': ['console', 'notification_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Custom Settings for Voter Management
VOTER_EXCEL_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'excel_uploads')
VOTER_EXPORT_PATH = os.path.join(MEDIA_ROOT, 'exports')

# Create necessary directories
os.makedirs(VOTER_EXCEL_UPLOAD_PATH, exist_ok=True)
os.makedirs(VOTER_EXPORT_PATH, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, 'static'), exist_ok=True)

# Current User and Timestamp
CURRENT_USER = 'BrainstormerAI'
CURRENT_TIMESTAMP = '2025-03-27 11:31:18'

# Cache Settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Custom Template Context Processor
def global_settings(request):
    return {
        'ADMIN_SITE_HEADER': ADMIN_SITE_HEADER,
        'CURRENT_USER': CURRENT_USER,
        'CURRENT_TIMESTAMP': CURRENT_TIMESTAMP,
    }

# Add the context processor to TEMPLATES
TEMPLATES[0]['OPTIONS']['context_processors'].append('core.settings.global_settings')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or your email host
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'adititomar201098@gmail.com'
EMAIL_HOST_PASSWORD = 'pizq izoc milp zlow'

# Swagger Settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,
    'PERSIST_AUTH': True,
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'REFETCH_SCHEMA_ON_LOGOUT': True,
}

# Install PyMySQL
pymysql.install_as_MySQLdb()

# Production settings
if not DEBUG:
    # Security settings for production
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
    # Static files configuration for production
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    # Render Media Storage Configuration
    # Use Render's persistent disk for media files
    MEDIA_ROOT = '/opt/render/project/src/media'
    MEDIA_URL = '/media/'
    
    # AWS S3 Configuration for Media Files (commented out - not using S3)
    # AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
    # AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
    # AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
    # AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='us-east-1')
    # AWS_S3_FILE_OVERWRITE = False
    # AWS_DEFAULT_ACL = None
    # AWS_S3_VERIFY = True
    
    # Use S3 for media files in production (commented out)
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
    
    # HTTPS settings (uncomment if using HTTPS)
    # SECURE_SSL_REDIRECT = True
    # SECURE_HSTS_SECONDS = 31536000
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True

