from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import News, Category
from .forms import NewsForm


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


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'title': 'News',
        'news_item': news_item
        }
    return render(request, template_name='news/view_news.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm()
    else:
        form = NewsForm()
        
    context = {
        'title': 'Add news',
        'form': form
    }
    return render(request, 'news/add_news.html', context)
