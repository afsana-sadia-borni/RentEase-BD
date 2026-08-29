"""
Django settings for rentease_bd project.
"""

import os
from pathlib import Path
import cloudinary
from dotenv import load_dotenv

# .env ফাইল থেকে Variable লোড করা
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# Security
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-wiflf_iqy)lwtu)ou!svx^t8ee253fy(-!m%!10n)8z%!ebstx')

# Render-এ থাকলে DEBUG অটোমেটিক False হবে, লোকাল পিসিতে True থাকবে
DEBUG = os.getenv('RENDER') is None

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',  # staticfiles এর ঠিক উপরে
    'django.contrib.staticfiles',
    'cloudinary',          # Cloudinary app
    'home',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Added for static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'rentease_bd.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'rentease_bd.wsgi.application'


# Database (PostgreSQL - Credentials from Environment)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "neondb"),
        "USER": os.getenv("DB_USER", "neondb_owner"),
        "PASSWORD": os.getenv("DB_PASSWORD", "npg_ioDaIH87lTpF"),
        "HOST": os.getenv("DB_HOST", "ep-still-mode-axm4pomw.c-4.us-east-2.aws.neon.tech"),
        "PORT": os.getenv("DB_PORT", "5432"),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}


# Fix AutoField warning
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files (image upload using Cloudinary)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# গ্লোবাল Cloudinary Configuration
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)