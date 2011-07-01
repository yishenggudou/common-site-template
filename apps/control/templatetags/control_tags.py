from control.models import Services, ContentBlock
from django import template

register = template.Library()

@register.inclusion_tag('control/tags/get_all_services.html')
def get_all_services():
    services = Services.objects.all()
    return {'services': services}


@register.inclusion_tag('control/tags/show_content.html')
def show_content(block_id):
    try:
        content = ContentBlock.objects.get(block_id=block_id)
    except ContentBlock.DoesNotExist:
        content = {'content': "Can't find %s" % block_id}
    return {'content': content}
