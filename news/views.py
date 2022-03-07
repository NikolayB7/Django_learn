from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import News


# def index(request):
#     news = News.objects.all()
#     res = "<h3>Список новостей</h3>"
#     for item in news:
#         res += f"<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n"
#     return HttpResponse(res)


def index(request):
    news = News.objects.order_by("-creates_at")
    context = {"news": news, "title": "Список новостей"}
    return render(request, "news/index.html", context)


# Create your views here.
