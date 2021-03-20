import pymysql
import configparser
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config
from testcase.middleground.WMS.common.Pash import Public_mkdir


host_ip = config.get('database').get(config.get('run')).get('host_ip')

class mp_label(DataBaseOperate):
    def __init__(self):
        super(mp_label, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def git_warehouse_monitor(self,id_value):
        # 查出仓库ID为1的，绑定了摄像头的，且为"未解绑"状态的数据
        sql = "SELECT * FROM `mp-wms`.`t_warehouse_monitor` " \
              "where warehouse_id = {} " \
              " and is_delete != 1 " \
              "order by id desc limit 1;".format(id_value)
        return self.operate_db(sql=sql)
    def git_warehouse_monitor_is_delete(self):
        '''
        查询已绑定的设备仓库，且为未解绑的状态
        '''
        sql = "SELECT * FROM `mp-wms`.`t_warehouse_monitor` where is_delete != 0 order by id desc limit 1;"
        return self.operate_db(sql=sql)

    def git_warehouse_status(self):
        '''查询已启用状态得仓库'''
        sql = "select * from `mp-wms`.`t_warehouse` " \
              "where id in (select `id` from `mp-wms`.`t_warehouse` group by `name` having `status` = 1) " \
              "and `name` != '' order by id desc limit 1;"
        return self.operate_db(sql=sql)

    def git_warehouse_employee(self):
        '''查出仓库已绑定员工的关系id'''
        sql = "select * from `mp-wms`.`t_warehouse_employee` where is_delete = 0 order by id desc limit 1;"
        return self.operate_db(sql=sql)
    def gti_warehouse_erp_sync_log(self):
        '''查wms同步到erp的日志'''
        sql = "select * from `mp-wms`.t_warehouse_erp_sync_log where `status` = 1;"
        return self.operate_db(sql=sql)

    def git_whs_receipt(self,status=None):
        '''查不同状态入库单'''
        # 待入库
        if status == 0:
            sql = "select * from `mp-wms`.`t_whs_receipt` where `status` = 0 order by id desc limit 1;"
            return self.operate_db(sql=sql)
        # 已入库
        elif status == 1:
            sql = "select * from `mp-wms`.`t_whs_receipt` where `status` = 1 order by id desc limit 1;"
            return self.operate_db(sql=sql)
        # 已取消
        elif status == 2:
            sql = "select * from `mp-wms`.`t_whs_receipt` where `status` = 2 order by id desc limit 1;"
            return self.operate_db(sql=sql)
    def git_whs_receipt_notice(self):
        sql = "select * from `mp-wms`.`t_whs_receipt` " \
              "where `auto_receiving` = 0 " \
              "and `status` = 0 " \
              "and `source` = 'ERP' " \
              "order by id desc  limit 1;"
        return self.operate_db(sql=sql)





if __name__ == '__main__':
   t = mp_label().git_warehouse_status()
   print(t)