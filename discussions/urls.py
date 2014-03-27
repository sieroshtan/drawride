from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^discussions/$', DiscussionsView.as_view(), name='discussions'),
                       url(r'^discussion/(?P<username>[A-Za-z0-9_]+)/$', DiscussionView.as_view(), name='discussion'),
                       url(r'^compose/(?P<username>[A-Za-z0-9_]+)/$', compose, name='compose'))
