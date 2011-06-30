from main.models import Services
from django import template

register = template.Library()

@register.inclusion_tag('main/tags/services_tag.html')
def services_list():
    services = Services.objects.all()
    return {"services": services}
