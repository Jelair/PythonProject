# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     do_flask
   Description :
   Author :       simplefly
   date：          2017/12/18
-------------------------------------------------
   Change Activity:
                   2017/12/18:
-------------------------------------------------
"""
__author__ = 'simplefly'

# 一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应
# def application(environ, start_response):
#     method = environ['REQUEST_METHOD']
#     path = environ['PATH_INFO']
#     if method=='GET' and path=='/':
#         return handle_home(environ, start_response)
#     if method=='POST' and path='/signin':
#         return handle_signin(environ, start_response)

from flask import Flask
from flask import request

app = Flask(__name__)

# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
                  <p><input name="username"></p>
                  <p><input name="password" type="password"></p>
                  <p><button type="submit">Sign In</button></p>
                  </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
        app.run()