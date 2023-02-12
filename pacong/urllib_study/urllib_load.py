import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
url_img = 'https://pic1.zhimg.com/v2-5ab650f7dd654f6b1c62ed7a394f8609_r.jpg'
urllib.request.urlretrieve(url=url_img, filename='D:/FJVCC/img/iu.jpg')