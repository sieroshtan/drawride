from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('', include('main.urls')),
    path('', include('registration.urls')),
    path('', include('users.urls')),
    path('', include('discussions.urls')),
    path('', include('follow.urls')),
    path('', include('rides.urls')),
    path('', include('comments.urls')),
    path('', include('search.urls')),
    path('', include('geo.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
