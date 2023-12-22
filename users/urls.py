from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("users/", UsersView.as_view(), name='users'),
    path("settings/", SettingsView.as_view(), name='settings'),
    path("settings/password/", SettingsPasswordView.as_view(), name='settings_password'),
    path("settings/photo/", SettingsPhotoView.as_view(), name='settings_photo'),
    re_path(r"^user/(?P<slug>[A-Za-z0-9_]+)/$", ProfileView.as_view(), name='profile'),
    re_path(r"^(?P<slug>[A-Za-z0-9_]+)/drafts/$", ProfileDraftsView.as_view(), name='drafts'),
    re_path(r"^(?P<slug>[A-Za-z0-9_]+)/involved/$", ProfileInvolvedView.as_view(), name='involved'),
    re_path(r"^(?P<slug>[A-Za-z0-9_]+)/favorite/$", ProfileFavoritesView.as_view(), name='favorite')
]
