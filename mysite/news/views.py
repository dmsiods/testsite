from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from news.models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')

    context = {
        'news': news,
        'title': 'Список новостей'
    }

    return render(request, template_name='news/index.html', context=context)


def test(request):
    # import pdb; pdb.set_trace()

    # return HttpResponse('<h1>Тестовая страница</h1>')

    return render(request, 'news/test.html', {})


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)

    return render(request, 'news/view_news.html', {'news_item': news_item})
