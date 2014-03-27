from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^about/$',
                           AboutView.as_view(),
                           name='about'))
