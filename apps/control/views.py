# -*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.conf import settings

from control.models import Services

def service(request, slug):
    serv = get_object_or_404(Services, slug=slug)
    return render(request, 'control/service.html', {'service': serv})
