from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from news.forms import NewsForm
from news.models import News, Category


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}  # для статичных данных

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def index(request):
#     news = News.objects.order_by('-created_at')
#
#     context = {
#         'news': news,
#         'title': 'Список новостей'
#     }
#
#     return render(request, template_name='news/index.html', context=context)


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


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)

        if form.is_valid():
            news = form.save()

            return redirect(news)

    else:
        form = NewsForm()

    return render(request, 'news/add_news.html', {'form': form})
