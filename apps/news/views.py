# -*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.conf import settings

from news.models import NewsPost, Category


'''To template:
posts - extracted posts
'''

def all_news(request):
    news_list = NewsPost.objects.filter(is_draft=False)
    #print reverse('category', args=['obshie'])
    return render(request, 'news/all_news.html', {'posts': news_list})


def categories(request):
    cats = Category.objects.all()
    return render(request, 'news/categories.html', {'categories': cats})


def category(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = cat.newspost_set.all()
    return render(request, 'news/category.html', {'posts': posts, 'category': cat})


def news_post(request, cat_slug, post_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = cat.newspost_set.all()
    post = get_object_or_404(posts, slug=post_slug)
    return render(request, 'news/news_post.html', {'post': post})
