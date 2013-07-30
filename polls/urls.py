__author__ = 'Yusdenis'

from django.conf.urls import  patterns, url

from polls  import  views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/(?P<client_id>\d+)$', views.create, name='create'),
    url(r'^lista/(?P<poll_id>\d+)$', views.polls, name='polls'),
)