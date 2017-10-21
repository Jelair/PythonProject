# python 高级特性：生成器
g = (x * x for x in range(10))
print(next(g))

for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0 ,1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

def fibIter(max):
    n, a, b = 0, 0 ,1
    while n < max:
        #在执行过程中，遇到yield就中断，下次又继续执行
        yield b #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fibIter(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e)
        break

def triangles():
    L = [1]
    while True:
        yield L
        for i in range(1,len(L)):
            L[-i] = L[-i] + L[-i-1]

        L.append(1)
    return 'done'

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
