# python 高级特性：迭代
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

for ch in 'ABC':
    print(ch)

from collections import Iterable
print(isinstance('abc', Iterable))
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A','B','C']):
    print(i, value)

for x, y in [(1,1), (2,4), (3,9)]:
    print(x, y)


#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#Python的for循环本质上就是通过不断调用next()函数实现的