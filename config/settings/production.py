from .base import *
import dj_database_url
import os


ALLOWED_HOSTS = ['*']  # luego puedes restringir

DATABASES = {
    'default': dj_database_url.parse(
        os.getenv("DATABASE_URL"),
        conn_max_age=600
    )
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')