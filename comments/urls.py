from django.urls import path
from comments.views import ride_comments, post_comment

urlpatterns = [
    path("ride/<int:ride_id>/comment", post_comment, name="post_comment"),
    path("ride/<int:ride_id>/comments", ride_comments, name="ride_comments"),
]
