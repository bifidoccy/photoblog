from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-0%1dy0-b#nqxaws=z$&bi%(r6qsi55_g+yb6odi56-76wcqza6'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATIC_DIR = BASE_DIR / 'static'
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = BASE_DIR / 'static'