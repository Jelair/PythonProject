#import builtins
# 修改abs变量的指向在其他模块也生效
#builtins.abs = 10

def add(x , y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))
