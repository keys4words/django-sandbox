from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Home Page',
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': 'Category Page',
        'category': category,
    }

    return render(request, template_name='news/category.html', context=context)