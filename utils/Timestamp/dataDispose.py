#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/10 16:18
# @Author: wei.zhang
# @File : dataDispose.py
# @Software: PyCharm
import copy


class dataDispose(object):
    def __init__(self):
        super(dataDispose, self).__init__()

    def inspect_name(self, data_dict, **kwargs):
        import copy
        add_data = []
        for k in kwargs.keys():
            for i in kwargs.get(k):
                cp_dict = copy.deepcopy(data_dict)
                cp_dict[k] = i
                add_data.append(cp_dict)
        return add_data

    def recursion_dispose_data_list(self, value: list, lst1=[], lst2=[]):
        """
        生成测试数据,生成列表
        :param value: 传值必须是二维列表
        :param lst1:
        :param lst2:
        :return:
        """
        lst = value.copy()
        l = lst.pop(0)
        if len(value) > 1:
            for i in l:
                ll = lst1.copy()
                ll.append(i)
                self.recursion_dispose_data_list(lst, ll)
        if len(value) == 1:
            for i in l:
                ll = lst1.copy()
                ll.append(i)
                lst2.append(ll)
        return lst2

    def recursion_dispose_data_dict(self, dic={}, lst2=[], **kwargs):
        """
        生成测试数据,生成字典
        :param kwargs:
        :param dic:
        :param lst2:
        :return:
        """
        lst = list(kwargs.keys())
        l = lst.pop(0)
        kl = kwargs.pop(l)
        if len(lst) > 0:
            for i in kl:
                d = copy.deepcopy(dic)
                d[l] = i
                self.recursion_dispose_data_dict(dic=d, lst2=lst2, **kwargs)
        if len(lst) == 1:
            for i in kl:
                d = copy.deepcopy(dic)
                d[l] = i
                lst2.append(d)
        return lst2
