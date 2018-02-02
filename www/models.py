#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Tim Yao'

'''
Models for user, blog, comment.
'''

import time, uuid
from orm import Model, StringField, BooleanField, IntegerField, TextField


def next_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    name = StringField(ddl='varchar(100)')

