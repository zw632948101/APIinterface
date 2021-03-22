from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')

class Bullpen(DataBaseOperate):
    def __init__(self):
        super(Bullpen, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def get_cattle(self,):
        """
        查询牛信息表数据
        """
        sql  = "SELECT `t_cattle`.id,`t_cattle`.cattle_no,`t_cattle`.cattle_ear_tag_no " \
               "FROM `bf-breed`.`t_cattle` " \
               "where is_delete != 1 and cattle_ear_tag_no != 'null' and cattle_no != 'null' " \
               "order by id desc limit 1;"

        return self.operate_db(sql=sql)
    def get_cattle_fence(self):
        sql = "select * from `bf-breed`.t_cattle_fence " \
              "where is_delete != '1' and fence_no != 'null' order by id asc limit 1;"

        return self.operate_db(sql=sql)

    def get_product_category_mapping(self):
        sql = "select `t_product_category_mapping`.`sku_code` from `bf-breed`.t_product_category_mapping " \
              "where is_delete != '1' order by id desc limit 1;"
        return self.operate_db(sql=sql)




if __name__ == '__main__':
    t = int(Bullpen().get_cattle()[0]['cattle_ear_tag_no']) + 1
    b = Bullpen().get_product_category_mapping()[0]['sku_code']
    print(b)