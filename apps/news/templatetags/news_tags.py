from news.models import Category
from django import template

register = template.Library()

@register.inclusion_tag('news/tags/get_all_categories.html')
def get_all_categories():
    categories = Category.objects.all()
    return {"categories": categories}
