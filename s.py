import urllib3
import os
import re
import requests
from bs4 import BeautifulSoup

url = 'https://filmarks.com/movies/14348'
bsURL = requests.get(url)
soup = BeautifulSoup(bsURL.text, 'html.parser')
review_texts = soup.select(".p-mark__review")
#print(review_texts)

move_title = str(soup.select(".p-content-detail__title > span")[0].text)
# dir_n = re.match(r'.*<span>(.*?)</span>.*', move_title).group(1)
last_page = soup.select_one(".c-pagination__last")
if last_page:
        last_page_num= int(last_page.get('href').split("=")[-1])
else:
        last_page_num = 0
# print(dir_n)
print(move_title)
for zero in range(last_page_num):
    hoge_url = url + '?page='+str(zero)+''
    hoge_bsURL = requests.get(hoge_url)
    hoge_soup = BeautifulSoup(hoge_bsURL.text, 'html.parser')
    review_texts += hoge_soup.select(".p-mark__review")
    print(zero)
    print(hoge_url)
print(str(review_texts))
path = move_title
os.makedirs('data')
if os.path.exists(path) == False:
    path = 'data/' + path
    os.makedirs(path)
if os.path.exists(path) == True:
    print("すでに完了しています")
path += '/review.txt'
tmppath = 'list.txt'
with open(path, mode='w') as f:
    f.write(str(review_texts))
with open(tmppath, mode='w') as g:
    g.write(move_title)
