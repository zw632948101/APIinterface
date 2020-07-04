#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/2/10 09:52
@Author: hengxin
"""


import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from interfaces.flowerChaser.UserAction import UserAction
from utils.log import log
from testcase.flowerChaser.sql.Keeper import KeeperInfoSql
from testcase.flowerChaser.sql.Passport import PassportInfoSql
from faker import Faker
from random import choice


class AdminOperationMain(unittest.TestCase):
    """
    接口文档: http://dev-user.worldfarm.com/swagger-ui.html
    运营后台相关接口
    """
    ua = UserAction()
    ba = BeeAction()
    log.info("开始执行User接口测试用例")
    pis = PassportInfoSql()
    kis = KeeperInfoSql()
    fake = Faker(locale="zh_CN")

    def test00_fc_admin_add_user_without_login(self):
        """
        POST /fc/admin/user/add
        未登录创建账号
        :return:
        """
        json_response = self.ua._fc_admin_user_add()
        if json_response["status"] == "ERROR":
            self.assertEqual("Request parameter missing", json_response["errorMsg"])
        else:
            self.assertTrue(False, "未登录, 创建空账号成功")

    def test_fc_admin_add_user_with_normal_user(self):
        """
        POST /fc/admin/user/add
        普通用户创建账号
        :return:
        """
        self.ua.set_user('26632629@qq.com', '123456')
        json_response = self.ua._fc_admin_user_add(email_='wenliang.wu@worldfarm.com', phone_='13558715792',
                                                   userName_='吴文亮')
        if json_response["status"] == "ERROR":
            self.assertEqual("抱歉,您没有相应的访问权限!", json_response["errorMsg"])
        else:
            self.assertTrue(False, "普通用户创建账号成功")

    def test_fc_admin_add_user_with_registered_email(self):
        """
        POST /fc/admin/user/add
        邮箱重复, 创建账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_='26632629@qq.com', phone_='19902832572',
                                                   userName_='QA测试鑫')
        if json_response["status"] == "ERROR":
            self.assertEqual("当前邮箱已注册，请重新输入", json_response["errorMsg"])
        else:
            self.assertTrue(False, "邮箱重复, 创建账号成功")

    def test_fc_admin_add_user_with_wrong_email(self):
        """
        POST /fc/admin/user/add
        邮箱格式错误, 创建账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_='qq.com', phone_='19902832572',
                                                   userName_='QA测试鑫')
        if json_response["status"] == "ERROR":
            self.assertEqual("邮箱格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "邮箱格式错误, 创建账号成功")

    def test_fc_admin_add_user_with_long_email(self):
        """
        POST /fc/admin/user/add
        邮箱超过64位, 创建邮箱
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
                                                          '@worldfarm.com',
                                                   phone_='19983286362', userName_='QA测试鑫')
        if json_response["status"] == "ERROR":
            self.assertEqual("邮箱长度不能超过64位", json_response["errorMsg"])
        else:
            self.assertTrue(False, "邮箱超过64位, 创建账号成功")

    def test_fc_admin_add_user_with_wrong_phone(self):
        """
        POST /fc/admin/user/add
        手机号格式不正确, 创建邮箱
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_='abcdefg@worldfarm.com',
                                                   phone_='11002832572', userName_='QA测试鑫')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号格式不正确, 创建账号成功")

    def test_fc_admin_add_user_with_short_phone(self):
        """
        POST /fc/admin/user/add
        手机号小于11位, 创建邮箱
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_=None,
                                                   phone_='18919028649', userName_=self.fake.name())
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号小于11位, 创建账号成功")

    def test_fc_admin_add_user_with_long_phone(self):
        """
        POST /fc/admin/user/add
        手机号小于11位, 创建邮箱
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_='abcdefg@worldfarm.com',
                                                   phone_='186028325722', userName_='QA测试鑫')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号小于11位, 创建账号成功")

    def test_fc_admin_add_user_with_registered_phone(self):
        """
        POST /fc/admin/user/add
        手机号重复, 创建账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_='18602832572@qq.com', phone_='18602832572',
                                                   userName_='QA测试鑫')
        if json_response["status"] == "ERROR":
            self.assertEqual("该手机号已注册", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号重复, 创建账号成功")

    def test_fc_admin_add_user_without_name(self):
        """
        POST /fc/admin/user/add
        姓名为空, 创建账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_='26632629@qq.com', phone_='18602832572',
                                                   userName_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名为空, 创建账号成功")

    def test_fc_admin_add_user_with_long_name(self):
        """
        POST /fc/admin/user/add
        姓名超过20字, 创建账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', '123456', 'employee')
        json_response = self.ua._fc_admin_user_add(email_='26632629@qq.com', phone_='18602832572',
                                                   userName_='姓名不能超过20字姓名不能超过20字姓名不能超过20字')
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能超过20个字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名超过20字, 创建账号成功")

    def test01_fc_admin_edit_user_without_login(self):
        """
        POST /fc/admin/user/edit
        未登录编辑账号
        :return:
        """
        json_response = self.ua._fc_admin_user_edit(email_='26632629@qq.com', phone_='18602832572',
                                                    userName_='用户名')
        if json_response["status"] == "ERROR":
            self.assertEqual("Request parameter missing", json_response["errorMsg"])
        else:
            self.assertTrue(False, "未登录编辑账号成功")

    def test_fc_admin_edit_user_with_normal_user(self):
        """
        POST /fc/admin/user/edit
        普通用户登录, 编辑账号
        :return:
        """
        self.ua.set_user('26632629@qq.com', 123456)
        json_response = self.ua._fc_admin_user_edit(email_='26632629@qq.com', phone_='18602832572',
                                                    userName_='用户名', userId_=407)
        if json_response["status"] == "ERROR":
            self.assertEqual("抱歉,您没有相应的访问权限!", json_response["errorMsg"])
        else:
            self.assertTrue(False, "普通用户登录, 编辑账号")

    def test_fc_admin_edit_user_without_user_id(self):
        """
        POST /fc/admin/user/edit
        用户ID为空, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='26632629@qq.com', phone_='18602832572',
                                                    userName_='用户名', userId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("用户ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "用户ID为空, 编辑账号成功")

    def test_fc_admin_edit_user_with_wrong_user_id(self):
        """
        POST /fc/admin/user/edit
        用户ID不存在, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='1860283257226632629@qq.com', phone_='19908328636',
                                                    userName_='用户名', userId_=0)
        if json_response["status"] == "ERROR":
            self.assertEqual("账号不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "用户ID不存在, 编辑账号成功")

    def test_fc_admin_edit_user_without_user_name(self):
        """
        POST /fc/admin/user/edit
        用户名为空, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='26632629@qq.com', phone_='18602832572',
                                                    userName_='', userId_=407)
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "用户名为空, 编辑账号成功")

    def test_fc_admin_edit_user_with_long_user_name(self):
        """
        POST /fc/admin/user/edit
        用户名超过20个字, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='26632629@qq.com', phone_='18602832572',
                                                    userName_='26632629@qq.com26632629@qq.com', userId_=407)
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能超过20个字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "用户名超过20个字, 编辑账号成功")

    def test_fc_admin_edit_user_with_wrong_email(self):
        """
        POST /fc/admin/user/edit
        邮箱格式不正确, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='qq.com', phone_='18602832572',
                                                    userName_='用户名', userId_=407)
        if json_response["status"] == "ERROR":
            self.assertEqual("邮箱格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "邮箱格式不正确, 编辑账号成功")

    def test_fc_admin_edit_user_with_long_email(self):
        """
        POST /fc/admin/user/edit
        邮箱超过64位, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='2663262926632629266326292663262926632629266326292663262921'
                                                           '@qq.com',
                                                    phone_='18602832572', userName_='用户名', userId_=407)
        if json_response["status"] == "ERROR":
            self.assertEqual("邮箱长度不能超过64位", json_response["errorMsg"])
        else:
            self.assertTrue(False, "邮箱超过64位, 编辑账号成功")

    def test_fc_admin_edit_user_with_wrong_phone(self):
        """
        POST /fc/admin/user/edit
        手机号格式错误, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='26632629@qq.com',
                                                    phone_='12002832572', userName_='用户名', userId_=407)
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号格式错误, 编辑账号成功")

    def test_fc_admin_edit_user_with_long_phone(self):
        """
        POST /fc/admin/user/edit
        手机号超过11位, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='26632629@qq.com',
                                                    phone_='186028325723', userName_='用户名', userId_=407)
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号超过11位, 编辑账号成功")

    def test_fc_admin_edit_user_with_short_phone(self):
        """
        POST /fc/admin/user/edit
        手机号少于11位, 编辑账号
        :return:
        """
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_='26632629@qq.com',
                                                    phone_='1200283257', userName_='用户名', userId_=407)
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号少于11位, 编辑账号成功")

    def test_fc_admin_edit_user_success(self):
        """
        POST /fc/admin/user/edit
        信息合法编辑成功
        :return:
        """
        old_user = self.pis.query_earliest_user()[0]
        new_mail = self.fake.email()
        new_phone = self.fake.phone_number()
        new_name = self.fake.name()
        self.ua.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ua._fc_admin_user_edit(email_=new_mail, phone_=new_phone,
                                                    userName_=new_name, userId_=old_user["id"])
        if json_response["status"] == "OK":
            new_user = self.pis.query_earliest_user()[0]
            self.assertEqual(new_mail, new_user["email"])
            self.assertEqual(new_phone, new_user["phone"])
            self.assertEqual(new_name, new_user["username"])
            self.ua._fc_admin_user_edit(email_='26632629@qq.com', phone_='18602832572',
                                        userName_='QA测试鑫', userId_=old_user["id"])
        else:
            self.assertTrue(False, "信息合法编辑失败")

    def test02_admin_set_fc_user_role_without_login(self):
        """
        POST /admin/fc-user/set-role
        未登录设置角色
        :return:
        """
        json_response = self.ba._admin_fc_user_set_role(userIds_=[407], roleCode_=1001, postCode_=1000)
        if json_response["status"] == "ERROR":
            self.assertEqual("Request parameter missing", json_response["errorMsg"])
        else:
            self.assertTrue(False, "未登录设置角色成功")

    def test_admin_set_fc_user_role_with_normal_user(self):
        """
        POST /admin/fc-user/set-role
        普通用户, 设置角色
        :return:
        """
        self.ba.set_user('26632629@qq.com', 123456)
        json_response = self.ba._admin_fc_user_set_role(userIds_=[407], roleCode_=1001, postCode_=1000)
        if json_response["status"] == "ERROR":
            self.assertEqual("抱歉,您没有相应的访问权限!", json_response["errorMsg"])
        else:
            self.assertTrue(False, "普通用户, 设置角色成功")

    def test_admin_set_fc_user_role_without_user_id(self):
        """
        POST /admin/fc-user/set-role
        用户ID为空, 设置角色
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_fc_user_set_role(userIds_='', roleCode_=1001, postCode_=1000)
        if json_response["status"] == "ERROR":
            self.assertEqual("用户ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "用户ID为空, 设置角色成功")

    def test_admin_set_fc_user_role_with_wrong_user_id(self):
        """
        POST /admin/fc-user/set-role
        用户ID不存在, 设置角色
        :return:
        """
        user_id = 0
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_fc_user_set_role(userIds_=[user_id], roleCode_=1001, postCode_=1000)
        if json_response["status"] == "ERROR":
            self.assertEqual("用户(%d)不存在" % user_id, json_response["errorMsg"])
        else:
            self.assertTrue(False, "用户ID不存在, 设置角色成功")

    def test_admin_set_fc_user_role_with_wrong_role_code(self):
        """
        POST /admin/fc-user/set-role
        角色编码错误, 设置角色
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_fc_user_set_role(userIds_=[407], roleCode_=0, postCode_=1000)
        if json_response["status"] == "ERROR":
            self.assertEqual("角色不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "角色编码错误, 设置角色成功")

    def test_admin_set_fc_user_role_without_role_code(self):
        """
        POST /admin/fc-user/set-role
        角色编码为空, 设置角色
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_fc_user_set_role(userIds_=[407], roleCode_='', postCode_=1000)
        if json_response["status"] == "ERROR":
            self.assertEqual("角色编码不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "角色编码为空, 设置角色成功")

    def test_admin_set_fc_user_role_with_wrong_post_code(self):
        """
        POST /admin/fc-user/set-role
        岗位编码错误, 设置角色
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_fc_user_set_role(userIds_=[407], roleCode_=1001, postCode_=0)
        if json_response["status"] == "ERROR":
            self.assertEqual("岗位不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "岗位编码错误, 设置角色成功")

    def test_admin_set_fc_user_role_without_post_code(self):
        """
        POST /admin/fc-user/set-role
        岗位编码为空, 设置角色
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_fc_user_set_role(userIds_=[407], roleCode_=1001, postCode_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("岗位编码不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "岗位编码为空, 设置角色成功")

    def test_admin_set_fc_user_role_success(self):
        """
        POST /admin/fc-user/set-role
        信息合法, 设置成功
        :return:
        """
        post_code = {"1000": "管理员", "1001": "蜂农", "1002": "项目专员", "1003": "驾驶员",
                     "1004": "后勤专员", "1005": "项目经理"}
        role_code = {"1001": "管理员", "1002": "普通员工"}
        random_post = choice(["1001", "1002", "1003", "1004", "1005"])
        random_role = choice(["1002"])
        old_user = self.pis.query_earliest_user()[0]
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_fc_user_set_role(userIds_=[old_user["id"]],
                                                        roleCode_=random_role, postCode_=random_post)
        if json_response["status"] == "OK":
            user = self.pis.query_earliest_user()[0]
            self.assertEqual(old_user["id"], user["id"])
            self.assertEqual(random_role, user["role_code"])
            self.assertEqual(random_post, user["post_code"])
            log.info("ID为%d的用户[%s], 角色设置为[%s], 岗位设置为[%s]"
                          % (user["id"], user["username"], role_code[random_role], post_code[random_post]))
            self.ba._admin_fc_user_set_role(userIds_=[old_user["id"]],
                                            roleCode_=1001, postCode_=1000)
        else:
            self.assertTrue(False, "信息合法, 设置失败")

    def test03_fc_bee_admin_bee_keeper_add_without_login(self):
        """
        POST /fc-bee/admin/bee-keeper/add
        未登录, 添加养蜂师傅
        :return:
        """
        json_response = self.ba._admin_bee_keeper_add()
        if json_response["status"] == "ERROR":
            self.assertEqual("Request parameter missing", json_response["errorMsg"])
        else:
            self.assertTrue(False, "未登录, 添加养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_add_with_normal_user(self):
        """
        POST /fc-bee/admin/bee-keeper/add
        普通用户, 添加养蜂师傅
        :return:
        """
        self.ba.set_user('26632629@qq.com', 123456)
        json_response = self.ba._admin_bee_keeper_add(name_="普通用户添加")
        if json_response["status"] == "ERROR":
            self.assertEqual("抱歉,您没有相应的访问权限!", json_response["errorMsg"])
        else:
            self.assertTrue(False, "未登录, 添加养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_add_without_name(self):
        """
        POST /fc-bee/admin/bee-keeper/add
        姓名为空, 添加养蜂师傅
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_add(name_="")
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名为空, 添加养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_add_with_long_name(self):
        """
        POST /fc-bee/admin/bee-keeper/add
        姓名超过20字, 添加养蜂师傅
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_add(name_="我是养蜂师傅我是养蜂师傅我是养蜂师傅我是养蜂师傅")
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能超过20字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名超过20字, 添加养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_add_repeated_name(self):
        """
        POST /fc-bee/admin/bee-keeper/add
        名字重复, 添加养蜂师傅
        :return:
        """
        keeper = self.kis.query_latest_keeper()[0]
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_add(name_=keeper["name"])
        if json_response["status"] == "ERROR":
            self.assertEqual("养蜂师傅姓名重复", json_response["errorMsg"])
        else:
            self.assertTrue(False, "名字重复, 添加养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_add_success(self):
        """
        POST /fc-bee/admin/bee-keeper/add
        名字合法, 添加养蜂师傅
        :return:
        """
        keeper_name = self.fake.name()
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_add(name_=keeper_name)
        if json_response["status"] == "OK":
            keeper = self.kis.query_keeper_by_name(keeper_name)[0]
            self.assertEqual(keeper_name, keeper["name"])
        else:
            self.assertTrue(False, "名字合法, 添加养蜂师傅成功")

    def test04_fc_bee_admin_bee_keeper_edit_without_login(self):
        """
        POST /fc-bee/admin/bee-keeper/edit
        未登录, 编辑养蜂师傅
        :return:
        """
        json_response = self.ba._admin_bee_keeper_edit(id_=4, name_="张三")
        if json_response["status"] == "ERROR":
            self.assertEqual("Request parameter missing", json_response["errorMsg"])
        else:
            self.assertTrue(False, "未登录, 编辑养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_edit_with_normal_user(self):
        """
        POST /fc-bee/admin/bee-keeper/edit
        普通用户, 编辑养蜂师傅
        :return:
        """
        self.ba.set_user('26632629@qq.com', 123456)
        json_response = self.ba._admin_bee_keeper_edit(id_=4, name_="张三")
        if json_response["status"] == "ERROR":
            self.assertEqual("抱歉,您没有相应的访问权限!", json_response["errorMsg"])
        else:
            self.assertTrue(False, "普通用户, 编辑养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_edit_without_id(self):
        """
        POST /fc-bee/admin/bee-keeper/edit
        师傅ID为空, 编辑养蜂师傅
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_edit(id_="", name_="张三")
        if json_response["status"] == "ERROR":
            self.assertEqual("师傅ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "师傅ID为空, 编辑养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_edit_with_wrong_id(self):
        """
        POST /fc-bee/admin/bee-keeper/edit
        养蜂师傅不存在, 编辑养蜂师傅
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_edit(id_=0, name_="张三")
        if json_response["status"] == "ERROR":
            self.assertEqual("养蜂师傅不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂师傅不存在, 编辑养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_edit_without_name(self):
        """
        POST /fc-bee/admin/bee-keeper/edit
        姓名为空, 编辑养蜂师傅
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_edit(id_=1, name_="")
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名为空, 编辑养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_edit_with_long_name(self):
        """
        POST /fc-bee/admin/bee-keeper/edit
        姓名超过20字, 编辑养蜂师傅
        :return:
        """
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_edit(id_=1, name_="我是养蜂师傅我是养蜂师傅我是养蜂师傅我是养蜂师傅")
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能超过20字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名超过20字, 编辑养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_edit_repeated_name(self):
        """
        POST /fc-bee/admin/bee-keeper/edit
        名字重复, 添加养蜂师傅
        :return:
        """
        keeper = self.kis.query_latest_keeper()[0]
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        keeper_id = keeper["id"] - 1
        json_response = self.ba._admin_bee_keeper_edit(id_=keeper_id, name_=keeper["name"])
        if json_response["status"] == "ERROR":
            self.assertEqual("养蜂师傅姓名重复", json_response["errorMsg"])
        else:
            self.assertTrue(False, "名字重复, 添加养蜂师傅成功")

    def test_fc_bee_admin_bee_keeper_edit_success(self):
        """
        POST /fc-bee/admin/bee-keeper/edit
        姓名合法, 编辑养蜂师傅
        :return:
        """
        new_keeper_name = self.fake.name()
        old_keeper = self.kis.query_latest_keeper()[0]
        self.ba.set_user('admin@worldfarm.com', 123456, 'employee')
        json_response = self.ba._admin_bee_keeper_edit(id_=old_keeper["id"], name_=new_keeper_name)
        if json_response["status"] == "OK":
            log.info("ID为%s的养蜂师傅:%s 更名为:%s" % (old_keeper["id"], old_keeper["name"], new_keeper_name))
            new_keeper = self.kis.query_latest_keeper()[0]
            self.assertEqual(new_keeper_name, new_keeper["name"])
        else:
            self.assertTrue(False, "姓名合法, 编辑养蜂师傅成功")
