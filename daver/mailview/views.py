from django.shortcuts import render
from django.http import HttpResponse
from .crawling import crawl


def index(request):
    db = crawl()
    # writer = crawling.writer
    # date = crawling.date
    # count = crawling.count
    print(db)
    return render(request, '1.html', db)
