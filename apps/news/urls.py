# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('news.views',
    url(r'^$', 'all_news', name='all-news-page'), # all news in page with pagination
    url(r'^categories/$', 'categories', name='categories-page'), # categories with descriptions
)
