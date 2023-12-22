import re
import random
import hashlib
from django.template.loader import render_to_string
from django.db.models import Manager
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings


SHA1_RE = re.compile('^[a-f0-9]{40}$')


class ActivationManager(Manager):
    def activate_user(self, activation_key):
        if SHA1_RE.search(activation_key):
            try:
                user = self.get(activation_key=activation_key)
            except self.model.DoesNotExist:
                return False

            user.is_active = True
            user.activation_key = 'ALREADY_ACTIVATED'
            user.save()
            return user
        return False

    def create_inactive_user(self, username, email, password):
        new_user = get_user_model().objects.create_user(username, email, password)
        new_user.is_active = False

        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1((salt+username).encode('utf-8')).hexdigest()

        new_user.activation_key = activation_key
        new_user.save()

        ctx_dict = {'activation_key': activation_key}
        subject = _("Drawride | Email verification")

        message = render_to_string('registration/activation_email.html',
                                   ctx_dict)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, (email,))

        return new_user
