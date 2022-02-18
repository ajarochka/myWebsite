from django import template
from firstapp.models import Category, News
from django.db.models import *

register = template.Library()

@register.simple_tag()
def find_category():
    # categories = Category.objects.annotate(cnt=Count('news').filter(cnt__gt=0))
    # categories = Category.objects.values(max=Max('news__views'))
    # return Category.objects.all()

    allCategories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return categories

# @register.simple_tag()
@register.inclusion_tag('firstapp/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
