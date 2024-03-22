from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(active_category=None):
    categories = Category.objects.filter(news__is_published=True).annotate(news_count=Count('news')).filter(news_count__gt=0)

    return {'categories': categories, 'active_category': active_category}
