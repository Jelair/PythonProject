# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     do_wsgi
   Description :
   Author :       simplefly
   date：          2017/12/18
-------------------------------------------------
   Change Activity:
                   2017/12/18:
-------------------------------------------------
"""
__author__ = 'simplefly'

# WSGI : Web Server Gateway Interface
# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!<h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]