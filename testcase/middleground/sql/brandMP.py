
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class mp_label(DataBaseOperate):
    def __init__(self):
        super(mp_label, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


    def git_admin_biz_add(self,ruleName_=None):
        '''
        查询业务名称

        :param ruleName_:
        :return:
        '''

        sql = "select * from `mp-product`.`t_biz_type` where `name` = {};".format(ruleName_)
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