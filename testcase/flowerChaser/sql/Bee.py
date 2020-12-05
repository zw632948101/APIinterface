from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.log import log
from utils.environmentConfiguration import config
import random
import os
import datetime

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class ConfigInformationSql(object):
    db = DataBaseOperate()

    def query_province_id_by_province_name(self, province_name):
        sql = "SELECT id FROM `fc-bee`.t_region WHERE level = 0 AND full_name LIKE '%%%s%%';" % province_name
        info = self.db.operate(host_ip, sql)
        if info:
            return info[0]
        return

    def sql_id_by_full_name(self, full_name, parent_id):
        """
        根据名称查询对应的城市ID
        :param full_name:
        :return:
        """
        sql = "SELECT id FROM `fc-bee`.t_region WHERE level = 1 AND full_name LIKE '%%%s%%' AND parent_id = %s;" % (full_name, parent_id)
        return self.db.operate(host_ip, sql)

    def query_reason_cityid_by_full_name(self, city_id, full_name):
        sql = "SELECT id FROM `fc-bee`.t_region WHERE level = 2 AND `name` LIKE '%%%s%%' AND parent_id = %s;" % (
            full_name, city_id)

        info = self.db.operate(host_ip, sql)
        if info:
            return info[0]
        return

    def query_attach_all(self):
        """
        查询表中全部的URL链接
        """
        sql = """SELECT tb.url FROM `fc-bee`.t_bee_reserve_attach tb ;"""
        info = self.db.operate(host_ip, sql)
        if info:
            return info
        return


class NectarSourceInformationSql(object):
    db = DataBaseOperate()

    def sql_nectar_source_id_by_status(self):
        """
        查询未入驻状态的蜜源地
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_nectar_source WHERE `status`=1 AND is_delete=0;"
        return self.db.operate(host_ip, sql)

    def sql_nectar_source_id_by_status_id(self, status=2):
        """
        查询已入驻状态的蜜源地
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_nectar_source WHERE `status`='%s' AND is_delete=0;" % str(status)
        return self.db.operate(host_ip, sql)

    def sql_query_extract_add_png(self):
        """
        查询20张图片
        :return:
        """
        sql = """SELECT url FROM `fc-bee`.t_nectar_source_attach WHERE is_delete=0 ORDER BY rand() DESC LIMIT 20;"""
        return self.db.operate(host_ip, sql)

    def sql_all_nectar_source(self):
        """
        查询当前所有蜜源地
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_nectar_source WHERE is_delete=0 ORDER BY id DESC ;"
        return self.db.operate(host_ip, sql)

    def query_all_operator_list(self):
        """
        查詢全部操作人列表
        """
        sql = """
            SELECT
            bf.user_id AS userId ,bf.real_name AS userName ,bf.contact_number AS contactNumber ,ur.role_code AS roleCode
            ,tc.`value` AS roleStr
            FROM
            `fc-bee`.t_bee_friend bf
            INNER JOIN `fc-bee`.t_user_role ur ON ur.user_id = bf.user_id AND ur.is_delete = 0 AND ur.role_code IN (1005,1006,1002,1003,1004)
            INNER JOIN `fc-bee`.t_config tc ON tc.`key` = ur.role_code  AND tc.is_delete = 0 AND  tc.`code` = '10001'
            WHERE bf.is_delete = 0
            ORDER BY locate(ur.role_code,'1005,1006,1002,1003,1004') ,CONVERT(bf.user_name USING GBK) ASC;
              """
        return self.db.operate(host_ip, sql)

    def sql_nectar_source_by_id(self, id):
        """
        根据蜜源地id查询蜜源地
        :param id:
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_nectar_source WHERE id=%s;" % id
        return self.db.operate(host_ip, sql)

    def sql_nectar_source_type(self):
        """
        查询系统配置的蜜源品种
        :return:
        """
        sql = "SELECT tc.`key` FROM `fc-bee`.t_config tc WHERE tc.`code` = 10002 AND tc.is_delete = 0;"
        return self.db.operate(host_ip, sql)

    def sql_random_nectar_source_type(self, n):
        """
        随机查询n个蜜源品种类型
        :param n:
        :return:
        """
        sql = """SELECT DISTINCT tt.`key` typeCode FROM `fc-bee`.t_config tt WHERE tt.is_delete = 0 AND tt.`code`=10002 ORDER BY rand() LIMIT %s;""" % n
        return self.db.operate(host_ip, sql)

    def sql_nectar_car_length_type(self):
        """
        查询系统配置的车辆类型
        :return:
        """
        sql = "SELECT tc.`key`, tc.value FROM `fc-bee`.t_config tc WHERE tc.`code` = 10003 AND tc.is_delete = 0;"
        return self.db.operate(host_ip, sql)

    def sql_region(self, level):
        """
        查询系统配置的区号
        :return:
        """
        sql = "SELECT tr.`id` FROM `fc-bee`.t_region tr WHERE tr.`level` = '%s' AND tr.is_delete = 0;" % level
        return self.db.operate(host_ip, sql)

    def sql_nectar_source_last_seetle_time(self, nectar_source_id):
        """
        查询指定蜂场的最后一次入驻时间
        :return:
        """
        sql = 'SELECT enter_time FROM `fc-bee`.t_enter_record WHERE is_delete = 0 AND nectar_source_id = %s AND leave_time IS NULL ' \
              'ORDER BY enter_time DESC LIMIT 1;' % nectar_source_id
        enter_times = self.db.operate(host_ip, sql)[0]
        last_enter_time = datetime.datetime.strptime(enter_times.get("enter_time"), "%Y-%m-%d")
        return int(datetime.datetime.timestamp(last_enter_time) * 1000)


class ContainerInformationSql(object):
    db = DataBaseOperate()

    def sql_container_id_by_status(self):
        """
        查询待投放状态的养蜂平台
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_container WHERE `status`=1 AND is_delete=0;"
        return self.db.operate(host_ip, sql)

    def sql_all_container(self):
        """
        查询当前所有养蜂平台
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_container WHERE is_delete=0 ORDER BY id DESC;"
        return self.db.operate(host_ip, sql)

    def sql_container_by_status(self):
        """
        查询已投放已摇蜜状态的养蜂平台
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_container WHERE (`status`=2  OR  `status`=3) AND is_delete=0;"
        return self.db.operate(host_ip, sql)

    def get_random_platform(self):
        """
        生产随机平台列表字符串
        :return:
        """
        containers = self.sql_all_container()
        platform = ''
        for n in range(random.randint(1, len(containers))):
            platform += '%s,' % (random.choice(containers)["id"])
        final_platform = ','.join(set(platform[:-1].split(',')))
        return final_platform

    @staticmethod
    def get_random_img_list(img_num=3):
        """
        生产随机图片列表字符串
        :return:
        """
        current_path = os.path.dirname(os.path.abspath(__file__))
        current_path = current_path.replace('sql', 'testCase/user')
        urls = list(Config('imgUrl', current_path).data.values())
        img_list = ''
        final_urls = random.sample(urls, img_num)
        for url in final_urls:
            img_list += '"%s",' % url
        final_img_list = ','.join(img_list[:-1].split(','))
        return '[%s]' % final_img_list

    def sql_container_by_nectar_source_id(self, nectar_source_id):
        """
        通过蜜源地查询当前蜜源地已入驻的养蜂平台
        :return:
        """
        sql = """
        SELECT * FROM `fc-bee`.t_container WHERE nectar_source_id=%s AND is_delete=0 ORDER BY enter_time DESC;
        """ % nectar_source_id
        return self.db.operate(host_ip, sql)

    def sql_container_by_id(self, id):
        """
        通过平台id查询养蜂平台
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_container WHERE id=%s ;" % id
        return self.db.operate(host_ip, sql)


class ExtractInformationSql(object):
    db = DataBaseOperate()

    def sql_all_extract_record(self):
        """
        查询所有摇蜜记录
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_extract_record WHERE  is_delete=0 ORDER BY id DESC ;"
        return self.db.operate(host_ip, sql)

    def sql_extract_record_detail_by_extract_record_id(self, extract_record_id):
        """
        根据摇蜜记录ID查询摇蜜记录详情
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_extract_record_detail " \
              "WHERE extract_record_id=%s AND is_delete=0 ORDER BY enter_time DESC;" % extract_record_id
        return self.db.operate(host_ip, sql)

    def sql_extract_record_by_extract_record_id(self, extract_record_id):
        """
        根据摇蜜记录ID查询摇蜜记录
        :param extract_record_id:
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_extract_record " \
              "WHERE id=%s AND is_delete=0 ;" % extract_record_id
        return self.db.operate(host_ip, sql)

    def sql_mobile_extract_operator(self):
        """
        查找所有摇蜜记录的操作人（养蜂总监、养蜂技师、养蜂助理）
        :return:
        """
        sql = "SELECT tu.username FROM `world-user`.t_user tu WHERE id IN (SELECT user_id FROM `fc-bee`.t_user_role tur WHERE tur.role_code IN (1002, 1003, 1004) AND tur.is_delete=0) AND is_delete=0 AND status IN (1,2) ORDER BCONVERT(tu.username USING gbk) COLLATE gbk_chinese_ci ASC;"
        return self.db.operate(host_ip, sql)


class StatisticsSql(object):
    db = DataBaseOperate()

    def sql_statistics_nectar_source(self):
        """
        蜜源分布统计
        :return:
        """
        sql = """
        # 蜜源省分布
        SELECT 
            tr.`name` article,
            tr.`id` province,
            SUM(IF(tns.`status`=1, 1, 0)) readyNum,
            SUM(IF(tns.`status`=2, 1, 0)) workingNum,
            SUM(IF(tns.`status`=3, 1, 0)) completedNum,
            COUNT(tns.province) total
        FROM `fc-bee`.t_nectar_source tns
        LEFT JOIN `fc-bee`.t_region tr ON tns.province = tr.id
        WHERE tns.is_delete = 0 AND tr.is_delete = 0
        GROUP BY tns.province;
        # 蜜源合计
        SELECT 
            '合计' article,
            SUM(IF(tns.`status`=1, 1, 0)) readyNum,
            SUM(IF(tns.`status`=2, 1, 0)) workingNum,
            SUM(IF(tns.`status`=3, 1, 0)) completedNum,
            COUNT(tns.province) total
        FROM `fc-bee`.t_nectar_source tns
        LEFT JOIN `fc-bee`.t_region tr ON tns.province = tr.id
        WHERE tns.is_delete = 0 AND tr.is_delete = 0;
        """
        return self.db.operate(host_ip, sql)

    def sql_statistics_nectar_source_type(self):
        """
        蜜源类型统计
        :return:
        """
        sql = """
        SELECT
            tt.`key` typeCode,
            tt.`value` typeName,
            COUNT(tns.type) typeNum
        FROM `fc-bee`.t_nectar_source tns
        LEFT JOIN `fc-bee`.t_config tt ON tns.type = tt.`key`
        WHERE tns.is_delete = 0 AND tt.`code`=10002
        GROUP BY tns.type;
        """
        return self.db.operate(host_ip, sql)

    def sql_statistics_nectar_type(self):
        """
        蜂蜜类型统计
        :return:
        """
        sql = """
        SELECT 
            tt.`value` typeName,
            tt.`key` typeCode,
            SUM(ter.weight) typeWeight
        FROM `fc-bee`.t_extract_record ter
        LEFT JOIN `fc-bee`.t_config tt ON ter.nectar_source_type = tt.`key`
        WHERE ter.is_delete = 0 AND tt.`code`=10002
        GROUP BY ter.nectar_source_type;
        """
        return self.db.operate(host_ip, sql)

    def query_count_of_container(self, time_stamp):
        """
        平台统计
        :parameter time_stamp: 开始时间戳, 秒
        :return:
        """
        sql = """
        SELECT 
            trcm.month_no label,
            CONCAT_WS(', ', keeping_num, ready_num, extracted_num) `value`
        FROM `fc-bee`.t_report_container_month trcm
        WHERE trcm.is_delete = 0 
        AND trcm.month_no = DATE_FORMAT( FROM_UNIXTIME(%d), '%%Y-%%m');
        """ % time_stamp
        return self.db.operate(host_ip, sql)

    def query_count_of_hive(self, time_stamp):
        """
        蜂箱统计
        :parameter time_stamp: 开始时间戳, 秒
        :return:
        """
        sql = """
        SELECT 
            trhm.month_no monthNo,
            trhm.hive_num hiveNum
        FROM `fc-bee`.t_report_hive_month trhm
        WHERE trhm.is_delete = 0 
        AND trhm.month_no = DATE_FORMAT( FROM_UNIXTIME(%d), '%%Y-%%m');
        """ % time_stamp
        return self.db.operate(host_ip, sql)

    def query_count_of_honey(self, time_stamp):
        """
        蜂蜜统计
        :parameter time_stamp: 开始时间戳, 秒
        :return:
        """
        sql = """
            SELECT 
                trnm.month_no monthNo,
                trnm.container_num containerNum,
                trnm.hive_num hiveNum,
                trnm.nectar_weight nectarWeight,
                trnm.`avg` `avg`
            FROM `fc-bee`.t_report_nectar_month trnm
            WHERE trnm.is_delete = 0 
            AND trnm.month_no = DATE_FORMAT( FROM_UNIXTIME(%d), '%%Y-%%m');
        """ % time_stamp
        return self.db.operate(host_ip, sql)


class ClinteleSql(DataBaseOperate):
    def __init__(self):
        super(ClinteleSql, self).__init__()

    def query_customer_and_swarm_info(self, phone):
        """
        通过手机号查询蜂农和蜂群资料
        :param phone:
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_bee_friend tc LEFT JOIN `fc-bee`.t_swarm_info ts ON tc.id=ts.bee_friend_id WHERE tc.is_delete = 0 AND tc.contact_number = '%s';" % phone
        info = self.operate(host=host_ip, sql=sql)
        if info:
            return info[0]
        else:
            return

    def query_constomer_all_info(self, pn=None, ps=None, phone=None):
        """
        查询客户资料
        :param pn:
        :param ps:
        :param phone:
        :return:
        """
        limit = "LIMIT %s,%s" % (pn, ps) if ps else ''
        phone = "AND tc.contact_number = '%s'" % phone if phone else ''
        sql = """
            SELECT
                tc.id ,
                tc.keeper_name as keeperName,
                UNIX_TIMESTAMP( tc.recent_visit_time ) * 1000 as recentVisitTime,
                tc.sale_intention as saleIntention,
                tc.contact_number as contactNumber,
                CASE tc.sale_intention WHEN 1 THEN '无' WHEN 2 THEN '一般' WHEN 3 THEN '强烈' END saleIntentionStr
            FROM
                `fc-bee`.t_customer tc 
                WHERE tc.is_delete = 0
                %s
                ORDER BY tc.recent_visit_time DESC,tc.sale_intention DESC ,tc.id ASC
                %s;
              """ % (phone, limit)
        info = self.operate(host=host_ip, sql=sql)
        if info:
            return info
        else:
            return

    def query_bee_friend_According_to_the_condition(self, pn=None, ps=None, phone=None, province_id=None, city_id=None,
                                                    county=None, lng=None, lat=None, cooperationIntentions=None,
                                                    searchType=None, distanceType=None):
        """
        根据条件查询蜂友资料
        :param pn: 页码
        :param ps: 查询条数
        :param phone: 手机号
        :param province_id: 省id
        :param city_id: 市id
        :param county: 区/县id
        :param lng: 经度
        :param lat: 纬度
        :param cooperationIntentions: 合作意向
        :param searchType: 筛选类型1查询经纬度距离，2根据省市区查询无距离
        :param distanceType:距离类型
        :return:
        """
        if searchType == 1:
            lng = lat = 'NULL'
            pcc = "AND t.province = %s AND t.city = %s AND t.county = %s" % (province_id, city_id, county)
        else:
            pcc = ''
        if lng is None:
            lng = lat = 'NULL'
        limit = "LIMIT %s,%s" % (pn, ps) if ps else ''
        phone = "AND tc.contact_number = '%s'" % phone if phone else ''
        if isinstance(cooperationIntentions, tuple):
            ci = "AND (t.sale_intention != 1 OR t.willingness != 1)"
        elif cooperationIntentions == 1:
            ci = "AND t.sale_intention != 1"
        elif cooperationIntentions == 2:
            ci = "AND t.willingness != 1"
        else:
            ci = ''
        if distanceType:
            dt_l = ['10000', '50000', '100000', '200000']
            dt = "AND t.distance <= " + dt_l[distanceType]
        else:
            dt = ''
        sql = """
            SELECT 
                t.contact_number AS contactNumber,
                t.distance,
                t.id,
                t.keeper_name AS keeperName,
                UNIX_TIMESTAMP( t.recent_visit_time ) * 1000 AS recentVisitTime,
                t.sale_intention AS saleIntention,
                CASE t.sale_intention WHEN 1 THEN '无卖蜂意向' WHEN 2 THEN '卖蜂意向一般' WHEN 3 THEN '卖蜂意向强烈' END saleIntentionStr
            FROM (SELECT
                ROUND(
                6378.137 * 2 * ASIN(
                SQRT(
                POW( SIN( ( %s * PI( ) / 180 - tb.lat * PI( ) / 180 ) / 2 ), 2 ) + COS( %s * PI( ) / 180 ) * COS( tb.lat * PI( ) / 180 ) * POW( SIN( ( %s * PI( ) / 180 - tb.lng * PI( ) / 180 ) / 2 ), 2 ) 
                ) ) * 1000 ) AS distance,tb.* 
            FROM
                `fc-bee`.t_bee_friend tb) AS t
                WHERE t.is_delete = 0
                %s %s %s %s
            ORDER BY t.distance ASC,t.recent_visit_time DESC
            %s;
              """ % (lat, lat, lng, pcc, ci, dt, phone, limit)
        info = self.operate(host=host_ip, sql=sql)
        if info:
            return info
        else:
            return

    def query_swarm_all_info(self, sid=None):
        """
        查询蜂群信息
        :param id:
        :return:
        """
        sid = "AND ts.id = '%s'" % sid if sid else ''
        sql = """
        SELECT * FROM `fc-bee`.t_swarm_info ts WHERE ts.is_delete = 0 %s ;
              """ % sid
        info = self.operate(host=host_ip, sql=sql)
        if info:
            if sid:
                return info[0]
            return info
        else:
            return

    def query_all_bee_clue_info(self):
        """
        获取全部的卖蜂线索
        :return:
        """
        sql = """
        SELECT * FROM `fc-bee`.t_bee_clue tb WHERE tb.status = 1 AND tb.is_delete = 0 ;
              """
        info = self.operate(host=host_ip, sql=sql)
        if info:
            return info
        else:
            return

    def query_all_bee_clue_by_phone(self, phone):
        """
        通过手机号查询卖蜂线索
        :param phone:
        :return:
        """
        sql = """
        SELECT * FROM `fc-bee`.t_bee_clue tb WHERE tb.contact_number = '%s' AND tb.is_delete = 0 ;
              """ % phone
        info = self.operate(host=host_ip, sql=sql)
        if info:
            return info[0]
        else:
            return


class BeeSettleInRecordSql(object):
    db = DataBaseOperate()

    def query_test(self):
        sql = "SELECT * FROM `fc-bee`.t_user_info WHERE is_delete = 0;"
        return self.db.operate(host_ip, sql)


class VisitRecordSql(object):
    db = DataBaseOperate()

    def sql_all_customer(self):
        """
        查询所有的客户
        :return:
        """
        sql = """SELECT * FROM `fc-bee`.t_bee_friend WHERE  is_delete=0 ORDER BY id DESC ;"""
        return self.db.operate(host_ip, sql)

    def sql_bee_friend_phone_by_user_id(self, user_id):
        """
        查询蜂友的电话号码
        :return:
        """
        sql = """SELECT phone FROM `world-user`.t_user WHERE id = %s;""" % user_id
        return self.db.operate(host_ip, sql)

    def sql_all_swarm_info(self):
        """
        查询所有的蜂群
        :return:
        """
        sql = """SELECT * FROM `fc-bee`.t_swarm_info WHERE  is_delete=0 ORDER BY id DESC ;"""
        return self.db.operate(host_ip, sql)

    def sql_bee_friend_by_id(self, id):
        """
        根据蜂友id查询蜂友详情
        :param id:
        :return:
        """
        sql = """SELECT * FROM `fc-bee`.t_bee_friend WHERE  id=%s AND is_delete=0  ORDER BY id DESC ;""" % id
        return self.db.operate(host_ip, sql)

    def query_swarm_info_by_friend_id(self, user_id):
        """
        根据蜂友id查询蜂群信息
        :param user_id:
        :return:
        """
        sql = """SELECT
                    tsi.* 
                FROM
                    `fc-bee`.t_swarm_info tsi 
                WHERE
                    tsi.user_id = '%s' 
                    AND tsi.is_delete = 0;""" % user_id
        return self.db.operate(host_ip, sql)

    def query_friend_info_by_user_id(self, user_id):
        # 通过userId查询蜂友信息
        sql = """
               SELECT
                    tbf.* ,
                    tml.label_type
                FROM
                    `fc-bee`.t_bee_friend tbf 
                    LEFT JOIN `fc-bee`.t_business_label tml ON tbf.user_id = tml.user_id
                WHERE
                    tbf.user_id = '%s' 
                    AND tml.is_delete = 0
                    AND tbf.is_delete = 0;""" % user_id
        return self.db.operate(host_ip, sql)

    def query_label_type(self):
        # 查询互助信息标签
        sql = """
               SELECT
                    tc.`key`,
                    tc.`value` 
                FROM
                    `fc-bee`.t_config tc 
                WHERE
                    tc.`code` = 10006;"""
        return self.db.operate(host_ip, sql)

    def query_contact_number_buy_user(self, user_id):
        # 通过user_id查询手机号
        sql = """
               SELECT
                    tbf.contact_number
                FROM
                    `fc-bee`.t_bee_friend tbf
                WHERE
                    tbf.user_id = '%s';""" % user_id
        return self.db.operate(host_ip, sql)

    def query_vehicle_length(self):
        # 查询可通行车辆长度
        sql = """
               SELECT
                    tc.`key`,
                    tc.`value` 
                FROM
                    `fc-bee`.t_config tc 
                WHERE
                    tc.`code` = 10003;"""
        return self.db.operate(host_ip, sql)

    def query_regular_source(self):
        # 查询蜜源品种枚举值
        sql = """
               SELECT
                    tc.`key`,
                    tc.`value` 
                FROM
                    `fc-bee`.t_config tc 
                WHERE
                    tc.`code` = 10002;"""
        return self.db.operate(host_ip, sql)

    def query_swarm_detail(self):
        # 查询蜂场信息
        sql = """
               SELECT
                    si.*
                FROM
                    `fc-bee`.t_swarm_info si
                WHERE
                    si.is_delete =0;"""
        return self.db.operate(host_ip, sql)


class BeeClueSql(object):
    db = DataBaseOperate()

    def sql_all_bee_clue(self):
        """
        查询所有卖蜂线索
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_bee_clue WHERE is_delete=0 AND status=1 ORDER BY create_time DESC;"
        info = self.db.operate(host=host_ip, sql=sql)
        if info:
            return info[0]
        else:
            return

    def sql_bee_clue_by_mobile(self, contact_number):
        """
        通过手机号查询卖蜂线索
        :param contact_number:
        :return:
        """
        sql = "SELECT * FROM `fc-bee`.t_bee_clue WHERE is_delete=0 AND status=1 AND contact_number = %s ORDER BY create_time DESC;" % contact_number
        return self.db.operate(host=host_ip, sql=sql)

    def sql_bee_clue_order_by_contact(self):
        """
        查询卖蜂线索列表排序
        :return:
        """
        sql = 'SELECT * FROM `fc-bee`.t_bee_clue WHERE is_delete=0 AND status=1 ORDER BY contact_time ASC , create_time DESC;'
        return self.db.operate(host=host_ip, sql=sql)

    def sql_bee_clue_detail(self, id):
        """
        查看卖蜂线索详情
        :param id:
        :return:
        """
        sql = 'SELECT * FROM `fc-bee`.t_bee_clue WHERE is_delete=0 AND status=1 AND id = %s;' % id
        return self.db.operate(host=host_ip, sql=sql)

    def sql_bee_clue_is_delete(self, id):
        """
        查询已删除卖蜂线索
        :param id:
        :return:
        """
        sql = 'SELECT * FROM `fc-bee`.t_bee_clue WHERE is_delete=1 AND status=1 AND id = %s;' % id
        return self.db.operate(host=host_ip, sql=sql)

    def query_user_nectar_soure_list(self, userid):
        """
        通过userID查询用户蜜源地-列表
        :param userid:
        :return:
        """
        sql = """
                SELECT
                    tu.province,
                    tu.county,
                    (SELECT tr.name FROM `fc-bee`.t_region tr WHERE tr.level = 2 AND tr.id = tu.county) as countyName,
                    tu.id,
                    (SELECT tr.name FROM `fc-bee`.t_region tr WHERE tr.level = 0 AND tr.id = tu.province) as provinceName,
                    (SELECT tr.name FROM `fc-bee`.t_region tr WHERE tr.level = 1 AND tr.id = tu.city) as cityName,
                    tu.city,
                    tu.lat,
                    tu.lng
                FROM
                    `fc-bee`.t_user_nectar_source tu 
                WHERE
                    tu.creator_id = '%s' 
                    AND tu.is_delete = 0 
                ORDER BY
                    tu.id DESC;
              """ % userid
        sql_info = self.db.operate(host=host_ip, sql=sql)
        if sql_info:
            return sql_info
        return

    def query_city_and_county_name_list(self, searchContent):
        """
        根据搜索关键字查询对应的地址
        :param searchContent:
        :return:
        """
        sql = """
                SELECT 
                    t.city,
                    t.cityFullName,
                    t.cityName,
                    t.county,
                    t.countyFullName,
                    t.countyName,
                    t.lat,
                    t.lng,
                    tr.id as province,
                    tr.full_name as provinceFullName,
                    tr.name as provinceName
                FROM `fc-bee`.t_region tr 
                RIGHT JOIN(SELECT
                    CASE tr_co.LEVEL WHEN 2 THEN tr_co.id END AS county,
                    CASE tr_co.LEVEL WHEN 2 THEN tr_co.full_name END AS countyFullName,
                    CASE tr_co.LEVEL WHEN 2 THEN tr_co.NAME END AS countyName,
                    CASE tr_co.LEVEL WHEN 1 THEN tr_co.id ELSE (SELECT t.id FROM `fc-bee`.t_region t WHERE t.level = 1 AND t.id = tr_co.parent_id) END AS city,
                    CASE tr_co.LEVEL WHEN 1 THEN tr_co.full_name ELSE (SELECT t.full_name FROM `fc-bee`.t_region t WHERE t.level = 1 AND t.id = tr_co.parent_id) END AS cityFullName,
                    CASE tr_co.LEVEL WHEN 1 THEN tr_co.NAME ELSE (SELECT t.NAME FROM `fc-bee`.t_region t WHERE t.level = 1 AND t.id = tr_co.parent_id) END AS cityName,
                    CASE tr_co.LEVEL WHEN 1 THEN tr_co.parent_id ELSE (SELECT t.parent_id FROM `fc-bee`.t_region t WHERE t.level = 1 AND t.id = tr_co.parent_id) END AS parent_id,
                    tr_co.lng,
                    tr_co.lat
                FROM
                    `fc-bee`.t_region tr_co 
                WHERE
                    tr_co.LEVEL IN ( '2', '1' ) 
                    AND tr_co.full_name LIKE '%{0}%') AS t ON tr.id = t.parent_id ;
              """.format(searchContent)
        sql_info = self.db.operate(host=host_ip, sql=sql)
        if sql_info:
            return sql_info
        return


class PurchaseSql(object):
    db = DataBaseOperate()

    def query_customer_id(self):
        """
        查询客户id
        :return:
        """
        sql = """ 
                SELECT
                    tc.user_id 
                FROM
                    `fc-bee`.t_bee_friend tc
                WHERE
                    tc.is_delete = 0;"""
        return self.db.operate(host_ip, sql)

    def query_purchase_id(self):
        """
        查询事件id
        :return:
        """
        sql = """ 
               SELECT
                    * 
                FROM
                    `fc-bee`.t_contract 
                WHERE
                    is_delete = 0 
                ORDER BY
                    id DESC;"""
        return self.db.operate(host_ip, sql)

    def query_contract_id(self):
        """
        查询合同id
        :return:
        """
        sql = """
            SELECT
                tp.id,
                tp.`status` 
            FROM
                `fc-bee`.t_contract tp 
            WHERE
                tp.is_delete = 0 
                AND tp.STATUS != 3;
             """
        return self.db.operate(host_ip, sql)

    def query_contract_info_by_contract_id(self, contract_id):
        """
        根据合同id查询合同信息
        :return:
        """
        sql = """ 
                SELECT
                    tc.friend_id,
                    tc.contract_no,
                    tc.`status`,
                    tc.amount,
                    tc.handsel,
                    tc.identity_front,
                    tc.identity_back,
                    tc.bank_front,
                    tc.bank_back,
                    tc.contract_pics,
                    tc.sign_time,
                    tcd.* 
                FROM
                    `fc-bee`.t_contract tc
                    LEFT JOIN `fc-bee`.t_contract_detail tcd ON tc.id = tcd.contract_id
                WHERE
                    tcd.is_delete = 0 
                    AND tc.id = %s
                ORDER BY
                    tc.create_time DESC;""" % (contract_id)
        return self.db.operate(host_ip, sql)

    def query_contract_info(self, friend_id, creator_id):
        """
        查询客户下最新的合同详情信息
        :return:
        """
        sql = """ 
                SELECT
                    tc.friend_id,
                    tc.contract_no,
                    tc.`status`,
                    tc.amount,
                    tc.handsel,
                    tc.identity_front,
                    tc.identity_back,
                    tc.bank_front,
                    tc.bank_back,
                    tc.contract_pics,
                    tc.sign_time,
                    tcd.* 
                FROM
                    `fc-bee`.t_contract tc
                    LEFT JOIN `fc-bee`.t_contract_detail tcd ON tc.id = tcd.contract_id
                WHERE
                    tc.is_delete = 0 
                    AND tcd.is_delete = 0 
                    AND tc.user_id = %s
                ORDER BY
                    tc.create_time DESC LIME 1;""" % friend_id
        return self.db.operate(host_ip, sql)

    def query_purchase_detail(self, contract_id):
        """
        通过采购单id查询采购单详情
        :return:
        """
        sql = """SELECT
                    *
                FROM
                    `fc-bee`.t_contract tc
                    LEFT JOIN `fc-bee`.t_contract_detail tcd ON tc.id = tcd.contract_id 
                WHERE
                    tc.is_delete = 0 
                    AND tcd.is_delete = 0 
                    AND tc.id =%s;""" % contract_id
        return self.db.operate(host_ip, sql)

    def query_purchase_list(self, customer_id, pn, ps):
        """
        通过客户id及分页规则查询采购单list
        :return:
        """
        sql = """ 
                SELECT
                    tc.*, tcd. hive_num
                FROM
                    `fc-bee`.t_contract tc
                    LEFT JOIN `fc-bee`.t_contract_detail tcd ON tcd.contract_id =tc.id
                WHERE
                    tc.is_delete = 0 
                    AND tc.friend_id = %s
                    ORDER BY tc.create_time DESC
                    LIMIT %s, %s;""" % (customer_id, (pn - 1) * 20, ps)
        return self.db.operate(host_ip, sql)

    def sql_contract_view_by_friend_id(self, friend_id):
        """
        根据客户id查询最新的合同
        :param friend_id:
        :return:
        """
        sql = """SELECT
                    * 
                FROM
                    `fc-bee`.t_contract 
                WHERE
                    friend_id = %s 
                ORDER BY
                    create_time DESC LIMIT 1;""" % friend_id
        return self.db.operate(host_ip, sql)


class HelpSql(object):
    db = DataBaseOperate()

    def sql_help_info_by_user_id(self):
        sql = """SELECT * FROM  `fc-bee`.t_help_info WHERE is_delete = 0 AND `status` = 0;"""
        return self.db.operate(host_ip, sql)

    def sql_help_info(self):
        sql = """SELECT * FROM  `fc-bee`.t_help_info WHERE is_delete = 0;"""
        return self.db.operate(host_ip, sql)

    def sql_help_comment_by_user_id(self, user_id):
        sql = """SELECT * FROM  `fc-bee`.t_help_comment WHERE comment_user_id=%s AND is_delete = 0;""" % user_id
        return self.db.operate(host_ip, sql)

    def sql_help_comment(self):
        sql = """SELECT * FROM  `fc-bee`.t_help_comment WHERE  is_delete = 0;"""
        return self.db.operate(host_ip, sql)


class ShuntSql(object):
    db = DataBaseOperate()

    def sql_shunt_buy_status(self, shunt_status, user_id):
        """
        通过用户ID查询对应调车状态的调车信息
        :return:
        """
        sql = """ 
                   SELECT
                        ts.id 
                    FROM
                        `fc-bee`.t_shunt ts 
                    WHERE
                        ts.is_delete = 0 
                        AND ts.shunt_status = '%s'
                        AND ts.user_id = '%s';""" % (shunt_status, user_id)
        return self.db.operate(host_ip, sql)

    def sql_shunt_buy_id(self, shunt_id):
        """
        通过调车记录ID查询对应调车详情
        :return:
        """
        sql = """ SELECT
                        ts.*
                    FROM
                        `fc-bee`.t_shunt ts
                    WHERE
                        ts.id = '%s';""" % shunt_id
        return self.db.operate(host_ip, sql)


# class BeekeeperNearbySql(DataBaseOperate):
#     log = logger('执行周边蜂友相关sql查询')
#
#     def sql_mobile_nearby_bee_friend_page_list(self):
#         pass


class PersonalSql(object):
    db = DataBaseOperate()

    def sql_mutual_label_type(self, n):
        """
        随机选择n个互助标签
        :return:
        """
        sql = """
                SELECT DISTINCT
                    tt.`key` typeCode
                FROM `fc-bee`.t_config tt 
                WHERE tt.is_delete = 0 AND tt.`code`=10006
                ORDER BY rand() LIMIT %s;
                """ % n
        return self.db.operate(host_ip, sql)

    def sql_random_statistics_nectar_source_type(self, n):
        """
        随机选择n个蜜源类型
        :return:
        """
        sql = """
                SELECT DISTINCT
                    tt.`key` typeCode
                FROM `fc-bee`.t_config tt
                WHERE tt.is_delete = 0 AND tt.`code`=10002
                ORDER BY rand() LIMIT %s;
                """ % n
        return self.db.operate(host_ip, sql)


class UserAuthData(DataBaseOperate):
    """
        实名认证MySQL数据查询
    """

    def __init__(self):
        super(UserAuthData, self).__init__()


class ShuntSql(object):
    db = DataBaseOperate()

    def sql_shunt_buy_status(self, shunt_status, user_id):
        """
        通过用户ID查询对应调车状态的调车信息
        :return:
        """
        sql = """ 
                   SELECT
                        ts.id 
                    FROM
                        `fc-bee`.t_shunt ts 
                    WHERE
                        ts.is_delete = 0 
                        AND ts.shunt_status = '%s'
                        AND ts.user_id = '%s';""" % (shunt_status, user_id)
        return self.db.operate(host_ip, sql)

    def sql_shunt_buy_id(self, shunt_id):
        """
        通过调车记录ID查询对应调车详情
        :return:
        """
        sql = """ SELECT
                        ts.*
                    FROM
                        `fc-bee`.t_shunt ts
                    WHERE
                        ts.id = '%s';""" % shunt_id
        return self.db.operate(host_ip, sql)

    def query_shunt_list_info(self, userid):
        """
        通过userID查询调车信息列表
        :param userid: 用户ID
        :return: 返回list
        """
        sql = """
            SELECT
                ts.id AS id,
                ts.loading_type AS loadingType,
                CASE ts.loading_type WHEN 1 THEN '挑蜂' WHEN 2 THEN '吊装' WHEN 3 THEN '叉车' ELSE '未知' END loadingDesc,
                UNIX_TIMESTAMP(ts.use_time)*1000 AS useTime,
                ts.cargo_name AS cargoName,
                ts.amount,
                CASE WHEN ts.cargo_name = '蜂蜜' THEN '桶' WHEN ts.cargo_name IN ( '蜜蜂', '蜂箱' ) THEN '箱' WHEN ts.cargo_name IN ( '空桶', '空托盘', '空木箱', '杂件' ) THEN '个'  END unit,
                ts.min_weight AS minWeight,
                ts.max_weight AS maxWeight,
                ts.min_capacity AS minCapacity,
                ts.max_capacity AS maxCapacity,
                ts.use_type AS useType,
                ts.truck_length_list AS truckLengthList,
                ts.truck_type_list AS truckTypeList,
                ts.remark AS remark,
                ts.shunt_status AS shuntStatus,
                CASE ts.shunt_status  WHEN 1 THEN '调车中'  WHEN 2 THEN '已调车'  WHEN 3 THEN '已取消'  WHEN 4 THEN '已完成'  END shuntStatusDesc,
                ts.cancel_reasons as cancelReasons,
                UNIX_TIMESTAMP(ts.create_time)*1000  AS createTime,
	            UNIX_TIMESTAMP(ts.edit_time)*1000  AS editTime,
	            UNIX_TIMESTAMP(ts.arrival_time)*1000  AS arrivalTime,
	            ts.driver_name AS driverName,
                ts.driver_telephone AS driverTelephone,
                ts.plate_number AS plateNumber,
                ts.create_id AS createId,
                ta.address, ta.address_type AS addressType , ta.city , ta.county,
                ta.creator_id as creatorId, ta.id as address_id, ta.lat, ta.lng, ta.province, ta.location_name as locationName
            FROM
                `fc-bee`.t_shunt ts 
                LEFT JOIN `fc-bee`.t_shunt_address ta ON ta.id = ts.load_address_id OR ta.id = ts.unload_address_id
            WHERE
                ts.user_id = '%s' 
                AND ts.is_delete = 0 
            ORDER BY
            ts.create_time DESC;
              """ % userid
        info = self.db.operate(host_ip, sql)
        if not info:
            return
        return info

    def query_chunt_address_info_list(self, addressType, userid):
        """
        通过userID和addresstype查询地址簿列表
        :param addressType: 装卸货地址类型，1,装货地址，2卸货地址
        :param userid: 用户ID
        :return:
        """
        sql = """
                SELECT
                    ta.address,
                    ta.address_type AS addressType,
                    ta.city,
                    ta.county,
                    ta.creator_id AS creatorId,
                    ta.id,
                    ta.lat,
                    ta.lng,
                    ta.province,
                    ta.location_name AS locationName 
                FROM
                    `fc-bee`.t_shunt_address ta 
                WHERE
                    ta.creator_id = '%s' 
                    AND ta.address_type = %s 
                ORDER BY
                    ta.create_time DESC;
              """ % (userid, addressType)
        info = self.db.operate(host_ip, sql)
        if not info:
            return
        return info


class BeekeeperNearbySql(object):
    def __init__(self):
        from utils.databaseConnection.DataBaseOperatePool import DataBaseOperate
        self.__db = DataBaseOperate()
        self.__db.creat_db_pool(host_ip)

    def __del__(self):
        self.__db.close_db_pool()

    def sql_beekeeper_nearby_search_content_random(self):
        from threading import Thread
        sql_dict = {"mutual_labels_all": 'SELECT `value` FROM `fc-bee`.t_config WHERE code=10006 AND is_delete=0',
                    "user_name": 'SELECT username FROM `world-user`.t_user ORDER BY rand() LIMIT 1;',
                    "user_mobile": 'SELECT phone FROM `world-user`.t_user WHERE phone IS NOT NULL ORDER BY rand() LIMIT 1;',
                    "user_id": 'SELECT id FROM `world-user`.t_user WHERE phone IS NOT NULL ORDER BY rand() LIMIT 1;',
                    }
        thread_list, sql_result = list(), dict()

        for sql_name, sql in sql_dict.items():
            t = Thread(target=lambda sql_name_, sql_: sql_result.update({sql_name_: self.__db.query_data(sql_)}),
                       args=(sql_name, sql))
            t.start()
            thread_list.append(t)
        [thread_item.join() for thread_item in thread_list]
        return sql_result

    def sql_mobile_nearby_bee_friend_page_list(self, search_content):
        sql = '''SELECT tu.id                                                                       AS 'userId',
       tu.head_img                                                                 AS 'headImg',
       tu.username                                                                 AS 'keeperName',
       tu.phone                                                                    AS 'contactNumber',
       tbf.native_province                                                         AS 'nativeProvince',
       tbf.native_city                                                             AS 'nativeCity',
       tbf.native_county                                                           AS 'nativeCounty',
       tbf.regular_source                                                          AS 'regularSource',
       tbf.age                                                                     AS 'age',
       tbf.seniority                                                               AS 'seniority',
       tmp.label_types                                                             AS 'labelList',
       if(tbf.lat IS NOT NULL, tbf.lat, tsi.lat)                                       AS 'lat',
       if(tbf.lng IS NOT NULL, tbf.lng, tsi.lng)                                       AS 'lng',
       if(tbf.address IS NOT NULL, tbf.address, tsi.address)                           AS 'address',
       if(tbf.location_update_time IS NOT NULL, tbf.location_update_time, tsi.edit_time) AS 'loationUpdateTime',
       if(tbf.province IS NOT NULL, tbf.province, tsi.province) AS 'province',
       if(tbf.city IS NOT NULL, tbf.city, tsi.city) AS 'city',
       if(tbf.county IS NOT NULL, tbf.county, tsi.county) AS 'county'
       this_is_a_tag_str_result_1 
FROM `fc-bee`.t_bee_friend AS tbf
     LEFT JOIN `fc-bee`.t_swarm_info AS tsi ON tbf.user_id = tsi.user_id
    LEFT JOIN `world-user`.t_user AS tu ON tbf.user_id = tu.id
    LEFT JOIN (SELECT user_id, group_concat(label_type) AS 'label_types' FROM `fc-bee`.t_mutual_label this_is_a_tag_str_for_formart_sql GROUP BY user_id) AS tmp ON tmp.user_id = tbf.user_id'''
        if len(search_content) > 1:
            sql += ' WHERE'
            if search_content.get('searchKey', None):
                sql += ' AND tu.username LIKE "%%%s%%" OR tu.phone LIKE "%%%s%%" ' % (search_content.get('searchKey'),
                                                                                      search_content.get('searchKey'))

            if search_content.get('intentions', None):
                sql += ' AND tbf.intention in (%s) ' % ','.join([str(x) for x in search_content.get('intentions')])

            if search_content.get('mutualLabels', None):
                mutual_labels_keys = self.__db.query_data('''SELECT `key` AS db_key
FROM `fc-bee`.t_config
WHERE code = 10006 AND `value` IN %s''' % str(tuple(search_content.get('mutualLabels'))))

                sql_sub = 'WHERE label_type in %s' % str(tuple(x.get('db_key') for x in mutual_labels_keys))
                sql = sql.replace('this_is_a_tag_str_for_formart_sql', sql_sub)
            else:
                sql = sql.replace('this_is_a_tag_str_for_formart_sql', '')

            if search_content.get('searchType', None) == '1':
                sql += ' HAVING province = ' + str(search_content.get('province'))
                sql += ' AND city = ' + str(search_content.get('city'))
                sql += ' AND county = ' + str(search_content.get('county'))

            elif search_content.get('searchType', None) == '2':
                if str(search_content.get('distanceType')) == '1':
                    distance = 5000
                elif str(search_content.get('distanceType')) == '2':
                    distance = 10000
                else:
                    distance = 50000
                sql = sql.replace('this_is_a_tag_str_result_1',
                                  ',st_distance(point(if(tbf.lng IS NOT NULL, tbf.lng, tsi.lng) , if(tbf.lat IS NOT NULL, tbf.lat, tsi.lat)), point(%3.8f, %2.8f)) * 111195 AS distance' % (
                                      search_content.get('lng'), search_content.get('lat')))
                sql += ' HAVING distance <= %s' % distance

            if search_content.get('lng', None):
                sql = sql.replace('this_is_a_tag_str_result_1',
                                  ',st_distance(point(if(tbf.lng IS NOT NULL, tbf.lng, tsi.lng) , if(tbf.lat IS NOT NULL, tbf.lat, tsi.lat)), point(%3.8f, %2.8f)) * 111195 AS distance' % (
                                      search_content.get('lng'), search_content.get('lat')))
                sql += ' ORDER BY distance ASC '
            else:
                sql += ' ORDER BY tu.id DESC '

            if search_content.get('pn', None) is not None:
                sql += " LIMIT %s,20 " % str((search_content.get('pn') - 1) * 20 + 1)

            if sql.endswith("WHERE"):
                sql = sql.replace('WHERE', '')
            sql = sql.replace('this_is_a_tag_str_result_1', '')
            sql = sql.replace(',)', ')')
            sql = sql.replace(', )', ')')
            sql = sql.replace(' WHERE AND ', ' WHERE ')
            sql = sql.replace(' WHERE HAVING ', ' HAVING ')
            sql = sql.replace(' WHERE LIMIT ', ' LIMIT ')
            sql = sql.replace(' WHERE ORDER ', ' ORDER ')

        return self.__db.query_data(sql)

    def sql_mobile_nearby_bee_friend_associate(self, key):
        sql = '''SELECT id AS 'userId',
       username AS 'keeperName',
       phone AS 'contactNumber'
FROM `world-user`.t_user
WHERE  account_type = 21 AND (username LIKE '%{0}%' OR phone LIKE '%{0}%') ORDER BY id DESC ;'''.format(key)
        return self.__db.query_data(sql)

    def sql_mobile_nearby_bee_friend_detail(self, user_id):
        sql = '''
SELECT tu.id                                                                             AS 'userId',
       tu.head_img                                                                       AS 'headImg',
       tu.username                                                                       AS 'keeperName',
       tu.phone                                                                          AS 'contactNumber',
       tu.gender AS 'gender',
       tbf.native_province                                                               AS 'nativeProvince',
       tbf.native_city                                                                   AS 'nativeCity',
       tbf.native_county                                                                 AS 'nativeCounty',
       tbf.regular_source                                                                AS 'regularSourceCode',
       tbf.age                                                                           AS 'age',
       tbf.seniority                                                                     AS 'seniority',
       tbf.id AS 'id',
       tbf.sale_num AS 'saleNum',
       tmp.label_types                                                                   AS 'labelList',
       CASE tu.gender
       WHEN 1 THEN '男'
       WHEN 2 THEN '女'
       END 'genderStr',
       if(tbf.lat IS NOT NULL, tbf.lat, tsi.lat)                                         AS 'lat',
       if(tbf.lng IS NOT NULL, tbf.lng, tsi.lng)                                         AS 'lng',
       if(tbf.address IS NOT NULL, tbf.address, tsi.address)                             AS 'address',
       if(tbf.location_update_time IS NOT NULL, tbf.location_update_time, tsi.edit_time) AS 'locationUpdateTime',
       if(tbf.province IS NOT NULL, tbf.province, tsi.province)                          AS 'province',
       if(tbf.city IS NOT NULL, tbf.city, tsi.city)                                      AS 'city',
       if(tbf.county IS NOT NULL, tbf.county, tsi.county)                                AS 'county'
FROM `fc-bee`.t_bee_friend AS tbf
         LEFT JOIN `fc-bee`.t_swarm_info AS tsi ON tbf.user_id = tsi.user_id
         LEFT JOIN `world-user`.t_user AS tu ON tbf.user_id = tu.id
         LEFT JOIN (SELECT user_id, group_concat(label_type) AS 'label_types' FROM `fc-bee`.t_mutual_label GROUP BY user_id) AS tmp ON tmp.user_id = tbf.user_id
WHERE tu.id = {};'''.format(user_id)
        return self.__db.query_data(sql)

    def sql_mobile_swarm_get_by_user(self, user_id):
        sql = '''SELECT address,
       apiary_name  AS 'apiaryName',
       baby_num     AS 'babyNum',
       breed_place1 AS 'breedPlace1',
       breed_time1  AS 'breedTime1',
       chalkbrood,
       CASE chalkbrood
           WHEN 1 THEN '无'
           WHEN 2 THEN '轻度'
           WHEN 3 THEN '中度'
           WHEN 4 THEN '重度'
           END         'chalkbroodStr',
       city,
       colony,
       CASE colony
           WHEN 1 THEN '弱群'
           WHEN 2 THEN '普通'
           WHEN 3 THEN '强群'
           END         'colonyStr',
       county,
       eke_num      AS 'ekeNum',
       hive_num     AS 'hiveNum',
       honey_num    AS 'honeyNum',
       mite,
       plat_num     AS 'platNum',
       poisoning,
       province,
       queen_num    AS 'queenNum',
       queen_num1   AS 'queenNum1',
       queen_num2   AS 'queenNum2',
       small_num    AS 'smallNum',
       standard_num AS 'standardNum'
FROM `fc-bee`.t_swarm_info
WHERE user_id = {}
  AND is_delete = 0;'''.format(user_id)
        return self.__db.query_data(sql)


class BeeReserveInformationSql(object):
    db = DataBaseOperate()

    def sql_bee_reserve(self):
        sql = '''SELECT * FROM `fc-bee`.t_bee_reserve WHERE is_delete=0; '''
        return self.db.operate(host_ip, sql)

    def sql_bee_reserve_count(self):
        sql = '''SELECT count(1) AS '保护区总数' FROM `fc-bee`.t_bee_reserve WHERE is_delete=0;'''
        return self.db.operate(host_ip, sql)


class StaffSql(object):
    db = DataBaseOperate()

    def sql_staff_number(self):
        sql = '''SELECT # 员工数量
              -- count(1) AS '员工数量'
              tbf.*
              FROM `fc-bee`.t_user_role tur
              LEFT JOIN `fc-bee`.t_bee_friend tbf ON tbf.user_id = tur.user_id
              WHERE tur.role_code IN (1002, 1003, 1004, 1005 ,1006)
              AND tbf.status <> 3
              AND tbf.is_delete = 0
              AND tur.is_delete = 0 GROUP BY user_id;'''
        return self.db.operate(host_ip, sql)

    def sql_bee_friend_own_count(self):
        """
        查询自有养蜂人总数（养蜂技师和养蜂总监）
        :return:
        """
        sql = 'SELECT * FROM `fc-bee`.t_bee_friend tbf ' \
              'WHERE user_id IN (SELECT user_id FROM `fc-bee`.t_user_role tur WHERE tur.role_code IN (1002, 1003) AND tur.is_delete = 0)' \
              ' AND is_delete = 0 AND status IN (1, 2);'
        return self.db.operate(host_ip, sql)

    def sql_bee_friend_own_count_by_area(self, province, city):
        """
        查询指定省市的自有养蜂人
        :param province: 省码
        :param city: 市码
        :return:
        """
        sql = 'SELECT tbf.* FROM `fc-bee`.t_bee_friend tbf ' \
              'WHERE user_id IN (SELECT user_id FROM `fc-bee`.t_user_role tur WHERE tur.role_code IN (1002, 1003) AND tur.is_delete = 0) ' \
              'AND is_delete = 0 AND status IN (1, 2) AND province=%s AND city=%s ' \
              'ORDER BY create_time DESC ;' % (province, city)
        return self.db.operate(host_ip, sql)


class CollectionStatisticsSQL(DataBaseOperate):
    def __init__(self):
        super(CollectionStatisticsSQL, self).__init__()


class NectarSourcePlant(DataBaseOperate):
    def __init__(self):
        super(NectarSourcePlant, self).__init__()

    def query_nectar_source_plant_all(self):
        """
        查询全部蜜源植物信息
        """
        sql = """SELECT tp.id,tp.plant_name AS plantName,tp.code,tp.type,tp.variety,tp.alias,tp.region,tp.area,
                 tp.flowering_description AS floweringDescription,tp.nectar_flow_condition AS nectarFlowCondition,
                 tp.powder_type AS powderType,tp.min_honey_yield AS minHoneyYield,
                 tp.max_honey_yield AS maxHoneyYield,tp.pic_url,tp.code_icon,tp.map_icon,tp.remark
                  FROM `fc-bee`.t_nectar_source_plant tp WHERE tp.is_delete = 0;"""
        return self.operate(host_ip, sql)

    def query_nectar_source_plant_info(self, plantName):
        """
        查询单个蜜源植物信息
        """
        sql = "SELECT *  FROM `fc-bee`.t_nectar_source_plant tp  WHERE tp.plant_name = '%s';" % plantName
        return self.operate(host_ip, sql)

    def query_nectar_source_plant_attach(self, plantCode):
        """
        根据植物code查询植物附件
        """
        sql = """
                SELECT
                    ta.id,
                    ta.plant_code AS plantCode,
                IF
                    ( ta.url IS NULL, '', ta.url ) AS url,
                IF
                    ( ta.remark IS NULL, '', ta.remark ) AS remark,
                IF
                    ( ta.tag IS NULL, '', ta.tag ) AS tag 
                FROM
                    `fc-bee`.t_nectar_source_plant_attach ta 
                WHERE
                    ta.plant_code = '%s'
              """ % plantCode
        return self.operate(host_ip, sql)

    def query_nectar_source_plant_count(self):
        """
        查询蜜源植物统计
        """
        sql = """
                SELECT
                    COUNT(DISTINCT tnsp.id) AS 'allCount',
                    COUNT(DISTINCT IF(tnsp.type = '1',tnsp.id,NULL)) AS 'mainCount',
                    COUNT(DISTINCT IF(tnsp.type = '2',tnsp.id,NULL)) AS 'auxiliaryCount',
                    COUNT(DISTINCT IF((tsi.id IS NOT NULL OR tns.id IS NOT NULL)AND tnsp.type = '2',tnsp.id,NULL)) AS 'coveredAuxiliaryCount',
                    COUNT(DISTINCT IF((tsi.id IS NOT NULL OR tns.id IS NOT NULL)AND tnsp.type = '1' ,tnsp.id,NULL)) AS 'coveredMainCount'
                FROM
                    `fc-bee`.t_nectar_source_plant tnsp
                    LEFT JOIN `fc-bee`.t_swarm_info tsi ON tsi.cur_nectar_type LIKE CONCAT( '%', tnsp.`code`, '%' )	AND tsi.is_delete = 0
                    LEFT JOIN `fc-bee`.t_nectar_source tns ON tns.type LIKE CONCAT( '%', tnsp.`code`, '%' )	AND tns.is_delete = 0
                WHERE
                    tnsp.is_delete = 0;
              """
        return self.operate(host_ip, sql)[0]


class NectarSourcePointSql(object):
    db = DataBaseOperate()

    def query_nectar_source_point(self):
        sql = "SELECT * FROM `fc-bee`.t_nectar_source_point WHERE is_delete=0;"
        return self.db.operate(host_ip, sql)

    def query_nectar_source_point_attach(self):
        sql = """SELECT * FROM `fc-bee`.t_nectar_source_point_attach WHERE is_delete=0;"""
        return self.db.operate(host_ip, sql)

    def query_nectar_source_point_attach_by_point_id(self, point_id):
        sql = """SELECT * FROM `fc-bee`.t_nectar_source_point_attach WHERE point_id=%s AND is_delete =0;""" % point_id
        return self.db.operate(host_ip, sql)


if __name__ == '__main__':
    d = NectarSourcePlant()
    print(d.query_nectar_source_plant_all())
