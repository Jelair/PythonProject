# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     do_sqlalchemy
   Description :
   Author :       simplefly
   date：          2017/12/18
-------------------------------------------------
   Change Activity:
                   2017/12/18:
-------------------------------------------------
"""
__author__ = 'simplefly'

# ORM(Object-Relational Mapping),把关系数据库的表结构映射到对象上
# 导入
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 穿件对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接 '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/ssh')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

#****************向数据库表中添加一条记录*****************
# 创建session对象
session = DBSession()
# 创建新User对象
new_user = User(id='5', name='Bob')
# 添加到session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭session
session.close()

#*****************从数据库中查询数据*******************
# 创建Session
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性
print('type', type(user))
print('name', user.name)
# 关闭Session
session.close()

# ****************** 定义一对多 **********************
# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多
#     books = relationship('Book')
#
# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表示通过外键关联到user表的
#     user_id = Column(String(20), ForeignKey('user.id'))