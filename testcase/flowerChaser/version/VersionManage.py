#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/1/16 11:30
@Author: hengxin
"""


import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from actions.PassportAction import userAction
from utils.log.logger import logger
from sql.Version import VersionInfoSql
from utils.fake.FakeLocation import FakeLocation
from faker import Faker


class VersionManageMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ua = userAction()
    ba = BeeAction()
    email = '26632629@qq.com'
    ba.set_user(email, 123456)
    log = logger('VersionManageMain').logger
    log.info("版本管理接口测试用例")
    vis = VersionInfoSql()
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()

    def test_add_update_version(self):
        """
        添加待升级版本
        :return:
        """
        # appId: 01 android、02 ios
        # updateType: 0 选择更新，1 强制更新
        # downloadUrl: 通过/mobile/app-version/upload-app上传成功返回的url
        # versionNum: 用户可见应用版本号, 如v1.0.0
        # versionCode: 通过aapt d badging <apkfile>返回的versionCode, 必须大于线上用户已安装的versionCode
        # updateTitle: 呈现给用户的更新弹窗标题
        # updateMessage: 呈现给用户的更新弹窗内容,注意换行需要使用换行符\n
        # status: 1 最新版本，0 之前老版本
        app_id = '01'
        update_type = '0'
        version_num = 'v1.0.0'
        status = 1
        version_code = 4
        update_title = '更新标题'
        update_message = '1.第一行更新内容\n2.第二行更新内容'
        download_url = 'https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-koala/app/version/' \
                       'app_develop_debug_1.0.0_build%2815%29.apk'
        json_response = self.ba._mobile_app_version_add(appId_=app_id, updateType_=update_type, versionNum_=version_num,
                                                        status_=status, versionCode_=version_code,
                                                        updateTitle_=update_title, updateMessage_=update_message,
                                                        downloadUrl_=download_url)
        if json_response["status"] == "OK":
            version_from_db = self.vis.query_latest_update_version()
            self.assertEqual(version_from_db["app_id"], json_response)
        else:
            self.assertTrue(False, "我的日志和全部日志标志为空, 查询日志列表成功")
