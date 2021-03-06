from django.conf.urls import patterns, url
from .views import *
from .forms import LoginForm


urlpatterns = patterns('',
                       url(r'^signup/$', SignUpView.as_view(), name='signup'))


urlpatterns += patterns('',
                        url(r'^activate/(?P<activation_key>\w+)/$',
                            ActivationView.as_view(),
                            name='registration_activate'),

                        url(r'^login/$',
                            'django.contrib.auth.views.login',
                            {'template_name': 'registration/login.html', 'authentication_form': LoginForm},
                            name='login'),

                        url(r'^logout/$',
                            'django.contrib.auth.views.logout',
                            {'next_page': '/'},
                            name='logout'),

                        url(r'^recover/$', 'registration.views.custom_password_reset', name='recover'),

                        url(r'^reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                            'registration.views.custom_password_reset_confirm',
                            name='reset_confirm'))
