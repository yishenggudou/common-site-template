# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('control.views',
    url(r'^(?P<slug>.*)/$', 'service', name='service-page'),
)
