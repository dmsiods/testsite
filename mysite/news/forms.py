from django import forms
from news.models import Category


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label='Наименование',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        required=False,
        label='Текст',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    is_published = forms.BooleanField(initial=True, label='Опубликовано')
    category = forms.ModelChoiceField(
        label='Категория',
        empty_label='Выберите категорию',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
