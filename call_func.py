# abs 绝对值
abs(100)
abs(-100)
abs(12.34)

# max 最大值
max(1, 2)
max(2, 3, 1, -5)

# 数据类型转换
int('123')
int(12.34)
float('12.34')

str(1.23)
str(100)

bool(1)
bool('')

# 函数名其实就是指向一个函数对象的引用
a = abs
a(-1)

# practice 转16进制
n1 = 255
n2 = hex(n1)
nn3 = str(n2)
print('hellow,%s', n1) #hellow,%s 255
