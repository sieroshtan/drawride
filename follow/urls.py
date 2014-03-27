from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^user/(?P<username>[A-Za-z0-9_]+)/follow/$', follow, name='follow'),
                       url(r'^user/(?P<username>[A-Za-z0-9_]+)/unfollow/$', unfollow, name='unfollow'),
                       url(r'^(?P<slug>[A-Za-z0-9_]+)/followers/$', FollowersView.as_view(), name='followers'),
                       url(r'^(?P<slug>[A-Za-z0-9_]+)/following/$', FollowingView.as_view(), name='following'))
