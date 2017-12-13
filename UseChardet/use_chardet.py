

import chardet
# 使用chardet检测编码
result = chardet.detect(b'Hello, world!')
print(result)

data = '离离原上草，一岁一枯荣'.encode('utf-8')
result2 = chardet.detect(data)
print(result2)

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))