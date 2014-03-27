from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    text = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ('id',)
