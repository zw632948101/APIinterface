#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:17
__author__: wei.zhang
__remark__: 消息
"""
from .. import FarmQuery


class MessagesQuery(FarmQuery):
    def __init__(self):
        super(MessagesQuery, self).__init__()
        self.level = 'MessagesQuery'
