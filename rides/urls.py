from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', RidesView.as_view(), name='home'),
                       url(r'^draw/$', RideDrawView.as_view(), name='draw'),
                       url(r'^ride/(?P<pk>\d+)/$', RideView.as_view(), name='ride'),
                       url(r'^ride/(?P<pk>\d+)/edit/$', RideEditView.as_view(), name='edit'),
                       url(r'^popular/$', RidesPopularView.as_view(), name='popular'),
                       url(r'^upcoming/$', RidesUpcomingView.as_view(), name='upcoming'),
                       url(r'^ride/(?P<pk>\d+)/export/(?P<ext>gpx|kml)/$', ride_export, name='export'),
                       url(r'^ride/(?P<pk>\d+)/join/$', join, name='join'),
                       url(r'^ride/(?P<pk>\d+)/fave/$', fave, name='fave'))
