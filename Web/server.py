# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     server
   Description :
   Author :       simplefly
   date：          2017/12/18
-------------------------------------------------
   Change Activity:
                   2017/12/18:
-------------------------------------------------
"""
__author__ = 'simplefly'
# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数
from Web.do_wsgi import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()