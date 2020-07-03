#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.WorkRecord import WorkRecordSql
from testcase.flowerChaser.sql.LogComment import LogCommentSql
import random
from faker import Faker
import time


class CommentMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    comment = BeeAction()
    comment_db = WorkRecordSql()
    lcs = LogCommentSql()
    log = logger('ContainerMain').logger
    log.info("开始执行日志评论管理接口测试用例")
    fake = Faker(locale="zh_CN")
    comment.set_user('26632629@qq.com', '123456')

    def test_mobile_comment_add_success(self):
        """
        POST /mobile/comment/add
        添加日志评论成功
        :return:
        """
        logs = self.comment_db.get_all_work_log()
        if logs[0]["id"] is not None:
            log_id = random.choice(logs)["id"]
            content = self.fake.text(max_nb_chars=200)
            response = self.comment._mobile_comment_add(logId_=log_id, content_=content)
            if response["status"] == "OK":
                content_db = self.lcs.query_comment_by_log_id(log_id)[0]["content"]
                self.assertEqual(content_db, response["content"]["content"])
            else:
                self.assertTrue(False, "添加日志评论失败")
        else:
            self.assertTrue(False, "暂无日志")

    def test_mobile_comment_add_without_log_id(self):
        """
        POST /mobile/comment/add
        未输入日志ID, 添加日志评论
        :return:
        """
        content = self.fake.text(max_nb_chars=200)
        response = self.comment._mobile_comment_add(logId_=None, content_=content)
        if response["status"] == "ERROR":
            self.assertEqual("日志id不能为空", response['errorMsg'])
        else:
            self.assertTrue(False, "未传日志ID, 添加评论成功")

    def test_mobile_comment_add_with_wrong_log_id(self):
        """
        POST /mobile/comment/add
        输入不存在的日志ID, 添加日志评论
        :return:
        """
        content = self.fake.text(max_nb_chars=200)
        response = self.comment._mobile_comment_add(logId_=0, content_=content)
        if response["status"] == "ERROR":
            self.assertEqual("日志不存在", response['errorMsg'])
        else:
            self.assertTrue(False, "输入不存在的日志ID, 添加评论成功")

    def test_mobile_comment_add_without_content(self):
        """
        POST /mobile/comment/add
        未输入评论内容, 添加日志评论
        :return:
        """
        response = self.comment._mobile_comment_add(logId_=1)
        if response["status"] == "ERROR":
            self.assertEqual("评论内容不能为空", response['errorMsg'])
        else:
            self.assertTrue(False, "未输入评论内容, 添加评论成功")

    def test_mobile_comment_add_with_long_content(self):
        """
        POST /mobile/comment/add
        评论内容超过200字, 添加日志评论
        :return:
        """
        content = self.fake.text(max_nb_chars=251)
        response = self.comment._mobile_comment_add(logId_=1, content_=content)
        if response["status"] == "ERROR":
            self.assertEqual("评论不能超过200字", response['errorMsg'])
        else:
            self.assertTrue(False, "评论内容超过200字, 添加评论成功")

    def test_mobile_comment_del_success(self):
        """
        POST /mobile/comment/del
        删除日志评论成功
        :return:
        """
        comments = self.comment_db.get_all_comment_by_email("26632629@qq.com")
        if comments[0]["id"] is not None:
            comment_id = random.choice(comments)["id"]
            response = self.comment._mobile_comment_del(id_=comment_id)
            if response["status"] == "OK":
                comment = self.lcs.query_comment_by_comment_id(comment_id, 1)[0]
                self.assertEqual(1, comment['is_delete'])
            else:
                self.assertTrue(False, "删除日志评论成功")
        else:
            self.assertTrue(False, "暂无日志评论")

    def test_mobile_comment_del_not_belong_to_yourself(self):
        """
        POST /mobile/comment/del
        尝试删除别人的评论
        :return:
        """
        response = self.comment._mobile_comment_del(id_=9)
        if response["status"] == "ERROR":
            self.assertEqual("只能删除自己的评论", response['errorMsg'])
        else:
            self.assertTrue(False, "删除别人的日志评论成功")

    def test_mobile_comment_del_without_id(self):
        """
        POST /mobile/comment/del
        评论ID为空, 删除日志评论
        :return:
        """
        response = self.comment._mobile_comment_del(id_=None)
        if response["status"] == "ERROR":
            self.assertEqual("评论ID不能为空", response['errorMsg'])
        else:
            self.assertTrue(False, "评论ID为空, 删除日志评论成功")

    def test_mobile_comment_del_with_wrong_id(self):
        """
        POST /mobile/comment/del
        评论ID不存在, 删除日志评论
        :return:
        """
        response = self.comment._mobile_comment_del(id_=0)
        if response["status"] == "ERROR":
            self.assertEqual("评论不存在", response['errorMsg'])
        else:
            self.assertTrue(False, "评论ID不存在, 删除日志评论成功")

    def test_mobile_comment_list_success(self):
        """
        POST /mobile/comment/list
        根据日志ID获取评论列表
        :return:
        """
        logs = self.comment_db.get_all_work_log()
        if logs[0]["id"] is not None:
            log_id = random.choice(logs)["id"]
            response = self.comment._mobile_comment_list(id_=log_id)
            if response["status"] == "OK":
                comment_db = list(self.lcs.query_comment_by_log_id(log_id))
                comment_res = response['content']
                for c in comment_db:
                    for d in comment_res:
                        if c['id'] == d['id']:
                            self.assertEqual(c['log_id'], d['logId'])
                            if d['creatorId'] == c['creator_id']:
                                self.assertEqual("我", d['creatorName'])
                                self.assertEqual(c['head_img'], d['headImg'])
                                self.assertEqual(c['content'], d['content'])
                                create_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                                            time.localtime(float(d['createTime']) / 1000.0))
                                self.assertEqual(c['create_time'], create_time)
                            else:
                                self.assertEqual(c['creator_name'], d['creatorName'])
                                self.assertEqual(c['head_img'], d['headImg'])
                                self.assertEqual(c['content'], d['content'])
                                create_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                                            time.localtime(float(d['createTime'])/1000.0))
                                self.assertEqual(c['create_time'], create_time)
            else:
                self.assertTrue(False, "根据日志ID获取评论失败")
        else:
            self.assertTrue(False, "暂无日志")

    def test_mobile_comment_list_without_id(self):
        """
        POST /mobile/comment/list
        日志ID为空, 获取评论列表
        :return:
        """
        response = self.comment._mobile_comment_list(id_=None)
        if response["status"] == "ERROR":
            self.assertEqual("日志ID不能为空", response['errorMsg'])
        else:
            self.assertTrue(False, "日志ID为空, 查询评论成功")

    def test_mobile_comment_list_with_wrong_id(self):
        """
        POST /mobile/comment/list
        日志ID不存在, 尝试获取评论列表
        :return:
        """
        response = self.comment._mobile_comment_list(id_=0)
        if response["status"] == "ERROR":
            self.assertEqual("日志不存在", response['errorMsg'])
        else:
            self.assertTrue(False, "日志ID不存在, 查询评论成功")

