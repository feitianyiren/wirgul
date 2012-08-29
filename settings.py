#! -*- coding: utf-8 -*-
import os
TIME_DURATION_CHOICES = (tuple((n, n) for n in range(1,25)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEVELOPMENT_SERVER = True
USE_CENTRAL_SERVER = True

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

LDAP_SERVER = "193.255.97.12"
LDAP_ADMIN_DN = "cn=admin,dc=comu,dc=edu,dc=tr"
LDAP_PASSWORD = "l4upprl"

SERVER_ADRESS = "http://127.0.0.1:8000"
EDUROAM_INFO_ADDRESS = "http://eduroam.comu.edu.tr"
EDUROAM_DOMAIN = "comu.edu.tr"
EDUROAM_EXCEPTION_DOMAIN = "gmail.com" # for test purposes

LINK_TIMEOUT = 3600 # link onayı için gerekli zaman sn olarak

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USER = 'some_user_name'
EMAIL_PASSWORD = 'some_password'
EMAIL_PORT = 587
TEXT_MAIL_FOOTER = u"Çanakkale Onsekiz Mart Üniversitesi\r\n\
	                Bilgi İşlem Dairesi Başkanlığı\r\n\
	                Tel : +90 286 218 00 18 - 1410\r\n\
	                Tel - Fax : +90 286 218 05 18\r\n"
HTML_MAIL_FOOTER = u"<p>Çanakkale Onsekiz Mart Üniversitesi<br />\
	                Bilgi İşlem Dairesi Başkanlığı<br />\
	                Tel : +90 286 218 00 18 - 1410<br />\
	                Tel - Fax : +90 286 218 05 18<br /> \
                   </p> \
                    </body> \
                    </html> \
                    "
EMAIL_FROM_DETAIL = "Bilgi İşlem Dairesi Başkanlığı <yardim@comu.edu.tr>"
EMAIL_FROM = "yardim@comu.edu.tr"

EMAIL_USE_TLS = True
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

# captcha settings
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_FONT_PATH = os.path.join(PROJECT_ROOT, "fonts", "Vera.ttf")
CAPTCHA_LENGTH = 6
CAPTCHA_FONT_SIZE = 30
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)

CAPTCHA_FOREGROUND_COLOR = "red"

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wirguldb',                      # Or path to database file if using sqlite3.
        'USER': 'wirguldbusr',                      # Not used with sqlite3.
        'PASSWORD': 'w1rg3l',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Istanbul'
#gettext = lambda s: sLANGUAGES = (('tr', _('TR')),('en', _('EN')),)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-EN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://127.0.0.1:8000/site_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '543@apto(=u#6&c*b_6q_v@f$4b6*#$&m7nv7m#=rfx4-79d1v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'wirgul.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wirgul.web',
    'captcha',
    # Uncomment the next line to enable the admin:
    #'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
