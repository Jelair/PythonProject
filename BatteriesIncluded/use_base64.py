import base64

# 对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit
enStr = base64.b64encode(b'binary\x00string')
print(enStr)
deStr = base64.b64decode(enStr)
print(deStr)

# 由于标准的Base64编码后可能出现字符+和/，
# 在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，
# 其实就是把字符+和/分别变成-和_
enStr2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(enStr2)
enStr3 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(enStr3)
deStr3 = base64.urlsafe_b64decode(enStr3)
print(deStr3)