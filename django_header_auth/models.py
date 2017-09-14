from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings

from .functions import create_uuid, domain_email_extract


class ConsumerManager(auth_models.BaseUserManager):

    def create_user(self, domain, email, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and
        password.
        """
        now = timezone.now()

        if not domain:
            raise ValueError('Users must have a domain')
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username field')

        print("creating user", "with domain", domain,
              "email", email, 'username', username)

        consumer = self.model(
            domain=domain, email=email, username=username,
            is_staff=False, is_active=True,
            is_superuser=False,
            last_login=now, created_at=now, **extra_fields)

        if password:
            consumer.set_password(password)

        consumer.save(using=self._db)
        return consumer

    def create_superuser(self, domain, email, username, password, **extra_fields):
        u = self.create_user(domain, email, username, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class Consumer(auth_models.AbstractUser):
    uuid = models.CharField(max_length=64, default=create_uuid, unique=True)
    updated_at = models.DateTimeField(_('date updated'), null=True, blank=True)

    domain = models.CharField(_('consumer domain'), max_length=255)
    email = models.EmailField(_('email address'))

    objects = ConsumerManager()

    DOMAIN_FIELD = 'domain'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['domain', 'email']

    @property
    def is_alive(self):
        return self.is_active

    class Meta:
        unique_together = (("domain", "email"),)

    def get_full_name(self):
        full_name = '%s %s' % (self.domain, self.email)
        return full_name.strip()

    def get_short_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()
