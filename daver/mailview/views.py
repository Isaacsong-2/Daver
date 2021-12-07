from django.shortcuts import render
from django.http import HttpResponse
from .crawling import crawl
from django.http import Http404
from bs4 import BeautifulSoup as bs
import requests


def index(request):
    data = crawl()
    return render(request, 'mail_main.html', {'data': data})


def mail_detail(request, pk):
    data = crawl()
    print(len(data))
    url = "https://m.dcinside.com/board/gongik_new/2329281"
    header = {'User-agent': '*'}
    html = requests.get(url, headers=header)
    soup = bs(html.content, "html.parser")
    #글내용 = soup.find_all(class_="gall_tit ub-word")
    # print(글내용)
    if pk >= len(data):
        raise Http404('게시글을 찾을 수 없습니다')
    else:
        data = data[pk]
    return render(request, 'mail_detail.html', {'data': data})
