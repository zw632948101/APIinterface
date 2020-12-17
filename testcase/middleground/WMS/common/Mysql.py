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






# class MysqlUtil:
#
#     def __init__(self):
#         conf = configparser.ConfigParser()
#         conf.read(Public_mkdir,encoding='utf-8')
#         host = conf.get('mysql', 'host')
#         port = conf.getint('mysql', 'port')
#         user = conf.get('mysql', 'user')
#         password = conf.get('mysql', 'password')
#         database = conf.get('mysql','database')
#         try:
#             self.mysql = pymysql.connect(host=host,
#                                          user=user,
#                                          password=password,
#                                          database=database,
#                                          port=port,
#                                          cursorclass=pymysql.cursors.DictCursor)
#
#         except Exception as e :
#             print("数据库连接错误:{}".format(e))
#             raise e
#
#     def fetch_one(self,sql):
#         cursor = self.mysql.cursor()
#         cursor.execute(sql)
#         return cursor.fetchone()
#
#
#     def fetch_all(self,sql):
#         cursor = self.mysql.cursor()
#         cursor.execute(sql)
#         return cursor.fetchall()
#
#     def commit(self):
#         self.mysql.commit()
#
#     def close(self):
#         self.mysql.close()


if __name__ == '__main__':
    sql = "SELECT * FROM `t_warehouse_monitor`  where warehouse_id = 1  and is_delete != 1 order by id desc limit 1;"

    warehouse = mp_label().git_warehouse_monitor_is_delete()[0]['name']
    # 获取绑定关系的id，需要在解绑的时候传入
    print(warehouse)