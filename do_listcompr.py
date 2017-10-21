# python 高级特性：列表生成式
A = list(range(1,11))
print(A)

B = [x * x for x in range(1,11)]
print(B)

C = [x * x for x in range(1,11) if x % 2 == 0]
print(C)

D = [m + n for m in 'ABC' for n in 'XYZ']
print(D)

import os
#列出当前目录下的所有文件和目录名
E = [d for d in os.listdir('.')]
print(E)

d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
    print(k, "=", v)

F = [k+'='+v for k, v in d.items()]
print(F)

L = ['Hello', 'World', 'IBM', 'Apple']
G = [s.lower() for s in L]
print(G)

N = ['Hello', 'World', 18, 'Apple', None]
N = [n.lower() for n in N if isinstance(n, str)]
print(N)