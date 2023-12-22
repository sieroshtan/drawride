from django import template
from discussions.forms import MessageForm
from discussions.models import Message

register = template.Library()


@register.inclusion_tag("dialogs/form.html")
def message_form(to_user):
    return {"to_user": to_user, "form": MessageForm()}


@register.filter
def new_messages_count(user):
    return Message.objects.new_messages(user).count()
