# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),                       
    (r'', include('main.urls', namespace='main', app_name='main')),
    (r'^news/', include('news.urls', namespace='news', app_name='news')),
)


# static urls will be disabled in production mode
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
