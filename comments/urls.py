from django.urls import path
from comments.views import post_comment

urlpatterns = [path("ride/<int:ride_id>/comment", post_comment, name="post_comment")]
