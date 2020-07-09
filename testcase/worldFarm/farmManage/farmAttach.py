#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/1/3 11:12
__author__: wei.zhang

"""
import json
from random import choice
from testcase.worldFarm import testCase, FarmManage


class AttachMain(testCase):
    fq = FarmManage()

    def test_mobile_farm_attach_qualification_upload(self):
        """
        手机上传资质文件
        :return:
        """
        now_time = self.tt.get_standardtime_by_offset(formats='%Y%m%d%H%M%S')
        file = './../tempAttach/test.pdf'
        register = self.ka.mobile_farm_attach_qualification_upload(file=file, fileId=str(now_time))
        self.assertEqual(register.get('status'), 'OK')

    def test_mobile_farm_attach_add_qualification(self):
        """
        手机保存资质文件信息
        :return:
        """
        now_time = self.tt.get_standardtime_by_offset(formats='%Y%m%d%H%M%S')
        file = './../tempAttach/test.pdf'
        register = self.ka.mobile_farm_attach_qualification_upload(file=file, fileId=str(now_time))
        file_url = register['content']
        attachment = [{"bizType": 2, "sortNo": 1, "fileName": "世界观（原书第2版）.pdf", "fileType": "pdf", "fileSize": "10",
                       "fileUrl": str(file_url)}]
        attachment = json.dumps(attachment)
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_farm_attach_add_qualification(farmId=farm_id, attachment="%s" % attachment)
        self.assertEqual(register.get('status'), 'OK')

    def test_mobile_farm_attach_one_qualification_list(self):
        """
        单一类型资质文件列表 v1.2.4
        :return:
        """
        pn = 1
        ps = 100
        farm_id = 705
        biz_type = 2
        info = self.ka.mobile_farm_attach_one_qualification_list(pn, ps, farm_id, biz_type)
        self.assertEqual(info["status"], "OK")
        sql_farm_attach = self.fq.query_farm_attach_buy_email(self.email)
        attach_id = sql_farm_attach[0]['id']
        register = self.ka.mobile_farm_attach_del_qualification(attachId=attach_id)

    def test_mobile_farm_attach_qualification_upload_process(self):
        """
        手机上传资质文件进度百分比 V 1.2.4
        :return:
        """
        sql_farm_attach = self.fq.query_farm_attach_buy_email(self.email)
        attach_id = sql_farm_attach[0]['id']
        register = self.ka.mobile_farm_attach_del_qualification(attachId=attach_id)

    def test_mobile_farm_attach_qualification_type_count(self):
        """
        资产文件分类统计列表 V 1.2.4
        :return:
        """
        sql_farm_attach = self.fq.query_farm_attach_buy_email(self.email)
        farm_id = sql_farm_attach[0]['farm_id']
        register = self.ka.mobile_farm_attach_qualification_type_count(farmId=farm_id)

    def test_mobile_farm_attach_qualification_upload_send_email(self):
        """
        邮件上传发邮件 V 1.2.4
        :return:
        """
        sql_farm_attach = self.fq.query_farm_attach_buy_email(self.email)
        farm_id = sql_farm_attach[0]['farm_id']
        self.ka.mobile_farm_attach_qualification_upload_send_email(farmId=farm_id, bizType=2,
                                                                   email="632948101@qq.com")

    def test_mobile_farm_attach_get_qualification_auth(self):
        """
        批量获取附件授权 V 1.2.4
        :return:
        """
        now_time = self.tt.get_standardtime_by_offset(formats='%Y%m%d%H%M%S')
        file = './../tempAttach/澳洲调研小结-交易部分.pdf'
        register = self.ka.mobile_farm_attach_qualification_upload(file=file, fileId=str(now_time))
        file_url = register['content']
        get_qualification_auth = self.ka.mobile_farm_attach_get_qualification_auth(urls=file_url)
        auth_url_list = get_qualification_auth['content']
        auth_url = "".join(auth_url_list)
        attachment = [
            {"bizType": 7, "sortNo": 1, "fileName": "世界观（原书第2版）.pdf", "fileType": "pdf", "fileSize": "10",
             "fileUrl": str(auth_url)}]
        attachment = json.dumps(attachment)
        sql_farm_id = self.fq.query_farm_attach_buy_email(self.email)
        farm_id = sql_farm_id[0]['farm_id']
        register = self.ka.mobile_farm_attach_add_qualification(farmId=farm_id, attachment="%s" % attachment)

    def test_mobile_farm_attach_album_add(self):
        """
        移动端-农场附件-添加相册 V 1.2.4
        :return:
        """
        file_url = './../tempAttach/screen.png',
        farmId = self.fq.query_default_farm(self.email)[0].get('farm_id')
        register = self.ka.mobile_farm_attach_album_add(lable_id=None, lable_name=None, farmId=farmId, fileName=None,
                                                        fileType=None, fileSize=None,
                                                        fileUrl=file_url,
                                                        isCover=1)

        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_attach_album_del(self):
        """
        移动端-农场附件-删除图片
        :return:
        """
        register = self.ka.mobile_farm_attach_album_del(attachId=38)

        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_attach_album_upload(self):
        """
        移动端-农场附件-图片上传
        :return:
        """
        file = './../tempAttach/Screen.png'
        register = self.ka.mobile_farm_attach_album_upload(file=file)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_attach_cover_set(self):
        """
        移动端-农场-设置封面
        :return:
        """
        attachid = choice(self.fq.query_default_farm_attach(self.email)).get('id')
        register = self.ka.mobile_farm_attach_cover_set(attachId=attachid)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_attach_list(self):
        """
        移动端-农场-相册列表
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_farm_attach_list(pn=None, ps=None, farmId=farm_id)
        self.assertEqual(register['status'], 'OK')


if __name__ == '__main__':
    a = AttachMain()
