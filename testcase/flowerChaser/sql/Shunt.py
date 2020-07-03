from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from tools.Config import Config, Log
import random
import os
import time

host_ip = Config('config').data['database'][Config('config').data['run']]['host_ip']



class ShuntingRecordsSql(object):
    L = logger("ShuntingRecordsSql")
    db = DataBaseOperate()

    def sql_all_shunt_records(self):
        """
        查询所有调车记录
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_shunt WHERE is_delete=0 ORDER BY create_time DESC ;"
        return self.db.operate(host_ip, sql)

    def sql_all_shunt_records_by_status(self, status):
        """
        查询指定状态的调车总数
        :param status: 1.调车中，2.已调车，3.已取消，4.已到达
        :return:
        """
        sql = 'SELECT COUNT(*)  FROM `fc-bee`.t_shunt WHERE is_delete=0 AND shunt_status = %s ORDER BY create_time DESC ;' % status
        return self.db.operate(host_ip, sql)

    def sql_all_shunt_records_by_usetime(self, start_usetime, end_usetime):
        """
        查询用车时间在指定时间内的用车记录
        :param start_usetime: 用车开始时间
        :param end_usetime: 用车结束时间
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_shunt WHERE is_delete=0 AND use_time BETWEEN '%s' AND '%s' ORDER BY create_time DESC;" % (start_usetime, end_usetime)
        return self.db.operate(host_ip, sql)

    def sql_all_shunt_records_by_createtime(self, create_start, create_end):
        """
        查询发布日期在指定时间内的用车记录
        :param create_start: 调车开始时间
        :param create_end: 调车结束时间
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_shunt WHERE is_delete=0 AND create_time BETWEEN '%s' AND '%s' ORDER BY create_time DESC;" % (create_start, create_end)
        return self.db.operate(host_ip, sql)

    def sql_shunt_page_list_by_issuer(self, phone):
        """
        根据发布人手机号查询调车记录
        :return:
        """
        sql = "SELECT tu.username, tu.phone, ts.* FROM `fc-bee`.t_shunt ts " \
              "LEFT JOIN `world-user`.t_user tu ON ts.user_id = tu.id AND tu.account_type = 21 AND ts.is_delete = 0 " \
              "WHERE tu.phone LIKE '%%%s%%' AND ts.user_id IS NOT NULL " \
              "ORDER BY ts.create_time DESC;" % (phone)

if __name__ == '__main__':
    sr = ShuntingRecordsSql()
    sr.sql_all_shunt_records_by_usetime('2020-5-12 09:00:00', '2020-6-16 00:00:00')
