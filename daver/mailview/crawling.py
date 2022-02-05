import requests
from bs4 import BeautifulSoup as bs
import os
from urllib.parse import ParseResult


def crawl():
    url = "https://gall.dcinside.com/board/lists/?id=gongik_new"
    header = {'User-agent': '*'}
    html = requests.get(url, headers=header)
    soup = bs(html.content, "html.parser")

    # 제목
    제목 = soup.find_all(class_="gall_tit ub-word")
    title = []
    for q in 제목:
        if q.get_text()[-2] == ']':
            # db['title'] = q.get_text()[1:-5]
            title.append(q.get_text()[1:-5])
        else:
            # db['title'] = q.get_text()[1:-2]
            title.append(q.get_text()[1:-1])
    # 글쓴이
    글쓴이 = soup.find_all(class_="nickname")
    writer = []
    for q in 글쓴이:
        # db['writer'] = q.get_text()
        writer.append(q.get_text())
    # 작성일
    작성일 = soup.find_all(class_="gall_date")
    date = []
    for q in 작성일:
        # db['date'] = q.get_text()
        date.append(q.get_text())
    # 조회수
    조회수 = soup.find_all(class_="gall_count")
    count = []
    for q in 조회수:
        # db['count'] = q.get_text()
        count.append(q.get_text())
    # 글 번호
    글번호 = soup.find_all(class_="gall_num")
    write_num = []
    for q in 글번호:
        write_num.append(q.get_text())
    # print('1')
    # db만들기
    k = len(title) - len(writer)  # 공지글 제외
    data = []
    for i in range(len(writer)):
        db = {}
        db['title'] = title[i+k]
        db['writer'] = writer[i]
        db['date'] = date[i+k]
        db['count'] = count[i+k]
        db['id'] = str(int(write_num[k])-int(write_num[i+k]))
        db['write_num'] = write_num[i+k]
        data.append(db)
    # print(data)

    # 이미지 여부
    # 이미지 = soup.find_all(class_='gall_tit ub-word')
    # img = []
    # cnt = 0
    # for q in 이미지:
    #     cnt += 1
    #     print(q)
    #     img.append(q)

    # print(cnt)
    # print(img)
    # url = ParseResult(scheme='https', netloc='gall.dcinside.com', path='/board/view/',
    #                   params='', query='id=gongik_new&no=' + data[pk]['write_num'] + '&page=1', fragment='')
    # url = url.geturl()
    return data

# print(len(title), len(writer), len(date), len(count))
