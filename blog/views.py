from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # print(dir(request))
    return HttpResponse("<h2>Page blog</h2>")
