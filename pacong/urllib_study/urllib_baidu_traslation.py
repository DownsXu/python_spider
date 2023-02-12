import urllib.request
import urllib.parse
import json

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1675929939322_1675948461470_TTnnzIDWldoVN2keNP+ANHAbJT4ou26Ta8kZPABDrsbvr/+7+Df0xN8rRDC7zZAWmXou7eEBGjxhiM4GzjDYUkISs4pnSh2jZx15VOTf3I290wUQejrGLl8RqoFUTPQDLYBurUkAhu4J2moIUFK8BLb/Mprx0dfbFa6wYxHEsVWmYIlKBQ4CKcRbhyJHeys1uI6U+Og8KqdA+DdnugJDVyL/LePVV8SfwYZ+AzFgAMM6R0lcFkh9xBBpVFf9d4BbnmyTbWwnn26G1OZffq5mkmCTOSyWx2uKygDNy3aQsKgbruy3JcJMWKZLKX1a9Tu5',
    'Connection': 'keep-alive',
    'Content-Length': '117',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=D6A842815ED68D1065EB14D8767C0886:FG=1; BIDUPSID=D6A842815ED68D1065EB14D8767C0886; PSTM=1664373384; BDUSS=GlBdGtpYnA3aU1QMmpEd0loTno0aWNBRDJvLTBFS1Y4Rn5zTFlwZ2NaZzZaN3RqSVFBQUFBJCQAAAAAAAAAAAEAAAA1hKTnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADrak2M62pNjR; BDUSS_BFESS=GlBdGtpYnA3aU1QMmpEd0loTno0aWNBRDJvLTBFS1Y4Rn5zTFlwZ2NaZzZaN3RqSVFBQUFBJCQAAAAAAAAAAAEAAAA1hKTnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADrak2M62pNjR; ZFY=m8PnWGmK28ot29yvl5:BLu0T8GeF20I4UeqHjMB2cwnM:C; BAIDUID_BFESS=D6A842815ED68D1065EB14D8767C0886:FG=1; __bid_n=184035e614c3ee425b4207; FEID=v10-83801b60be7a747d56bf9956fc05e19d3729bbbc; __xaf_fpstarttimer__=1672821397826; __xaf_thstime__=1672821397904; __xaf_fptokentimer__=1672821397928; FPTOKEN=d+58z0YCj3M9prdJiqq7aFfXNaXhauNGU3MWVqSkDFuhnR8x4pyg21pGpLKdPdJc95az68OEU93IJjNPwF4jGyZl+k10Ny43nrOLkYIbx/23YPYCiepTn+/n4QL48ZFRZ7pMH6xl0FE+h3erveEVSzFWRZLVgoMS8LeBCDHJcf83fDDaGRMTLpODtNYkWrsOYT8j6WPWoW/qWc1cY8BqUYQ1Gq2DHxBINHgXtv/sRyXFn8QBUMaD14o+eRdt6CsZoWa119e/ZzS9OLN/GHtuacXOL46PezDezGh+GK7ZiA5n7cbZfsFhrh90XqEXAcCmYByHrKtufyCxXNU/1VNloVH79FVhDTuDBQvlvxTcumOcYUfgLn3upF4IUrZdUg/DjdhsEV3u19N1suh+e6IkeA==|OWDzFNvOLP1lXzbonZdKJorrkvfpEHvnPaqnFh8pPX8=|10|242a3992831820d5d3b07209ca4b8383; RT="z=1&dm=baidu.com&si=ddb35875-eb13-4014-b250-ef435ca03876&ss=ldq0k8v3&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=2ja&hd=2ju"; BDRCVFR[NKud350Tv3c]=mk3SLVN4HKm; delPer=0; PSINO=3; H_PS_PSSID=; BA_HECTOR=ah0k0005200525008laha16b1hu9mjj1l; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1675948243; ab_sr=1.0.1_M2Q4MzQ2MmMwMTNlMmFhYjNjYmZkYTdlN2YxNmI5YjQ2ZjQwOWJmMGMyNjFlYTI4OWEyYWY1MzA5NDg1YWE3MTE1ZDY3ODMzYzg4ZjBhMzk4NTFjOTc2ODlkZTE4MDY5NTE1NWY3YWZmOWJlYmUwN2E4NjNjNzUzOTA1MTY3ZGUwMmM2MGU1ZDIyODYyOTgxYTk4MzE5ZmZlMjEwMWFmYTM2NWI0MGM2NjZhZmRjMmMyOTc3M2E2ZTU5NWQ3NmRj; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1675948461',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'd21e4baebae5118fd3a0b74c913023e0',
    'domain': 'common'
}

data = urllib.parse.urlencode(data).encode('utf-8')
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'


request = urllib.request.Request(url=url, data=data, headers=headers)
reponse = urllib.request.urlopen(request)

conetent = reponse.read().decode('utf-8')

json_data = json.loads(conetent)
print(json_data)