import requests
from bs4 import BeautifulSoup

url = 'https://s.weibo.com/top/summary?cate=realtimehot'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
hot_list = soup.select('.td-02 a')

for i, item in enumerate(hot_list, 1):
    print(i, item.text.strip())
