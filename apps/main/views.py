# -*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.conf import settings

from django.shortcuts import render_to_response


def homepage(request):
    return render(request, 'main/home.html', {})

def about(request):
    return render(request, 'main/about.html', {})

def contacts(request):
    return render(request, 'main/contacts.html', {})
