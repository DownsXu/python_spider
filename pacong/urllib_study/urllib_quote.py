import urllib.request
import urllib.parse

url = 'https://cn.bing.com/search?q='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
name = urllib.parse.quote('周杰伦')
url += name

request = urllib.request.Request(url=url, headers=headers)
reponse = urllib.request.urlopen(request)
content = reponse.read().decode('utf-8')
print(content)