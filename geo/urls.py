from django.urls import path
from .views import *

urlpatterns = [
    path("cities", CitiesView.as_view(), name='cities'),
    path("city/<int:pk>", CityView.as_view(), name='city'),
    path("city/<int:pk>/people", CityPeopleView.as_view(), name='city_people'),
    path("change_city", ChangeCityView.as_view(), name='change_city'),
    path("set_city/<int:pk>", SetCityView.as_view(), name='set_city')
]
