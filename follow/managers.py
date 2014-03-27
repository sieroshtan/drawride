from django.db import models
from django.db import IntegrityError


class FollowingManager(models.Manager):
    def add_follower(self, follower, followee):
        try:
            self.create(follower=follower, followee=followee)
            return True
        except IntegrityError:
            return False

    def remove_follower(self, follower, followee):
        try:
            self.get(follower=follower, followee=followee).delete()
            return True
        except models.ObjectDoesNotExist:
            return False

    def followers(self, user):
        qs = self.filter(followee=user).all()
        return [u.follower for u in qs]

    def following(self, user):
        qs = self.filter(follower=user).all()
        return [u.followee for u in qs]

    def follows(self, follower, followee):
        try:
            self.get(follower=follower, followee=followee)
            return True
        except models.ObjectDoesNotExist:
            return False
