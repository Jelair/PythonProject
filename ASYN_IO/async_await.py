# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     async_await
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

@asyncio.coroutine
def hello():
    print('Hello world!')
    r = yield from asyncio.sleep(1)
    print('Hello again!')

# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。

async def hello():
    print('Hello world!')
    r = await asyncio.sleep(1)
    print('Hello again!')