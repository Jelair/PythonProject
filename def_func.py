import math
#def
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def nop():
    pass

#my_abs('A')

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x, y)
print(r)
#151.96152422706632 70.0 其实是返回一个tuple，多个变量接受值按位置赋值
#(151.96152422706632, 70.0)

#practice
def quadratic(a, b, c):
    pass


