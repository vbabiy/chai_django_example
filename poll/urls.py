from django.conf.urls.defaults import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^show/(?P<poll_id>\d+)/$', show, name='show'),
)
