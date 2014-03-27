from django.db import models
from django.utils import timezone
from .managers import FollowingManager
from django.conf import settings


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following')
    followee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers')
    created = models.DateTimeField(default=timezone.now)

    objects = FollowingManager()

    class Meta:
        unique_together = ('follower', 'followee')
