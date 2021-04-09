from django.shortcuts import render
from django.http import HttpResponse

from .models import News


# Create your views here.
def index(request):
    news = News.objects.order_by('-created_at')
    # res = '<h1>List of News</h1>'
    # for el in news:
    #     res += f'<div><p>{el.title}</p><p>{el.content}</p></div><hr>'
    # return HttpResponse(res)
    context = {
        'news': news,
        'title': 'News Page'
    }
    return render(request, 'news/index.html', context)


def test(request):
    return HttpResponse('<h1>Answer</h1>')