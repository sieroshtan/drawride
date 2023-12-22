from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r"^user/(?P<username>[A-Za-z0-9_]+)/follow$", follow, name="follow"),
    re_path(r"^user/(?P<username>[A-Za-z0-9_]+)/unfollow$", unfollow, name="unfollow"),
    re_path(
        r"^(?P<slug>[A-Za-z0-9_]+)/followers$",
        FollowersView.as_view(),
        name="followers",
    ),
    re_path(
        r"^(?P<slug>[A-Za-z0-9_]+)/following$",
        FollowingView.as_view(),
        name="following",
    ),
]
