#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Tim Yao'

import orm_demo
import asyncio
from www.models import User


async def test(loop):
    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    __pool = await orm_demo.create_pool(loop, host='127.0.0.1', user='root', password='123456', database='test')
    #没有设置默认值的一个都不能少
    u = User(id='123', name='Test')
    await u.save(__pool)

#把协程丢到事件循环中执行

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()