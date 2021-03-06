# django-header-auth
Django header driven authentication.

Integrate header driven user logic into django

Detailed documentation is in the "docs" directory.

## Quick start

1. Add "django_header_auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_header_auth',
    ]
    
2. Set the default django user model and setup authentication middleware and backends in settings file::

    AUTH_USER_MODEL = 'django_header_auth.Consumer'
    
    MIDDLEWARE = [
        '...',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django_header_auth.middleware.RemoteUserMiddleware',
        '...',
    ]
    
    AUTHENTICATION_BACKENDS = [
        'django_header_auth.backends.RemoteUserBackend',
    ]
    
3. Include the django_header_auth URLconf in your project urls.py like this::
    
    from django_header_auth.urls import urlpatterns as consumers_urls

    url(r'^django_header_auth/', include('consumers_urls')),
    
4. Run `python manage.py migrate` to create the django_header_auth models.
    
5. Visit http://127.0.0.1:8000/django_header_auth/ to participate in the poll.
    