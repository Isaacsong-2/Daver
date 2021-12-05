from django.shortcuts import render
from django.http import HttpResponse
from .crawling import crawl


def index(request):
    data = crawl()
    # writer = crawling.writer
    # date = crawling.date
    # count = crawling.count
    print(data)
    return render(request, '1.html', {'data': data})
