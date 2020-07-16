#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/9/11'
"""
from functools import wraps


def judge_response_status(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        json_response = func(*args, **kwargs)
        if json_response['status'] in ("OK", "ERROR"):
            return json_response
        else:
            raise Exception('status未返回OK或ERROR')

    return wrapper
