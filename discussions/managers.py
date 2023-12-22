from django.db import models
from django.db.models import Q


class MessageManager(models.Manager):
    def compose(self, from_user, to_user, text):
        message = self.model(from_user=from_user, to_user=to_user, text=text)
        message.save()
        message.update_contacts(to_user)

    def get_conversation_between(self, from_user, to_user):
        return self.filter(
            Q(from_user=from_user, to_user=to_user, from_user_deleted=False)
            | Q(from_user=to_user, to_user=from_user, to_user_deleted=False)
        )

    def new_messages(self, user):
        return self.filter(to_user=user, to_user_deleted=False, readed=False)

    def set_as_read(self, user, contact):
        return self.filter(
            to_user=user, from_user=contact, readed=False, to_user_deleted=False
        ).update(readed=True)

    def set_as_delete_from(self, from_user, to_user):
        self.filter(from_user=from_user, to_user=to_user, from_user_deleted=False).update(
            from_user_deleted=True
        )

    def set_as_delete_to(self, from_user, to_user):
        self.filter(from_user=to_user, to_user=from_user, to_user_deleted=False).update(
            to_user_deleted=True
        )


class MessageContactManager(models.Manager):
    def get_or_create(self, from_user, to_user, message):
        created = False
        try:
            contact = self.get(
                Q(from_user=from_user, to_user=to_user) | Q(from_user=to_user, to_user=from_user)
            )
        except self.model.DoesNotExist:
            created = True
            contact = self.create(from_user=from_user, to_user=to_user, latest_message=message)
        return contact, created

    def update_contact(self, from_user, to_user, latest_message):
        contact, created = self.get_or_create(from_user, to_user, latest_message)
        if not created:
            contact.latest_message = latest_message
            contact.from_user_deleted = False
            contact.to_user_deleted = False
            contact.save()
        return contact

    def get_contacts_for(self, user):
        return self.filter(
            (Q(to_user=user) & Q(to_user_deleted=False))
            | (Q(from_user=user) & Q(from_user_deleted=False))
        )

    def set_as_delete(self, user1, user2):
        contact = self.get(
            Q(to_user=user1) & Q(from_user=user2) | Q(to_user=user2) & Q(from_user=user1)
        )

        if contact.to_user == user1:
            contact.to_user_deleted = True
        else:
            contact.from_user_deleted = True
        return contact.save()
