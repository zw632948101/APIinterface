#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import yaml
from utils.log import log
from os.path import abspath, dirname


def get_config():
    with open(dirname(abspath('.'))+"/environmentConfiguration/config.yaml", encoding='utf-8') as f:
        config = yaml.safe_load(f)
        if config.get('which_project') in config.keys():
            return config.get(config.get('which_project'))
        else:
            log.error('未选择项目配置!')
            exit(0)


# def set_config_project(which_project=None):
#     file_path = dirname(abspath('.'))+"/environmentConfiguration/config.yaml"
#     with open(file_path, encoding='utf-8') as f:
#         config = yaml.safe_load(f)
#         config.update({'which_project': which_project})
#     with open(file_path, encoding='utf-8', mode='w') as f:
#         yaml.safe_dump(config, f)
