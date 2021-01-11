# encoding: utf-8

"""
__author__ = Zhang Pengfei
__date__ = 2018/10/18
"""
import codecs
import datetime
import json
import os
import time
import re
from utils.dataRequest.dataRequester import Request
from utils.checkApiChanges.checher.compareTheData import CompareTheData
from utils.environmentConfiguration import config
from utils.log import log


class UpdateAction(object):
    def __init__(self):
        super(UpdateAction, self).__init__()
        self.env = config.get('updateActionAPI')
        self.hosts = config.get('hosts').get(self.env)
        self.interfaces_path = '../../interfaces/%s/' % config.get('projectName')
        self.template_path = './template/'

    def get_edit_api(self):
        """
        检查接口变动，记录变动接口
        :return:
        """
        CompareTheData(self.env).statistics_api()

    def get_api_paths(self, host_name):
        """
        获取接口，并解析swagger接口
        :param host_name:
        :return:
        """
        json_content = Request().get(str(host_name) + '/v2/api-docs')
        paths = json.loads(json_content)["paths"]
        path_detail_list = []
        for p in paths:
            paras = []
            para_desc_list = []
            for request_method in paths[p]:
                desc = paths[p][request_method].get("tags", [])[0]
                summary = paths[p][request_method].get("summary", [])
                desc = desc + ' ' + summary
                para_desc_list.append(desc)
                paras = paths[p][request_method].get("parameters", [])
                if paras != [] and paras[0]['in'] == 'body' and paras[0]['schema'].get('$ref'):
                    # 判断传参类型是否为body并且以json展示
                    schema = paras[0]['schema']['$ref']
                    schema = schema.split('/')[-1]
                    properties = json.loads(json_content)['definitions'][schema]['properties']
                    paras = [{'name': pr} for pr in properties]
                para_desc_list.append(request_method)
            p_dict = {}
            if paras is None:
                pass
            else:
                for para in paras:
                    if not re.findall(r'\[\d{0,1}\]', para.get('name')):  # 判断参数是否为子参数
                        p_dict[para['name']] = u"%s_%s_%s" % (para.get('type', 'noType'),
                                                              para.get('required', 'noRequired'),
                                                              para.get('description',
                                                                       'noDescription'))
            para_desc_list.append(p_dict)
            path_detail_list.append({p: para_desc_list})
        return path_detail_list

    def get_api_statistics(self, file_name, host_name):
        """
        获取接口数据，生成TXT文件

        :param file_name:
        :param host_name:
        :return:
        """
        path_detail_list = self.get_api_paths(host_name)
        # demand_list = sorted(path_detail_list)
        now = time.strftime("_%Y-%m-%d_%H%M%S", time.localtime())
        # L.logger.debug(path_detail_list)
        if not os.path.exists(self.template_path + "docs"):
            os.makedirs(self.template_path + "docs")
        with codecs.open(self.template_path + 'docs/' + str(file_name) + now + '.txt', 'a',
                         'utf-8') as f:
            # with codecs.open('./PATH_ONLY_' + str(file_name) + now + '.txt', 'a', 'utf-8') as f:
            for item in path_detail_list:
                for k, v in item.items():
                    if isinstance(v[2], dict):
                        f.write('%s%s, %s\n' % (host_name, k, v[0]))

    def get_paths_yaml(self, file_name, host_name):
        """
        获取接口数据，生成yaml文件
        :param file_name:
        :param host_name:
        :return:
        """

        path_detail_list = self.get_api_paths(host_name)
        now = time.strftime("_%Y-%m-%d_%H%M%S", time.localtime())
        # current_path = os.path.dirname(os.path.abspath(__file__))
        if not os.path.exists(self.template_path + "tmpDocs"):
            os.makedirs(self.template_path + "tmpDocs")
        with codecs.open(self.template_path + "tmpDocs/" + str(file_name) + now + '.yaml', 'a',
                         'utf-8') as f:
            f.write(host_name + ':\n')
            for item in path_detail_list:
                for k, v in item.items():
                    if isinstance(v[2], dict):
                        f.write('  %s:\n' % k)
                        for x, y in v[2].items():
                            f.write('    %s:\n' % x)

    def constitute_request_method(self, request_method, param_data, lower_action, fun_name, api,
                                  fun_data, param_datas):
        """
        组合接口调用方法
        :param request_method: 请求方式，根据请求方式不同读取不同的模板文件
        :param param_data: 接口参数
        :param lower_action: 服务名称
        :param fun_name: 解析接口生成的方法名称
        :param api: 接口
        :param fun_data: 传参
        :return:
        """
        if request_method == 'post':
            fun_template = open(self.template_path + 'fun_post_template.txt', 'r').read()
        elif request_method == 'get':
            fun_template = open(self.template_path + 'fun_get_template.txt', 'r').read()

        param_rep = {'func_param': param_data, 'lower_action': lower_action, 'fun_name': fun_name,
                     'key': api,
                     'functions': fun_data, 'fun_params': param_datas}
        param_rep = dict((re.escape(k), v) for k, v in param_rep.items())
        pattern = re.compile("|".join(param_rep.keys()))
        fun_str = pattern.sub(lambda m: param_rep[re.escape(m.group(0))], fun_template)
        return fun_str

    def __constitute_upload(self, param_data, lower_action, fun_name, api, fun_data):
        fun_template = open(self.template_path + 'fun_upload_template.txt', 'r').read()
        param_rep = {'param': param_data, 'lower_action': lower_action, 'fun_name': fun_name,
                     'key': api,
                     'functions': fun_data}
        param_rep = dict((re.escape(k), v) for k, v in param_rep.items())
        pattern = re.compile("|".join(param_rep.keys()))
        fun_str = pattern.sub(lambda m: param_rep[re.escape(m.group(0))], fun_template)
        return fun_str

    def create_action(self, url_host: str, host_name: str):
        """
        解析参数牲畜对应action文件
        :param url_host:
        :param host_name:
        :return:
        """
        urldict = config.get('urldict')
        # 生成类和构造方法
        account_type = config.get('accounttype')
        action_name = urldict.get(url_host)
        lower_action = action_name.lower()
        url_host = url_host
        # 读取模板文件，替换相应的字段
        action_template = open(self.template_path + 'action_template.txt', 'r',
                               encoding='utf-8').read()
        rep = {'lower_action': lower_action, 'action_name': action_name, 'url_host': url_host,
               'accounttype': account_type}
        rep = dict((re.escape(k), v) for k, v in rep.items())
        pattern = re.compile("|".join(rep.keys()))
        action_template = pattern.sub(lambda m: rep[re.escape(m.group(0))], action_template)
        # 创建action文件
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        import os
        # todo
        action_file_name = self.interfaces_path + action_name.capitalize() + "Action_%s.py" % now
        # 读取方法模板文件
        fun_template = open(self.template_path + 'fun_post_template.txt', 'r').read()
        with open(action_file_name, "w", encoding='utf-8') as f:
            f.writelines(action_template)
            # 解析数据源组成方法参数
            path_detail_list = self.get_api_paths(host_name)
            for api_data in path_detail_list:
                for api, value in api_data.items():
                    f.write('\n')
                    # 获取接口替换特殊符号，生成方法名
                    fun_str = "[\/\-\【\】 \{\}]"
                    fun_name = re.sub(fun_str, '_', api[1:]).replace(".", "")
                    fun_data = param_data = param_datas = ''

                    if isinstance(value[2], dict):
                        paramlist = list(value[2].keys())
                        for param in paramlist:
                            param = re.sub('[\.\-]', '_', param)
                            if account_type == 'wf_account':
                                param_data += ", '%s': %s" % (param, param)
                                param_datas += "'%s': %s, " % (param, param)
                                fun_data += ", " + param + '=None'
                            else:
                                param_data += ", '%s': %s" % (param, param + '_')
                                param_datas += "'%s': %s, " % (param, param + '_')
                                fun_data += ", " + param + '_=None'
                    fun_str = self.constitute_request_method(request_method=value[1],
                                                             param_data=param_data,
                                                             lower_action=lower_action,
                                                             fun_name=fun_name,
                                                             param_datas=param_datas,
                                                             fun_data=fun_data, api=api)
                    f.writelines(fun_str)

    def add_path_only_txt(self):
        for key, host in self.hosts.items():
            log.info(key)
            try:
                self.get_api_statistics(key, host)
            except Exception as e:
                log.error(e)

    def add_latest_yaml(self):
        for key, host in self.hosts.items():
            log.info(key)
            try:
                self.get_paths_yaml(key, host)
            except Exception as e:
                log.error(e)

    def add_latest_action(self):
        for key, host in self.hosts.items():
            log.info(key)
            self.create_action(key, host)
            # try:
            #     self.create_action(key, host)
            # except Exception as e:
            #     log.error(e)


if __name__ == '__main__':
    update_action = UpdateAction()
    update_action.add_latest_action()
    # update_action.add_latest_yaml()
    # update_action.add_path_only_txt()
    # update_action.get_edit_api()
