ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'django_header_auth.Consumer'

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_header_auth.middleware.DjangoHeaderAuthMiddleware',
    
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'django_header_auth',
    'django_extensions'
)

AUTHENTICATION_BACKENDS = [
    'django_header_auth.backends.DjangoHeaderAuthBackend',
]
