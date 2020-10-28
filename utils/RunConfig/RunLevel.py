#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/10/28 09:43
# @Author: wei.zhang
# @File : RunLevel.py
# @Software: PyCharm

from utils.environmentConfiguration import config
from utils.log import log

class RunLevel(object):
    @staticmethod
    def skip_case(case_level):
        """
        判断是否需要跳过用例
        设置执行用例等级5个，按优先级执行
        1.主流程执行用例，保证接口调通，非必填字段全部填写
        2.主流程执行用例，保证接口调通，非必填字段可用不填写
        3.分支流程，校验必填字段错误类型
        4.分支流程，校验非必填字段错误类型
        5.其他
        :param level: 用例等级
        :return: 返回布尔值
        """
        run_level = config.get('RUN_LEVEL')
        if run_level > 5:
            log.info('设置跳过运行等级不能大于5')
            return
        if 0 < run_level <= case_level:
            return True
        return False
