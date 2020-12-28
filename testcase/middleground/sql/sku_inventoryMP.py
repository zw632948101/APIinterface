from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class mp_label(DataBaseOperate):
    def __init__(self):
        super(mp_label, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def git_sku_add(self,number):
        sql = "select * from `mp-product`.`t_sku` where id !='' order by id desc limit 1;" # 查最新的商品sku
        sql2 = "select count(*) from `mp-product`.`t_sku`;" # 查总条数
        if number == 1:
            return self.operate_db(sql=sql)
        elif number == 2:
            return self.operate_db(sql=sql2)
    def git_newest_sku(self):

        sql = ''


if __name__ == '__main__':
    t = mp_label().git_sku_add(1)
    # # sku_code = None
    # # for sku in t:
    # #     sku_code = sku['code']
    # # print(sku_code)
    # for i in t:
    #     print(i['count(*)'])
    print(t[0]['code'])
