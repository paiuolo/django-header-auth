from django.contrib.auth.middleware import RemoteUserMiddleware
from django.conf import settings


class DjangoHeaderAuthMiddleware(RemoteUserMiddleware):
    header = getattr(settings, 'DJANGO_HEADER_AUTH_USERNAME_HEADER', 'HTTP_X_CONSUMER_USERNAME')
    print('header', header)
    def clean_username(self, username, request):
        print('ma porca troia', username)
        return super(DjangoHeaderAuthMiddleware, self).clean_username(username, request)