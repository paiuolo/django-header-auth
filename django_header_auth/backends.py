from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import Group

from .functions import domain_email_extract, extract_groups


UserModel = get_user_model()
GROUPS_HEADER = getattr(settings, 'DJANGO_HEADER_AUTH_GROUPS_HEADER', 'HTTP_X_CONSUMER_GROUPS')

class DjangoHeaderAuthBackend(RemoteUserBackend):
    """
    Consumer authentication backend
    """
    def authenticate(self, request, remote_user):
        print('authenticate', request, remote_user)
        """
        The username passed as ``remote_user`` is considered trusted. Return
        the ``User`` object with the given username. Create a new ``User``
        object if ``create_unknown_user`` is ``True``.
        Return None if ``create_unknown_user`` is ``False`` and a ``User``
        object with the given username is not found in the database.
        """
        if not remote_user:
            return
        user = None
        
        domain, email = self.clean_username(remote_user)

        # Note that this could be accomplished in one try-except clause, but
        # instead we use get_or_create when creating unknown users since it has
        # built-in safeguards for multiple threads.
        user, created = UserModel._default_manager.get_or_create(**{
            UserModel.DOMAIN_FIELD: domain,
            UserModel.EMAIL_FIELD: email
        })
        if created:            
            user = self.configure_user(request, user)

        return user if self.user_can_authenticate(user) else None
        
    def clean_username(self, username):
        """
        Perform any cleaning on the "username" prior to using it to get or
        create the user object.  Return the cleaned username.
        By default, return the username unchanged.
        """
        return domain_email_extract(username)

    def configure_user(self, request, user):
        """
        Configure a user after creation and return the updated user.
        By default, return the user unmodified.
        """
        username = '{0}@{1}'.format(user.email, user.domain)
        groups = extract_groups(request.META.get(GROUPS_HEADER, 'users'))

        user.username = username
        
        for group in groups:
            group, _created = Group.objects.get_or_create(name=group)
            print('created group', group, user)
            group.user_set.add(user)
            
        if 'admin' in groups:
            user.is_staff = True
            user.is_active = True
            user.is_superuser = True
        
        user.save()

        return user