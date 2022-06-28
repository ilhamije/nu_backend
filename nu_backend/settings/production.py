from .base import *
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['nu-services.herokuapp.com']

# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('PROD_ENGINE', 'django.db.backends.sqlite3'),
#         'NAME': os.environ.get('PROD_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
#         'USER': os.environ.get('PROD_USER', ''),
#         'PASSWORD': os.environ.get('PROD_PASSWORD', ''),
#         'HOST': os.environ.get('PROD_HOST', 'localhost'),
#         'PORT': os.environ.get('PROD_PORT', ''),
#     }
# }

DATABASES['default'] = dj_database_url.config(default=os.environ.get('PROD_DB_URL'))


SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
