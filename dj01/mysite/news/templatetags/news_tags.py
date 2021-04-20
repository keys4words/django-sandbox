from django import template

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_categories_list')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='One', arg2='Two'):
    categories = Category.objects.all()
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}