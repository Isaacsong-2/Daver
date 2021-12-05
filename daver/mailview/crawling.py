import requests
from bs4 import BeautifulSoup as bs
import os


def crawl():
    url = "https://gall.dcinside.com/board/lists/?id=gongik_new"
    header = {'User-agent': '*'}
    html = requests.get(url, headers=header)
    soup = bs(html.content, "html.parser")

    # 제목
    cnt = 0
    제목 = soup.find_all(class_="gall_tit ub-word")
    title = []
    for q in 제목:
        if cnt < 2:
            cnt += 1
        else:
            if q.get_text()[-2] == ']':
                # db['title'] = q.get_text()[1:-5]
                title.append(q.get_text()[1:-5])
            else:
                # db['title'] = q.get_text()[1:-2]
                title.append(q.get_text()[1:-2])
    # print(title)
    # 글쓴이
    글쓴이 = soup.find_all(class_="nickname")
    writer = []
    for q in 글쓴이:
        # db['writer'] = q.get_text()
        writer.append(q.get_text())
    # print(writer)
    # 작성일
    cnt = 0
    작성일 = soup.find_all(class_="gall_date")
    date = []
    for q in 작성일:
        if cnt < 2:
            cnt += 1
        else:
            # db['date'] = q.get_text()
            date.append(q.get_text())
    # print(date)
    # 조회수
    cnt = 0
    조회수 = soup.find_all(class_="gall_count")
    count = []
    for q in 조회수:
        if cnt < 2:
            cnt += 1
        else:
            # db['count'] = q.get_text()
            count.append(q.get_text())
    # print(count)
    db = {}
    db['title'] = title
    db['writer'] = writer
    db['date'] = date
    db['count'] = count
    return db
# print(len(title), len(writer), len(date), len(count))
