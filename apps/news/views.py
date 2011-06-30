# -*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.conf import settings


def all-news(request):
    return render(request, 'news/index.html', {})


def categories(request):
    return render(request, 'news/categories.html', {})
