from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from mysite import settings
from news.forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from news.models import News, Category


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegisterForm()

    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2

    # extra_context = {'title': 'Главная'}  # для статичных данных

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])

        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id']).select_related('category')


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'


# def test(request):
#     # import pdb; pdb.set_trace()
#
#     objects = ['object1', 'object2', 'object3', 'object4', 'object5', 'object6', 'object7']
#
#     paginator = Paginator(objects, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#
#     return render(request, 'news/test.html', {'page_obj': page_objects})


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], settings.EMAIL_HOST_USER,
                             ['vitokaif@gmail.com'], fail_silently=True)

            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('test')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации формы')
    else:
        form = ContactForm()

    return render(request, 'news/test.html', {'form': form})

# def get_category(request,category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#
#     return render(request, 'news/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#
#     return render(request, 'news/view_news.html', {'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#
#         if form.is_valid():
#             news = form.save()
#
#             return redirect(news)
#
#     else:
#         form = NewsForm()
#
#     return render(request, 'news/add_news.html', {'form': form})
