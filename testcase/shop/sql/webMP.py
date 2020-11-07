from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config
import re

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class mp_label(DataBaseOperate):
    def __init__(self):
        super(mp_label, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def git_web_cart_add(self,number):
        if number == 1:
            sql_sku = "select `code` from `mp-product`.`t_sku` order by id desc limit 1;"
            return self.operate_db(sql=sql_sku)
        elif number == 2:
            sql_shop = "select * from `mp-product`.`t_shop` where `status` = '0' and `is_delete` = '0' order by id desc limit 1;"
            return self.operate_db(sql=sql_shop)

