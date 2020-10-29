"""
! /usr/bin/env python3
-*- coding: UTF-8 -*-
@Time:2020/10/29 9:30
@Author: he.chao
@File : attrManage.py
@Software: PyCharm
@modular:属性管理
"""
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import mp_label
from utils import runlevel
from ddt import data, ddt
from faker import Faker
import unittest
import random
import os
from utils.excelRead import excelRead
from utils.changData import changData
from jsonpath import jsonpath