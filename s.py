import urllib3
import re
import requests
from bs4 import BeautifulSoup

url = 'https://filmarks.com/movies/7420'
bsURL = requests.get(url)
soup = BeautifulSoup(bsURL.text, 'html.parser')
review_texts = soup.select(".p-mark__review")
#print(review_texts)

last_page = soup.select_one(".c-pagination__last")
if last_page:
        last_page_num= int(last_page.get('href').split("=")[-1])
else:
        last_page_num = 0
for zero in range(last_page_num):
    hoge_url = url + '?page='+str(zero)+''
    hoge_bsURL = requests.get(hoge_url)
    hoge_soup = BeautifulSoup(hoge_bsURL.text, 'html.parser')
    review_texts += hoge_soup.select(".p-mark__review")
print(str(review_texts))
path = 'review.txt'

with open(path, mode='w') as f:
    f.write(str(review_texts))
