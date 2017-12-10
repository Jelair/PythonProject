import os

print(os.name)
#print(os.uname())

#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)
#要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径
mpath = os.path.abspath('.')
print(mpath)
#在某个目录下创建一个新目录
newpath = os.path.join(mpath, 'file.txt')
#然后创建一个目录
os.mkdir(newpath)
#删除一个目录
os.rmdir(newpath)
#列出当前目录下的所有目录
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)
#列出所有的.py文件
f = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(f)