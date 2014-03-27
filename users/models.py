import os
import string
from random import choice

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from geo.models import City


def get_file_path(user, filename):
    return 'avatars/%i/%s.%s' % (user.id,
                                 ''.join(choice(string.ascii_letters + string.digits) for _ in range(9)),
                                 filename.split('.')[-1].lower())


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('n', _('Not specified')),
        ('m', _('Male')),
        ('f', _('Female')),
    )

    LANGUAGES = (
        ('ru', 'Russian'),
        ('en', 'English'),
    )

    username = models.CharField(max_length=45, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True)

    name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(default='n', max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(max_length=1000, blank=True)
    lang = models.CharField(max_length=2, choices=LANGUAGES, blank=True)
    photo = models.ImageField(upload_to=get_file_path)
    city = models.ForeignKey(City, null=True, blank=True)

    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ('email',)

    objects = UserManager()

    def get_name(self):
        return self.name or self.username

    def get_photo(self):
        if self.photo and os.path.isfile(os.path.join(settings.MEDIA_ROOT, self.photo.name)):
            return settings.MEDIA_URL + self.photo.name
        return settings.STATIC_URL + 'img/avatar-default.png'

    def get_absolute_url(self):
        return reverse('profile', args=(self.username,))
