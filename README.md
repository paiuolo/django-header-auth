# django-header-auth
Django remote headers driven authentication.


## Quick start

1. Add "django_header_auth" to your INSTALLED_APPS setting like this:
    ```python
    INSTALLED_APPS = [
        ...
        'django_header_auth',
    ]
    ```
2. Set the default django user model and setup authentication middleware and backends in settings file:
    ```python
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
    ```
    
3. Include the django_header_auth URLconf in your project urls.py like this:
    ```python
    from django_header_auth.urls import urlpatterns as consumers_urls

    url(r'^django_header_auth/', include(consumers_urls)),
   ```
4. Run `python manage.py migrate` to create the django_header_auth models.


### Todos

 - Write MORE Tests
 
### Contribute

Visit the [github page](https://github.com/paiuolo/django-header-auth/) to participate in the poll.

License
----

MIT

