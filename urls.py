# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from news.sitemap import NewsSitemap

sitemaps = {
    # put your app sitemap here
    'news': NewsSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),                       
    url(r'', include('main.urls', namespace='main', app_name='main')),
    url(r'^news/', include('news.urls', namespace='news', app_name='news')),
    url(r'^service/', include('control.urls', namespace='control', app_name='control')),

    # sitemap and rss
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
       {'sitemaps': sitemaps}, name='sitemap')
)


# static urls will be disabled in production mode
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
