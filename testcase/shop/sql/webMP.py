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

    def gti_web_cart_add2(self,switch):
        # 查商品sku
        if switch:
            sql = "select `code` from `mp-product`.`t_sku` " \
                  "where  `status` = 1 " \
                  "and `code` in (select `sku_code` from `mp-product`.`t_inventory` where `quantity` > 200) " \
                  "order by id asc limit 1;"
            return self.operate_db(sql=sql)
        # 查店铺Id
        elif switch == False:
            sql = "select `id` from `mp-product`.`t_shop` where `status` = 0 limit 1;"
            return self.operate_db(sql=sql)
    def git_web_order(self):
        sql = "select * from `wx-mall`.`t_order`  where id != '' order by id desc ;"
        return self.operate_db(sql=sql)
if __name__ == '__main__':
    import random
    t = mp_label().gti_web_cart_add2(True)
    print(type(t))
    print(random.choice(t)['code'])

    b = mp_label().gti_web_cart_add2(False)
    print(random.choice(b)['id'])