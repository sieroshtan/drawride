from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone
from django.conf import settings
from comments.models import Comment
from .managers import RideManager, RideMembersManager, UserFavoritesManager
from geo.models import City


class Ride(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='his_rides')
    title = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    points = models.TextField()
    distance = models.FloatField()
    description = models.CharField(max_length=1000, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='RideMembers', related_name='members')
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, through='UserFavorites', related_name='favorites')
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=0, related_name='rides')
    is_hide = models.BooleanField(default=False)
    comments = GenericRelation(Comment)

    objects = RideManager()

    def points_string(self):
        points = self.points.split(',')[::-1]
        return ','.join(points[:200])

    def static_url(self):
        return settings.MAP_STATIC_URL + self.points_string()

    def get_absolute_url(self):
        return reverse('ride', args=(self.id,))

    class Meta:
        ordering = ['-id']


class RideMembers(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)

    objects = RideMembersManager()

    class Meta:
        unique_together = ('ride', 'user')
        ordering = ('-id',)


class UserFavorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)

    objects = UserFavoritesManager()

    class Meta:
        unique_together = ('ride', 'user')
        ordering = ('-id',)
