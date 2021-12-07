from django.shortcuts import render
from django.http import HttpResponse
from .crawling import crawl
from django.http import Http404


def index(request):
    data = crawl()
    # writer = crawling.writer
    # date = crawling.date
    # count = crawling.count
    print(data)
    return render(request, 'mail_main.html', {'data': data})


def mail_detail(request, pk):
    data = crawl()
    try:
        data = data[pk]
    except data[pk] >= len(data):
        raise Http404('게시글을 찾을 수 없습니다')
    return render(request, 'mail_detail.html', {'data': data})
