from django import template
from follow.models import Follow

register = template.Library()


@register.inclusion_tag("follow/follow_button.html")
def follow_button(follower, followee):
    return {
        "followee": followee.username,
        "follows": Follow.objects.follows(follower, followee),
    }
