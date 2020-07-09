#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

"""
import unittest, os
from BeautifulReport import BeautifulReport


case_path = os.path.join(os.path.dirname("__file__"),os.path.pardir)
suite = unittest.defaultTestLoader.discover(case_path, pattern="*.py", top_level_dir=None)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    run = BeautifulReport(suite)
    run.report(filename='testCase', description="世界农场APP V1.2.7 接口测试")
