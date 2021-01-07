from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config
import re

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class mpShopSql(DataBaseOperate):
    def __init__(self):
        super(mpShopSql, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def git_admin_shop_add(self, name=None, remark=None):
        '''
        查询店铺
        :return:
        '''

        sql = r"select * from `mp-product`.`t_shop` where `name` = {} and `remark` = {} ;".format(
            name, remark)
        sql2 = "SELECT * FROM `mp-product`.`t_shop` WHERE id != '' ORDER BY id DESC LIMIT 1;"
        return self.operate_db(sql=sql2)

    def query_wms_subject_info(self):
        """
        查询wms使用的主体信息
        :return:
        """
        sql = """
            SELECT CONCAT(ts.id,'') AS code, ts.name
            FROM `mp-shop`.t_subject ts
            WHERE ts.is_delete = 0
            ORDER BY ts.id DESC;
              """
        return self.operate_db(sql=sql)


if __name__ == '__main__':
    t = mpShopSql().git_admin_shop_add()[0]['id']
    print(t)
