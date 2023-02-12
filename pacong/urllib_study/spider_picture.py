'''
活动名(学时) - 是否结束 - 活动时间 - 报名人数/限制人数 - 举办单位
//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[1]/a/div[1]/div[2]/div[1]/div/text()
//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[2]/a/div[1]/div[2]/div[1]/div/text()

//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[1]/a/div[1]/div[2]/div[1]/div/span
//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[2]/a/div[1]/div[2]/div[1]/div/span

//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[1]/a/div[1]/div[2]/div[1]/span
//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[2]/a/div[1]/div[2]/div[1]/span

//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[1]/a/div[1]/div[2]/div[2]/span
//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[3]/a/div[1]/div[2]/div[2]/span

//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[1]/a/div[2]/div[2]/span
//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[2]/a/div[2]/div[2]/span

//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[1]/a/div[2]/div[1]/p
//*[@id="app"]/div[2]/div/div/div[2]/div/div[5]/ul/div[1]/li[3]/a/div[2]/div[1]/p
'''

import urllib.request
import lxml.etree


def creat_request():
    url = 'https://cn.bing.com/images/search?q=iu&first=1'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'cookie': 'SUB=_2AkMUu4arf8NxqwJRmP4RzW3lZYh-ygDEieKi53dwJRMxHRl-yT9kqhEotRB6PzuoRIjRGxTW-FJVy0rZgPPjMhrTzD1z; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFK-Ubr2rumoyq.m0srz8IR; _s_tentry=-; Apache=8456275613106.201.1676087266901; SINAGLOBAL=8456275613106.201.1676087266901; ULV=1676087266903:1:1:1:8456275613106.201.1676087266901:'
    }

    rq = urllib.request.Request(url=url, headers=headers)
    return rq


def create_content(request):
    reponse = urllib.request.urlopen(request)
    content = reponse.read().decode('utf-8')
    return content


if __name__ == '__main__':
    # 定制请求头
    request = creat_request()
    # 发起请求
    content = create_content(request)
    print(content)
