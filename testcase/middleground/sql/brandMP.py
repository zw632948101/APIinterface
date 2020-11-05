
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class mp_label(DataBaseOperate):
    def __init__(self):
        super(mp_label, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


    def git_admin_biz_add(self,):
        '''
        查询业务名称

        :param ruleName_:
        :return:
        '''

        sql = "select * from `mp-product`.t_biz_type where id != '' order by id desc limit 1;"
        return self.operate_db(sql=sql)

    def git_admin_biz_change_status(self,id_=None,status_=None):
        '''
        查询业务状态
        :param id_:
        :param status_:
        :return:
        '''
        sql = "select * from `mp-product`.`t_biz_type` where {} = 1 and `status` = {};".format(id_,status_)
        return self.operate_db(sql=sql)

    def git_admin_biz_list_all(self):
        '''
        查询所有业务
        :return:
        '''
        sql = "select * from `mp-product`.`t_biz_type` where id != '';"
        return self.operate_db(sql=sql)

    def git_admin_brand_add(self):
        '''
        查询最新的一个品牌
        :param name:
        :param logo:
        :return:
        '''
        sql = "select * from `mp-product`.t_brand where id != '' order by id  desc limit 1;"
        return self.operate_db(sql=sql)
    def git_admin_section_add(self):
        '''
        查询最新的号段
        '''
        sql = "select * from `mp-product`.`t_section_no` where id != '' order by id desc limit 1;"
        return self.operate_db(sql=sql)
    def git_admin_attr_name(self):
        '''
        查询最新的属性/规格
        '''
        sql = "select * from `mp-product`.`t_attr_name` where id != '' order by id desc limit 1;"
        return self.operate_db(sql=sql)
    def git_admin_label(self):
        '''
        查询最新的商品标签
        '''
        sql = "select * from `mp-product`.`t_label` where id != '' order by id  desc limit 1;"
        return self.operate_db(sql=sql)



if __name__ == '__main__':

    rulName = "蜂蜜汁"
    t = mp_label()
    tt = t.git_admin_biz_add()
    print(tt)