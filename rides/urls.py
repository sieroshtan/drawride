from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", RidesView.as_view(), name='home'),
    path('draw/', RideDrawView.as_view(), name='draw'),
    path("ride/<int:pk>/", RideView.as_view(), name='ride'),
    path("ride/<int:pk>/edit/", RideEditView.as_view(), name='edit'),
    path("ride/<int:pk>/navigation/", RideNavigationView.as_view(), name='navigation'),
    path('popular/', RidesPopularView.as_view(), name='popular'),
    path('upcoming/', RidesUpcomingView.as_view(), name='upcoming'),
    re_path(r"^ride/(?P<pk>\d+)/export/(?P<ext>gpx|kml)/$", ride_export, name='export'),
    path("ride/<int:pk>/join/", join, name='join'),
    path("ride/<int:pk>/fave/", fave, name='fave')
]
