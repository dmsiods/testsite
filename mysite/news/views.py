from django.shortcuts import render
from django.http import HttpResponse

from news.models import News


def index(request):
    # print(dir(request))

    news = News.objects.order_by('-created_at')

    context = {
        'news': news,
        'title': 'Список новостей'
    }

    return render(request, template_name='news/index.html', context=context)


def test(requesr):
    # import pdb; pdb.set_trace()

    return HttpResponse('<h1>Тестовая страница</h1>')
