# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     coroutine
   Description :
   Author :       simplefly
   date：          2017/12/19
-------------------------------------------------
   Change Activity:
                   2017/12/19:
-------------------------------------------------
"""
__author__ = 'simplefly'
# 生产者生产消息后，直接通过yield跳转到消费者开始执行，
# 待消费者执行完毕后，切换回生产者继续生产，效率极高
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)