#import builtins
# 修改abs变量的指向在其他模块也生效
#builtins.abs = 10

def add(x , y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

from functools import reduce
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

reduce(fn, map(char2num, '13679'))

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
d = list(r)
print(d)

import functools
#一个完整的decorator的写法
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#针对带参数的decorator
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可

@log2('execute')
def now():
    print('2017-12-09')
now()

#匿名函数
f = lambda x: x * x
print(f(5))

#偏函数（Partial function）
#所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)
a = int2('100000')
print(a)