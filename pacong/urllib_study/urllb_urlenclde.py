import urllib.request
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
base_url = 'https://cn.bing.com/search?'

data = {
    'q': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

# 完整请求资源路径
url = base_url + urllib.parse.urlencode(data)

# 定制请求对象
request = urllib.request.Request(url=url, headers=headers)

reponse = urllib.request.urlopen(request)
print(reponse.read().decode('utf-8'))