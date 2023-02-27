from PIL import ImageFilter
from PIL import Image

im = Image.open('D:/FJVCC/img/iu.jpg')
ess = im.filter(ImageFilter.CONTOUR)
ess.save('D:/FJVCC/img/iu2.jpg')
