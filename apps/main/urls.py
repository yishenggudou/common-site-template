# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
    url(r'^$', 'homepage', name='home-page'),
    url(r'^about/$', 'about', name='about-page'),
    url(r'^contacts/$', 'contacts', name='contacts-page'),
)
