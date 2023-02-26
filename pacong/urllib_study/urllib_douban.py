from lxml import etree
import urllib.request
# import openpyxl

# wk = openpyxl.Workbook()
# sheet = wk.create_sheet()  # 创建表格

url = 'https://s.weibo.com/top/summary'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie':'SUB=_2AkMUu4arf8NxqwJRmP4RzW3lZYh-ygDEieKi53dwJRMxHRl-yT9kqhEotRB6PzuoRIjRGxTW-FJVy0rZgPPjMhrTzD1z; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFK-Ubr2rumoyq.m0srz8IR; _s_tentry=-; Apache=8456275613106.201.1676087266901; SINAGLOBAL=8456275613106.201.1676087266901; ULV=1676087266903:1:1:1:8456275613106.201.1676087266901:'
}

request = urllib.request.Request(url=url, headers=headers)
reponse = urllib.request.urlopen(request)
content = reponse.read().decode('utf-8')

tree = etree.HTML(content)

for item in range(1,52):
    result = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr[' + str(item) + ']/td[2]/a/text()')[0]
    # sheet.append([item-1, result])
    # wk.save('D:/FJVCC/img/top.xlsx')
    print(str(item-1) + ' ' + result)







