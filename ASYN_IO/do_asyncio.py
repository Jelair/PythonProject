# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     do_asyncio
   Description :
   Author :       simplefly
   date：          2017/12/19
-------------------------------------------------
   Change Activity:
                   2017/12/19:
-------------------------------------------------
"""
__author__ = 'simplefly'

import asyncio

# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO

@asyncio.coroutine
def hello():
    print('Hello world!')
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('Hello again!')

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
#loop.close()

import threading
@asyncio.coroutine
def hello2():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello2(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
