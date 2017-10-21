#函数的参数
# def power(x):
#     return x * x

def power(x, n=2): #n的默认参数为2, 注意必选参数在前
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2), power(2, 3))

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

print(calc([1,2,3])) #调用时先组装一个list或tuple

def calc2(*numbers): #定义为可变参数
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

print(calc2(1,2,3))

nums = [1,2,3]
print(calc(nums))
print(calc2(*nums))

def person(name, age, **kw): #kw获取一份拷贝
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Tom', 23, **extra)

#必选参数、默认参数、可变参数、命名关键字参数、关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)

f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

args = (1,2,3,4)
kw = {'d': 99, 'x' : '#'}
f1(*args, **kw)

def person(name, age, *, city, job):
    pass #命名关键字参数必须传入参数名，否则视为位置参数

def person(name, age, *args, city, job):
    pass #如果已有一个可变参数，则不再需要特殊分隔符*
