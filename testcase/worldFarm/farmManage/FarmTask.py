#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Xiujuan Chen'
__date__ = '2019/10/30'
农场任务
"""
import random
from testcase.worldFarm import testCase, ScheduleQuery


class FarmTask(testCase):
    fq = ScheduleQuery()

    def __init__(self, methodName='runTest'):
        super(FarmTask, self).__init__(methodName=methodName)
        self.ka.set_user(mobile=self.email, password=self.password)

    def test_mobile_farm_task_add(self):
        """
        添加农场任务 V 1.2.5
        :return:
        """
        farm_id = random.choice(self.fq.query_default_farm(email=self.email)).get('farm_id')
        start_time = self.tt.get_standardtime_timestamp(hour=5)
        end_time = self.tt.get_standardtime_timestamp(day=1, hour=5)
        task_name = description = "接口测试任务描述%s" % start_time
        userid_list = self.fq.query_farm_all_user_id(farmid=farm_id)
        userids = self.tool.data_assemble('user_id', userid_list, 3)
        self.ka._mobile_farm_task_add(farmId=farm_id, taskName=task_name, startTime=start_time,
                                      endTime=end_time, description=description, userIds=userids)

        task_list = self.fq.query_task_list_buy_farm_id_create_task_info(farm_id=farm_id)
        start_time_sql = self.tt.str_time_timestamp(task_list["start_time"])
        end_time_sql = self.tt.str_time_timestamp(task_list["end_time"])

        self.assertEqual(farm_id, task_list["farm_id"])
        self.assertEqual(task_name, task_list["task_name"])
        self.assertEqual(start_time, start_time_sql)
        self.assertEqual(end_time, end_time_sql)
        self.assertEqual(description, task_list["description"])

    def test_mobile_farm_task_update(self):
        """
        移动端-农场任务-编辑农场任务【v1.2.7 可对字段】
        :return:
        """
        farminfo = random.choice(self.fq.query_default_farm(email=self.email))
        farmid = farminfo.get('farm_id')
        userid = farminfo.get('user_id')
        taskid = random.choice(self.fq.query_task_info_buy_farm_id(farm_id=farmid)).get('id')
        start_time = self.tt.get_standardtime_timestamp(hour=5)
        end_time = self.tt.get_standardtime_timestamp(day=1, hour=5)
        task_name = description = "接口测试任务描述%s" % start_time
        userid_list = self.fq.query_farm_all_user_id(farmid=farmid)
        userids = self.tool.data_assemble('user_id', userid_list, 3)

        self.ka._mobile_farm_task_update(farmId=farmid, taskName=task_name, startTime=start_time,
                                         endTime=end_time, description=description, userIds=userids, id=taskid)

        taskinfo = self.fq.query_task_info_buy_task_id(task_id=taskid)
        taskuserinfo = self.fq.query_farm_task_receiver_info(taskid=taskid)
        userlist = self.tool.data_assemble('id', taskuserinfo)
        self.assertListEqual(userids, userlist)
        self.assertEqual(userid, taskinfo[0]["editor_id"])

        start_time_sql = self.tt.str_time_timestamp(taskinfo[0]["start_time"])
        end_time_sql = self.tt.str_time_timestamp(taskinfo[0]["end_time"])
        self.assertEqual(start_time, start_time_sql)
        self.assertEqual(end_time, end_time_sql)
        #
        self.assertEqual(task_name, taskinfo[0].get('task_name'))
        self.assertEqual(description, taskinfo[0]["description"])

    def test_mobile_farm_task_del(self):
        """
        删除农场任务V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        task_list = self.fq.query_task_info_buy_farm_id(farm_id)
        task_id = task_list[0]["id"]
        self.ka._mobile_farm_task_del(taskId=task_id)
        task_list_update = self.fq.query_task_info_buy_task_id(task_id=task_id)
        self.assertEqual(1, task_list_update[0]["is_delete"])

    def test_mobile_farm_task_list(self):
        """
        农场任务列表V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        register = self.ka._mobile_farm_task_list(pn=None, ps=None, farmId=farm_id, status=None)
        task_list = self.fq.query_task_list_buy_farm_id_sort(farm_id=farm_id)
        content = register.get('content')
        if content:
            for i in range(len(content.get("test_case"))):
                self.assertEqual(content["test_case"][i]["farmId"], task_list[i]["farm_id"])
                self.assertEqual(content["test_case"][i]["taskName"], task_list[i]["task_name"])
                self.assertEqual(content["test_case"][i]["description"], task_list[i]["description"])
                self.assertEqual(content["test_case"][i]["status"], task_list[i]["status"])

                distributeUsers = content["test_case"][i].get('distributeUsers')
                if distributeUsers:
                    taskuserinfo = self.fq.query_farm_task_receiver_info(taskid=content["test_case"][i].get('id'))
                    taskuserinfo = self.tool.del_dict_value_null(taskuserinfo)
                    self.assertListEqual(taskuserinfo, distributeUsers)

                # 断言完成人信息
                completeUser = content.get('completeUser')
                if completeUser:
                    completeuser = self.fq.query_task_info_complete_user(task_id=content["test_case"][i].get('id'))
                    completeuser = self.tool.del_dict_value_null(completeuser)
                    self.assertDictEqual(completeuser, completeUser)
        else:
            self.log.error("当前数据与数据库数据不匹配！")

    def test_mobile_farm_task_home(self):
        """
        农场计划首页V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        self.ka._mobile_farm_task_home(farmId=farm_id)

    def test_mobile_farm_task_update_status(self):
        """
        修改农场任务状态V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        task_list = self.fq.query_task_info_buy_farm_id(farm_id=farm_id)
        if len(task_list) > 0:
            task_id = task_list[0]["id"]
            self.ka._mobile_farm_task_update_status(taskId=task_id)
            task_info = self.fq.query_task_info_buy_task_id(task_id=task_id)
            self.assertEqual(30, task_info[0]["status"])
        else:
            self.log.error("当前农场暂无未完成/已过期任务！")

    def test_mobile_farm_graze_plan_add(self):
        """
        新建农场放牧计划V 1.2.5
        :return:
        """
        region_list = random.choice(self.fq.query_region_list_buy_email(email=self.email))
        farm_id = region_list.get('farm_id')
        region_id = region_list.get('id')
        plan_start_time = self.tt.get_standardtime_timestamp(day=1)
        current_quality = random.randint(2, 50) * 100
        end_quality = current_quality / 200 * 100
        grow_rate = end_quality / 200 * 100
        consume_rate = grow_rate
        expect_date = random.randint(1, 10)
        plan_type = 2 if expect_date <= 5 else 1
        self.ka._mobile_farm_graze_plan_add(farmId=farm_id, regionId=region_id, planType=plan_type,
                                            planStartTime=plan_start_time, currentQuality=current_quality,
                                            endQuality=end_quality, growRate=grow_rate, consumeRate=consume_rate
                                            , expectDate=expect_date)
        plan_list = self.fq.query_graze_plan_buy_region_id(regionid=region_id)
        start_time_sql = self.tt.str_time_timestamp(plan_list[0].get('plan_start_time'))
        self.assertEqual(farm_id, plan_list[0]["farm_id"])
        self.assertEqual(region_id, plan_list[0]["region_id"])
        self.assertEqual(plan_start_time, start_time_sql)
        self.assertEqual(current_quality, plan_list[0]["current_quality"])
        self.assertEqual(end_quality, plan_list[0]["end_quality"])
        self.assertEqual(grow_rate, plan_list[0]["grow_rate"])
        self.assertEqual(consume_rate, plan_list[0]["consume_rate"])
        self.assertEqual(expect_date, plan_list[0]["expect_date"])

    def test_mobile_farm_graze_plan_list(self):
        """
        农场放牧计划-农场放牧计划列表【v1.2.6 可联调】
        :return:
        """
        farmid = random.choice(self.fq.query_default_farm(self.email)).get('farm_id')
        status = random.choice([10, 15, 20])
        register = self.ka._mobile_farm_graze_plan_list(farmId=farmid, status=status)
        self.assertEqual(register['status'], "OK")

    def test_mobile_farm_graze_plan_detail(self):
        """
        农场放牧计划详情V 1.2.5
        :return:
        """
        region_list = random.choice(self.fq.query_default_farm(email=self.email))
        farmid = region_list["farm_id"]
        graze_list = self.fq.query_graze_plan_buy_farm_id(farmid=farmid)
        if graze_list:
            plan_id = graze_list[0]["id"]
            self.ka._mobile_farm_graze_plan_detail(planId=plan_id)
        else:
            self.log.info("当前围栏暂无放牧计划！")

    def test_mobile_farm_graze_plan_del(self):
        """
        删除农场放牧计划V 1.2.5
        :return:
        """
        region_list = random.choice(self.fq.query_default_farm(email=self.email))
        farmid = region_list.get('farm_id')
        graze_list = self.fq.query_graze_plan_buy_farm_id(farmid=farmid)
        if graze_list:
            plan_id = random.choice(graze_list).get('id')
            self.ka._mobile_farm_graze_plan_del(planId=plan_id)
            graze_list_update = self.fq.query_plan_info_buy_plan_id(plan_id=plan_id)
            self.assertEqual(1, graze_list_update[0]["is_delete"])
        else:
            self.log.error("围栏中暂无放牧计划！")

    # def test_mobile_farm_graze_plan_region_info(self):
    #     """
    #     获取围栏信息V 1.2.5
    #     :return:
    #     """
    #     region_list = self.fq.query_region_list_buy_email(email=self.email)
    #     region_id = region_list[0]["id"]
    #     self.koalaAction.mobile_farm_graze_plan_region_info(regionId=region_id)

    def test_mobile_farm_graze_plan_update_status(self):
        """
        修改农场放牧计划状态V 1.2.5
        :return:
        """
        region_id = random.choice(self.fq.query_default_farm(self.email)).get('farm_id')
        plan_id = random.choice(self.fq.query_graze_plan_buy_farm_id(farmid=region_id)).get('id')
        if plan_id:
            self.log.info("当前农场没有在执行的放牧计划")
            return
        self.ka._mobile_farm_graze_plan_update_status(planId=plan_id)
        plan_info_list = self.fq.query_plan_info_buy_plan_id(plan_id=plan_id)
        self.assertEqual(20, plan_info_list[0]["status"])

    def test_mobile_farm_task_detail(self):
        """
        移动端-农场任务-农场任务详情【v1.2.7 可对字段】
        :return:
        """
        farmid = random.choice(self.fq.query_default_farm(self.email)).get('farm_id')
        taskid = random.choice(self.fq.query_task_list_buy_farm_id(farm_id=farmid)).get('id')
        taskdetail = self.ka._mobile_farm_task_detail(taskId=taskid)
        taskinfo = self.fq.query_task_info_buy_task_id(task_id=taskid)[0]
        self.assertEqual(taskdetail.get('status'), 'OK')
        content = taskdetail.get('content')
        if content:
            self.assertEqual(content.get('taskName'), taskinfo.get('task_name'))
            self.assertEqual(content.get('status'), taskinfo.get('status'))
            self.assertEqual(content.get('id'), taskinfo.get('id'))
            self.assertEqual(content.get('farmId'), taskinfo.get('farm_id'))

            # 断言创建人信息
        createUser = content.get('createUser')
        if createUser:
            self.assertEqual(createUser.get('email'), taskinfo.get('email'))
            self.assertEqual(createUser.get('headImg'), taskinfo.get('head_img'))
            self.assertEqual(createUser.get('userName'), taskinfo.get('username'))
            self.assertEqual(createUser.get('phone'), taskinfo.get('phone'))
            self.assertEqual(createUser.get('id'), taskinfo.get('user_id'))

        # 断言接收人信息
        distributeUsers = content.get('distributeUsers')
        if distributeUsers:
            taskuserinfo = self.fq.query_farm_task_receiver_info(taskid=taskid)
            taskuserinfo = self.tool.del_dict_value_null(taskuserinfo)
            self.assertListEqual(taskuserinfo, distributeUsers)

        # 断言完成人信息
        completeUser = content.get('completeUser')
        if completeUser:
            completeuser = self.fq.query_task_info_complete_user(task_id=taskid)
            completeuser = self.tool.del_dict_value_null(completeuser)
            self.assertDictEqual(completeuser, completeUser)


if __name__ == '__main__':
    m = Main()
