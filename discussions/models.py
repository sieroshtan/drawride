from django.db import models
from .managers import MessageManager, MessageContactManager
from django.conf import settings


class Message(models.Model):
    text = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_users')
    from_user_deleted = models.BooleanField(default=False)
    to_user_deleted = models.BooleanField(default=False)
    readed = models.BooleanField(default=False)

    objects = MessageManager()

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)

        MessageContact.objects.update_contact(self.from_user,
                                              self.to_user,
                                              self)

    class Meta:
        ordering = ('id',)


class MessageContact(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages')
    latest_message = models.ForeignKey(Message)
    from_user_deleted = models.BooleanField(default=False)
    to_user_deleted = models.BooleanField(default=False)

    objects = MessageContactManager()

    class Meta:
        unique_together = ('from_user', 'to_user')
        ordering = ('-latest_message',)
