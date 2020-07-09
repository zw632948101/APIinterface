#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:17
__author__: wei.zhang
__remark__: 登录与注册
"""
from .. import FarmQuery


class LoginAndRegister(FarmQuery):
    def __init__(self):
        super(LoginAndRegister, self).__init__()
        self.level = 'LoginAndRegister'
