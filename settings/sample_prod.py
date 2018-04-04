from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost','127.0.0.1','example.com']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '853hhdq2%nt&f3kxi0itgl4_i87y3)9ybpxb*^j#h%91i73)#l'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

