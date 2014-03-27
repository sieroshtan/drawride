from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^cities/$', CitiesView.as_view(), name='cities'),
                       url(r'^city/(?P<pk>\d+)/$', CityView.as_view(), name='city'),
                       url(r'^city/(?P<pk>\d+)/people/$', CityPeopleView.as_view(), name='city_people'),
                       url(r'^change_city/$', ChangeCityView.as_view(), name='change_city'),
                       url(r'^set_city/(?P<pk>\d+)/$', SetCityView.as_view(), name='set_city'))
