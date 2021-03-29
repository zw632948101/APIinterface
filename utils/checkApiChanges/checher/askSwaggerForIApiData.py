#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from utils.log import log
import json
import copy


class InternalServerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print('请求服务器异常：%s' % self.msg)


class AskSwaggerForApiData(object):
    tmp_last_operate_str = None

    def __init__(self):
        pass

    def swagger_result(self, host):
        host = host + '/v2/api-docs'
        self.__tmp_swagger_response = self.__get_swagger_response(host)
        if self.__tmp_swagger_response.get('errorCode') == 500:
            log.info('请求服务器失败')
            raise InternalServerError(host)
        return self.__swagger_response_processing()

    def __get_swagger_response(self, swagger_url: str) -> dict:
        """
        从swagger上请求接口数据，并生成一个dict
        :param swagger_url: 需要请求的swagger地址
        :return: 接口字典
        """
        try:
            log.info("获取接口数据,获取地址：%s" % swagger_url)
            return json.loads(requests.get(swagger_url).content.decode("UTF-8"))
        except Exception as e:
            log.error(e)

    def __get_swagger_path_data(self, path: str):
        try:
            # 检查是否是definitions中更多元素，且为避免无限循环，检查返回的数据中是否有当前路径
            if path.startswith("#/definitions/"):
                tmp_path = path.split("/")
                result = self.__tmp_swagger_response.get(tmp_path[1]).get(tmp_path[2]).get("properties")
                result = json.dumps(result)
                result = json.loads(result.replace(path, "itself" + path))
                return result
            else:
                return path
        except AttributeError:
            # 后端不规范引起错误
            log.warning("服务器未告知%s数据结构，原样返回" % path)
            return path

    def __dict_data_operation(self, data):
        """
        操作的数据对象是多层次字典对象，将该字典对象中，满足特定条件的value进行替换
        :param data: 任意类型   swagger返回的paths
        :return:同传入的data类型
        """
        # 检查传入的数据是否是字典，若是字典需要检查每个元素是否含有特定字符(替换)
        if isinstance(data, dict):
            # 注意： 字典在遍历过程中不能操作key,若需要操作key,可以遍历字典key的list，写法如：for dict_key in list(data.keys)
            for dict_key in data:
                # 字典中还有可能再次套用一个字典，因此需要检查该字典中的值
                if isinstance(data.get(dict_key), dict):
                    data.update({dict_key: self.__dict_data_operation(data.get(dict_key))})
                # 当需要操作当字段名称是$ref，值不是dict时，说明该字典当value需要进行操作
                elif dict_key == "$ref":
                    data.update({
                        dict_key: self.__dict_data_operation(
                            self.__get_swagger_path_data(data.get(dict_key))
                        )})

            # 数据检查完成后，返回操作完成的数据
            return data
        else:
            # 当入参不是字典时，直接返回原有数据
            return data

    def __swagger_response_processing(self):
        log.info("处理swagger数据")
        try:
            tmp_swagger_response = self.__dict_data_operation(self.__tmp_swagger_response.get("paths"))
            tmp_swagger_response_tages = copy.deepcopy(tmp_swagger_response)
        except AttributeError as e:
            log.error(e)
            return
        for api in tmp_swagger_response:
            method = list((tmp_swagger_response.get(api).keys()))[0]
            tmp_swagger_response.get(api).update({"method": method})
            tmp_swagger_response.get(api).update({"desc": tmp_swagger_response.get(api).get(method).get("summary")})
            method_tags = list((tmp_swagger_response_tages.get(api).keys()))[0]
            tmp_swagger_response_tages.get(api).update({"method": method_tags})
            tmp_swagger_response_tages.get(api).update(
                {"tags": tmp_swagger_response_tages.get(api).get(method).get("tags")[0]})
            tmp_swagger_response_tages.get(api).update(
                {"desc": tmp_swagger_response_tages.get(api).get(method).get("summary")})
            try:
                tmp_swagger_response.get(api).update(
                    {"inParameter": tmp_swagger_response.get(api).get(method).pop("parameters")})
                tmp_swagger_response_tages.get(api).update(
                    {"inParameter": tmp_swagger_response_tages.get(api).get(method).pop("parameters")})
            except KeyError:
                tmp_swagger_response.get(api).update(
                    {"inParameter": None})
                tmp_swagger_response_tages.get(api).update(
                    {"inParameter": None})
            try:
                tmp_swagger_response.get(api).update(
                    {"outParameter": tmp_swagger_response.get(api).get(method).pop("responses")})
                tmp_swagger_response_tages.get(api).update(
                    {"outParameter": tmp_swagger_response_tages.get(api).get(method).pop("responses")})
            except KeyError:
                tmp_swagger_response.get(api).update(
                    {"outParameter": None})
                tmp_swagger_response_tages.get(api).update(
                    {"outParameter": None})

            tmp_swagger_response.get(api).__delitem__(method)
            tmp_swagger_response_tages.get(api).__delitem__(method_tags)

            # if method.lower() == "get":
            #     tmp_swagger_response.get(api).__delitem__(method)

        return tmp_swagger_response, tmp_swagger_response_tages
