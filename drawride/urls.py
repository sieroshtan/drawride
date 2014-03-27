from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
                       url('', include('main.urls')),
                       url('', include('registration.urls')),
                       url('', include('users.urls')),
                       url('', include('discussions.urls')),
                       url('', include('follow.urls')),
                       url('', include('rides.urls')),
                       url('', include('comments.urls')),
                       url('', include('search.urls')),
                       url('', include('geo.urls')))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
