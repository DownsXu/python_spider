import requests
import json
import openpyxl

wk = openpyxl.Workbook()
sheet = wk.create_sheet()  # 创建表格

# 在Pycharm中运行需要加请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
rep = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100009790789&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',headers=headers)
content = rep.text.replace('fetchJSON_comment98(', '').replace(');', '')
# print(content)
json_data = json.loads(content)
com = json_data['comments']
for item in com:
    color = item['productColor']
    name = item['nickname']
    content = item['content']
    sheet.append([name, color, content])
    wk.save('D:/FJVCC/img/comment_data.xlsx')


