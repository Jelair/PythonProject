
from PIL import Image

#************** 图像缩放操作 *****************
# 打开一个jpg图像文件，注意是当前路径
im = Image.open('test.jpg')
# 获得图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存
im.save('thumbnail.jpg', 'jpeg')

# 应用模糊滤镜
from PIL import ImageFilter
im2 = Image.open('thumbnail.jpg').filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')