# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from news.feed import LatestNewsFeed

urlpatterns = patterns('news.views',
    # rss
    url(r'^feed/$', LatestNewsFeed()),

    url(r'^$', 'all_news', name='all-news-page'), # all news in page with pagination
    url(r'^categories/$', 'categories', name='categories-page'), # categories with descriptions
    url(r'^(?P<cat_slug>.*)/(?P<post_slug>.*)/$', 'news_post', name='news-post-page'),
    url(r'^(?P<cat_slug>.*)/$', 'category', name='category-page'),

)
