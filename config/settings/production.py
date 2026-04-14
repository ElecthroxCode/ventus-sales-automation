from .base import *
import os
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    ".railway.app",
    "localhost",
    "127.0.0.1",
    os.getenv("RAILWAY_PUBLIC_DOMAIN", ""),
    os.getenv("RAILWAY_PRIVATE_DOMAIN", ""),
]


ALLOWED_HOSTS = [h for h in ALLOWED_HOSTS if h]

DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("DATABASE_URL"),
        conn_max_age=600
    )
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.railway.app",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "apps/dashboard/static",
]

# WhiteNoise serves static files in production
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"