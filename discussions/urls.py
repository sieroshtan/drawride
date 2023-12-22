from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("discussions", DiscussionsView.as_view(), name="discussions"),
    re_path(
        r"^discussion/(?P<username>[A-Za-z0-9_]+)$",
        DiscussionView.as_view(),
        name="discussion",
    ),
    re_path(r"^compose/(?P<username>[A-Za-z0-9_]+)$", compose, name="compose"),
]
