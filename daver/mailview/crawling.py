import requests
from bs4 import BeautifulSoup as bs
import re
url = "https://gall.dcinside.com/board/lists/?id=gongik_new"
header = {'User-agent': '*'}
html = requests.get(url, headers=header)
soup = bs(html.content, "html.parser")
# for child in soup.em.children:
# print(child)
글 = soup.find(class_="ub-content us-post")
제목 = 글.find(class_="gall_tit ub-word").get_text()
# print(글)
print(제목)
# for x in range(0, 1):
#     print(soup.select(".gall_tit ub-word").get_text())
