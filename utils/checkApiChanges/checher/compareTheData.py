#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = "yong.guo"
__data__ = "2019/07/27"
"""
import codecs
import os, sys
import time
from utils.environmentConfiguration import config
from utils.log import log
from utils.checkApiChanges.checher.askDatabaseForApiData import AskDatabaseForApiData
from utils.checkApiChanges.checher.askSwaggerForIApiData import AskSwaggerForApiData


class CompareTheData(object):
    def __init__(self, env):
        self.hosts = config.get('hosts').get(env)

    def statistics_api(self):
        adfa = AskDatabaseForApiData()
        asfa = AskSwaggerForApiData()
        for key, host in self.hosts.items():
            self.check_result = {"new_info": {}, "del_info": {}, "update_info": {}}
            self.database_data = adfa.get_database_data(host)
            swagger = asfa.swagger_result(host)
            if swagger is None or host is None:
                continue
            self.swagger_data, self.swagger_tags = swagger
            self.__cmp_config()
            self.data_check()
            adfa.updata_database(self.check_result, host)
            self.get_eidt_api_statistics(key, host)
            self.get_edit_api_excel_statistics(key, host)

    def __cmp_config(self):
        # 初始化比较结果映射关系
        self.new_api = {"cmp_result": ["new_api"]}
        self.new_in_parameter = {"cmp_result": ["new_in_parameter"]}
        self.new_ext_parameter = {"cmp_result": ["new_ext_parameter"]}
        self.new_api_desc = {"cmp_result": ["new_desc"]}
        self.new_api_method = {"cmp_result": ["new_method"]}

        self.del_api = {"cmp_result": ["del_api"]}
        self.del_in_parameter = {"cmp_result": ["del_in_parameter"]}
        self.del_ext_parameter = {"cmp_result": ["del_ext_parameter"]}
        self.del_api_desc = {"cmp_result": ["del_api_desc"]}
        self.del_api_method = {"cmp_result": ["del_api_method"]}

        self.update_in_parameter = {"cmp_result": ["update_in_parameter"]}
        self.update_ext_parameter = {"cmp_result": ["update_ext_parameter"]}
        self.update_api_desc = {"cmp_result": ["update_api_desc"]}
        self.update_api_method = {"cmp_result": ["update_api_method"]}

        self.api_key_map_method = "method"
        self.api_key_map_inParameter = "inParameter"
        self.api_key_map_outParameter = "outParameter"
        self.api_key_map_desc = "desc"

    def data_check(self):
        # 检查方法
        def api_info_checker(key: str, database_data):
            if key == self.api_key_map_method:
                tmp_str = "请求方法"
                tmp_method_new = self.new_api_method.get("cmp_result")
                tmp_method_del = self.del_api_method.get("cmp_result")
                tmp_method_update = self.update_api_method.get("cmp_result")
                old_name = "old_" + key
            elif key == self.api_key_map_inParameter:
                tmp_str = "入参"
                tmp_method_new = self.new_in_parameter.get("cmp_result")
                tmp_method_del = self.del_in_parameter.get("cmp_result")
                tmp_method_update = self.update_in_parameter.get("cmp_result")
                old_name = "old_" + key

            elif key == self.api_key_map_outParameter:
                tmp_str = "出参"
                tmp_method_new = self.new_ext_parameter.get("cmp_result")
                tmp_method_del = self.del_ext_parameter.get("cmp_result")
                tmp_method_update = self.update_ext_parameter.get("cmp_result")
                old_name = "old_" + key

            elif key == self.api_key_map_desc:
                tmp_str = "描述"
                tmp_method_new = self.new_api_desc.get("cmp_result")
                tmp_method_del = self.del_api_desc.get("cmp_result")
                tmp_method_update = self.update_api_desc.get("cmp_result")
                old_name = "old_" + key

            else:
                raise KeyError("传入参数错误")

            if self.swagger_data.get(check_api).get(key) != self.database_data.get(check_api).get(key):
                # 数据被删除
                if self.swagger_data.get(check_api).get(key) is None:
                    log.info("接口%s %s被删除" % (check_api, tmp_str))
                    self.check_result.get("update_info").get(check_api).get("cmp_result"). \
                        append(tmp_method_del)
                    self.check_result.get("update_info").get(check_api).update(
                        {old_name: self.database_data.get(check_api).get(key)})
                # 数据新增
                elif self.swagger_data.get(check_api).get(key) is None:
                    log.info("接口%s 新增%s" % (check_api, tmp_str))
                    self.check_result.get("update_info").get(check_api).get("cmp_result"). \
                        append(tmp_method_new)
                    self.check_result.get("update_info").get(check_api).update(
                        {old_name: self.database_data.get(check_api).get(key)})

                # 数据修改
                else:
                    log.info("接口%s %s发生更新" % (check_api, tmp_str))
                    self.check_result.get("update_info").get(check_api).get("cmp_result"). \
                        append(tmp_method_update)
                    self.check_result.get("update_info").get(check_api).update(
                        {old_name: self.database_data.get(check_api).get(key)})

        log.info("检查数据库和服务器返回的数据")
        if self.database_data != self.swagger_data:

            # 以服务器返回的数据为准，进行全遍历，并将对比过的数据删除
            for check_api in list(self.swagger_data.keys()):
                # 检查接口是否在数据库中存在
                try:
                    if check_api in self.database_data.keys():

                        log.debug("检查接口%s是否有变更" % check_api)
                        if self.swagger_data.get(check_api) != self.database_data.get(check_api):
                            # 接口发生变更，将变更数据记录到结果中
                            self.check_result.get("update_info").update({check_api: self.swagger_data.get(check_api)})
                            self.check_result.get("update_info").get(check_api).update({"cmp_result": []})

                            # 检查接口描述
                            # api_info_checker(self.api_key_map_desc, self.database_data)
                            # 检查接口方法
                            api_info_checker(self.api_key_map_method, self.database_data)
                            # 检查接口入参
                            api_info_checker(self.api_key_map_inParameter, self.database_data)
                            # 检查接口出参
                            api_info_checker(self.api_key_map_outParameter, self.database_data)

                        # 检查完成后，将接口从数据中删除，方便下次遍历检查
                        self.swagger_data.__delitem__(check_api)
                        self.database_data.__delitem__(check_api)

                    else:
                        # 数据库中没有的接口，走新增数据流程
                        log.debug("发现有新增接口%s" % check_api)
                        self.check_result.get("new_info").update({check_api: self.swagger_data.get(check_api)})
                        self.check_result.get("new_info").get(check_api).update(self.new_api)
                        self.swagger_data.__delitem__(check_api)
                except AttributeError:
                    log.error("数据库未配置swagger地址或地址错误")
                    exit(0)

            # 剩余database_data中是数据，是服务器删除的数据
            if 0 < len(self.database_data.items()):
                log.debug("发现有删除接口%s" % ",".join(list(self.database_data.keys())))
                self.check_result.get("del_info").update(self.database_data)

    def get_eidt_api_statistics(self, file_name, host_name):
        now = time.strftime("_%Y-%m-%d_%H%M%S", time.localtime())
        current_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
        if not os.path.exists(current_path + "/Attachment/EditApi"):
            os.makedirs(current_path + "/Attachment/EditApi")
        with codecs.open(current_path + "/Attachment/EditApi/" + str(file_name) + now + '.txt', 'a', 'utf-8') as f:
            for keys in self.check_result.keys():
                if keys != 'del_info':
                    f.write(keys + '\n')
                    info_d = self.check_result.get(keys)
                    for k, v in info_d.items():
                        api_info = self.swagger_tags.get(k)
                        tags = api_info.get('tags')
                        tags = tags + ' ' + v.get('desc')
                        f.write('%s%s, %s\n' % (host_name, k, tags))

    def get_edit_api_excel_statistics(self, file_name, host_name):
        """
        生成Excel文件
        :param file_name:
        :param host_name:
        :return:
        """
        import xlwt
        book = xlwt.Workbook()
        sheet = book.add_sheet(str(file_name))
        now = time.strftime("_%Y-%m-%d_%H%M%S", time.localtime())
        current_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
        excel_title = ["编号", "服务", "地址", "接口", "模块", "说明", "测试", "测试情况"]
        c = 0
        for i in range(len(excel_title)):
            sheet.write(c, i, excel_title[i])
        c += 1
        for keys in self.check_result.keys():
            if keys != 'del_info':
                sheet.write(c, 0, keys)
                c += 1
                info_d = self.check_result.get(keys)
                for k, v in info_d.items():
                    if not k.find('/api/') or not k.find('/web/'):
                        continue
                    api_info = self.swagger_tags.get(k)
                    excel_value = [c - 1, file_name, host_name, k, api_info.get('tags'), v.get('desc')]
                    for i in range(len(excel_value)):
                        sheet.write(c, i, excel_value[i])
                    c += 1
        book.save(current_path + "/Attachment/EditApi/" + str(file_name) + now + '.xls')
