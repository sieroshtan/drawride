from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^users/$', UsersView.as_view(), name='users'),
                       url(r'^settings/$', SettingsView.as_view(), name='settings'),
                       url(r'^settings/password/$', SettingsPasswordView.as_view(), name='settings_password'),
                       url(r'^settings/photo/$', SettingsPhotoView.as_view(), name='settings_photo'),
                       url(r'^user/(?P<slug>[A-Za-z0-9_]+)/$', ProfileView.as_view(), name='profile'),
                       url(r'^(?P<slug>[A-Za-z0-9_]+)/drafts/$', ProfileDraftsView.as_view(), name='drafts'),
                       url(r'^(?P<slug>[A-Za-z0-9_]+)/involved/$', ProfileInvolvedView.as_view(), name='involved'),
                       url(r'^(?P<slug>[A-Za-z0-9_]+)/favorite/$', ProfileFavoritesView.as_view(), name='favorite'))
