import requests
from bs4 import BeautifulSoup as bs
import re
url = "https://gall.dcinside.com/board/lists/?id=gongik_new"
header = {'User-agent': '*'}
html = requests.get(url, headers=header)
soup = bs(html.content, "html.parser")

# 제목
제목 = soup.find_all(class_="gall_tit ub-word")
title = []
for q in 제목:
    title.append(q.get_text())
print(title)
# 글쓴이
제목 = soup.find_all(class_="nickname")
writer = []
for q in 제목:
    writer.append(q.get_text())
print(writer)
# 작성일
cnt = 0
작성일 = soup.find_all(class_="gall_date")
date = []
for q in 작성일:
    if cnt < 2:
        cnt += 1
    else:
        date.append(q.get_text())
print(date)
# 조회수
cnt = 0
조회수 = soup.find_all(class_="gall_count")
count = []
for q in 조회수:
    if cnt < 2:
        cnt += 1
    else:
        count.append(q.get_text())
print(count)
