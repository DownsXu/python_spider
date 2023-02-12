import urllib.request
# 爬取的url
url = 'http://www.baidu.com'
# 发起请求
reponse = urllib.request.urlopen(url)
# 读取内容
content = reponse.read().decode('utf-8')
print(content)