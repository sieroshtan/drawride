from django.db import models
from django.utils import timezone


class RideManager(models.Manager):
    def rides(self, is_hide=False):
        return self.filter(is_hide=is_hide).annotate(members_count=models.Count('members'))

    def popular(self, user):
        popular_rides = self.rides().order_by('-members_count')
        if user.is_authenticated and user.city:
            return popular_rides.filter(city=user.city)
        return popular_rides

    def upcoming(self, user):
        upcoming_rides = self.rides().filter(start_time__gte=timezone.now()).order_by('start_time')
        if user.is_authenticated and user.city:
            return upcoming_rides.filter(city=user.city)
        return upcoming_rides

    def following(self, following):
        return self.rides().filter(user__in=following)


class RideMembersManager(models.Manager):
    def is_member(self, ride, user):
        try:
            self.get(ride=ride, user=user)
            return True
        except models.ObjectDoesNotExist:
            return False


class UserFavoritesManager(models.Manager):
    def is_favorite(self, ride, user):
        try:
            self.get(ride=ride, user=user)
            return True
        except models.ObjectDoesNotExist:
            return False
