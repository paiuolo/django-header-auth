from django.contrib.auth.middleware import RemoteUserMiddleware
from django.conf import settings


USERNAME_HEADER = getattr(
    settings, 'DJANGO_HEADER_AUTH_USERNAME_HEADER', 'HTTP_X_CONSUMER_USERNAME')


class DjangoHeaderAuthMiddleware(RemoteUserMiddleware):
    header = USERNAME_HEADER

    def clean_username(self, username, request):
        return super(DjangoHeaderAuthMiddleware, self).clean_username(username, request)
