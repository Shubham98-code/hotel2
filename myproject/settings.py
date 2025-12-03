"""
Django settings for myproject project.
Updated for Railway Deployment & Security.
"""

from pathlib import Path
import os
from decouple import config, Csv
import dj_database_url  # Needed for Railway Database

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY: Read from Environment Variables ---
SECRET_KEY = config('SECRET_KEY')

# cast=bool converts "False" string to actual Python False
DEBUG = config('DEBUG', default=False, cast=bool)

# Allow Railway domains
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='127.0.0.1,localhost')

# CSRF Trusted Origins (Required for Railway's HTTPS proxy)
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=Csv(), default='http://127.0.0.1')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    # Allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # REQUIRED for Railway CSS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

# --- DATABASE CONFIGURATION ---
# This automatically switches between SQLite (Local) and Postgres (Railway)
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES (CSS/JS) ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where files are collected for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- EMAIL CONFIGURATION (Gmail) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# --- LOGIN / ALLAUTH SETTINGS ---
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
SITE_ID = 1

# --- LOGIN / ALLAUTH SETTINGS ---
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
SITE_ID = 1

# 1. How users log in (Use Email, not Username)
ACCOUNT_LOGIN_METHODS = {'email'}

# 2. REQUIRED: Define the signup fields explicitly
# The asterisk (*) is CRITICAL here. It tells Django "This field is mandatory".
ACCOUNT_SIGNUP_FIELDS = [
    'email*', 
    # You can add 'first_name' or 'last_name' here if you want them
]

# 3. Email Verification
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' 

# 4. REMOVE these lines if they still exist in your file:
# ACCOUNT_EMAIL_REQUIRED = True      <-- DELETE THIS
# ACCOUNT_USERNAME_REQUIRED = False  <-- DELETE THIS
# ACCOUNT_AUTHENTICATION_METHOD = ... <-- DELETE THIS
# Social account providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET'),
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'}
    }
}
SOCIALACCOUNT_LOGIN_ON_GET = True