from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # print(dir(request))

    return HttpResponse('Hello world!')


def test(requesr):
    return HttpResponse('<h1>Тестовая страница</h1>')
