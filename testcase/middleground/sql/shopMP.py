from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config
import re

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class mp_label(DataBaseOperate):
    def __init__(self):
        super(mp_label, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


    def git_admin_shop_add(self,name=None,remark=None):
        '''
        查询店铺
        :return:
        '''

        sql = r"select * from `mp-product`.`t_shop` where `name` = {} and `remark` = {} ;".format(name,remark)
        sql2 = "select * from `mp-product`.`t_shop` where id != '' order by id desc limit 1;"
        return self.operate_db(sql=sql2)

if __name__ == '__main__':
    t = mp_label().git_admin_shop_add()[0]['id']
    print(t)
