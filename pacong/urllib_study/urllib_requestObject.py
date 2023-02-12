import urllib.request

url = 'https://www.baidu.com'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
rp = urllib.request.urlopen(request)
print(rp.read().decode('utf-8'))