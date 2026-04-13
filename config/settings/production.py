from .base import *
import dj_database_url
import os


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.parse(
        os.getenv("DATABASE_URL"),
        conn_max_age=600
    )
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

_railway_domain = os.getenv('RAILWAY_PUBLIC_DOMAIN')
CSRF_TRUSTED_ORIGINS = (
    [f'https://{_railway_domain}']
    if _railway_domain
    else ['https://web-production-7d6a8.up.railway.app']
) + ['https://*.railway.app']