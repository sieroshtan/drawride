from django.conf.urls import patterns, url

urlpatterns = patterns('comments.views',
                       url(r'^ride/(\d+)/comment/$', 'post_comment', name='post_comment'))
