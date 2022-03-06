from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # print(dir(request))
    return HttpResponse("<h3>Page news</h3>")


def test(request):
    # print(dir(request))
    return HttpResponse("<h1>Тестовая страница</h1>")


# Create your views here.
