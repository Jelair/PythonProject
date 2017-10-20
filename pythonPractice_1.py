#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

str = '亲爱的用户%s,您的话费余额为%f。' % ("张先生",5.9)
print(str)
#list
classmates = ['Michael','Bob','Make']
size_classmate = len(classmates)
print(classmates)
print(size_classmate)
#获取第一个元素
print(classmates[0])
#获取倒数第一个元素
print(classmates[-1])
#追加元素到末尾
classmates.append('Adam')
print(classmates)
#将元素插入到指定位置
classmates.insert(1,'Jack')
print(classmates)
#删除list末尾的元素
classmates.pop()
print(classmates)
#删除指定位置元素
classmates.pop(1)
print(classmates)

#tuple 一旦初始化就不能修改
students = ('Michael','Bob','Tracy',['Hello,World',123,"abc"])
print(students)
students[3][2] = 'Good'
print(students)
