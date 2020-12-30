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


    def git_web_order_close(self,orderNo):

        sql = "select order_status from `wx-mall`.`t_order` where order_no = {};".format(orderNo)
        return self.operate_db(sql=sql)

    # 查出 可以评价的订单号和该订单的商品编号
    def git_web_order_evaluate(self,name):
        sql = "select order_no,sku_no,order_status " \
              "from `wx-mall`.`t_order` as order_id join `wx-mall`.`t_order_item` as sku_id " \
              "on order_id.id = sku_id.order_id " \
              "where buyer_name = '{}' and order_status = 50;".format(name)
        return self.operate_db(sql=sql)
    # 查出已评价的订单状态 和 还原该订单状态为"未评价"
    def git_web_order_status(self,control = None,order_no=None):
        # 查订单状态
        if control:
            sql = "select buyer_name,order_status from `wx-mall`.`t_order` where order_no = '{}';".format(order_no)
            return self.operate_db(sql=sql)
        # 还原订单状态
        else:
            sql2 = "update  `wx-mall`.`t_order` set order_status = 50 where order_no = '{}';".format(order_no)
            return self.operate_db(sql=sql2)
    # 查一条最新的评价
    def git_web_order_product_evaluate(self):
        sql = "select * from `wx-mall`.`t_product_evaluate` where `status` = 1 order by id desc  limit 1;"
        return self.operate_db(sql=sql)

    def gei_web_sku_favorite(self):
        sql = ""

if __name__ == '__main__':
    import random
    # t = mp_label().gti_web_cart_add2(True)
    # print(type(t))
    # print(random.choice(t)['code'])
    #
    # b = mp_label().gti_web_cart_add2(False)
    # print(random.choice(b)['id'])

    # p = mp_label().git_web_order_evaluate('蜂友708528')
    # orderNo = p[0]['order_no']
    # skuNo = p[0]['sku_no']
    # print("订单编号:{0},商品编号:{1}".format(orderNo,skuNo))
    # print(p)
    # print(mp_label().git_web_order_evaluate('蜂友708528')[0]['sku_no'])
    order_status = mp_label().git_web_order_status(2020110709143999018005)
    print(order_status)
    evaluateNo = mp_label().git_web_order_product_evaluate()
    print(evaluateNo[0]['status'])
    print(evaluateNo[0]['evaluate_no'])
