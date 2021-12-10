from django.shortcuts import render
from django.http import HttpResponse
from .crawling import crawl
from django.http import Http404
from bs4 import BeautifulSoup as bs
import requests
from urllib.parse import ParseResult


def mail(request):
    data = crawl()[0]
    return render(request, 'mail_main.html', {'data': data})


def mail_detail(request, pk):
    data = crawl()[0]
    #data = saved().data
    url = ParseResult(scheme='https', netloc='gall.dcinside.com', path='/board/view/',
                      params='', query='id=gongik_new&no=' + data[pk]['write_num'] + '&page=1', fragment='')
    url = url.geturl()  # url 생성

    header = {'User-agent': '*'}
    html = requests.get(url, headers=header)
    soup = bs(html.content, "html.parser")
    글내용 = soup.find_all(class_="write_div")  # 글내용 스크래핑
    data[pk]['content'] = 글내용  # db에 추가
    # print(글내용)
    if pk >= len(data):
        raise Http404('게시글을 찾을 수 없습니다')
    else:
        data = data[pk]
    return render(request, 'mail_detail.html', {'data': data})
