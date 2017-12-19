# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     do_mysql
   Description :
   Author :       simplefly
   date：          2017/12/18
-------------------------------------------------
   Change Activity:
                   2017/12/18:
-------------------------------------------------
"""
__author__ = 'simplefly'

# 导入MySQL驱动
import mysql.connector
# 注意把password设为你的root口令
conn = mysql.connector.connect(user='root', password='root', database = 'ssh') # 此处需先创建数据库，否则会报错（Unknow database）
cursor = conn.cursor()
# 创建user表
cursor.execute('create table user (id varchar(20) PRIMARY KEY , name varchar(20))')
# 插入一行记录, 注意MySQL的占位符是%s
cursor.execute('insert into user (id, name) VALUES (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection
cursor.close()
conn.close()