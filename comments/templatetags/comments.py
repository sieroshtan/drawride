from django import template
from django.contrib.contenttypes.models import ContentType
from comments.forms import *

register = template.Library()


@register.inclusion_tag('comments/form.html')
def comments_form(user, ride):
    return {'user': user,
            'form': CommentForm(),
            'ride_id': ride.id}


@register.inclusion_tag('comments/comments.html')
def comments(obj):
    comment_type = ContentType.objects.get_for_model(obj)
    return {'comments': Comment.objects.filter(content_type__pk=comment_type.id, object_id=obj.id)}
