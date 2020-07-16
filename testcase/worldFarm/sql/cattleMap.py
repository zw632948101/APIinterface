#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:16
__author__: wei.zhang
__remark__: 牲畜地图
"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery


class CattleMap(FarmQuery):
    def __init__(self):
        super(CattleMap, self).__init__()
        self.level = 'CattleMap'

    def query_cattle_info(self, farmid):
        """
        查询牲畜详情
        :return:
        """
        sql = """
            SELECT * FROM `world-koala`.t_cattle tc WHERE tc.device_id is not null AND tc.device_id != '' AND tc.is_delete = '0' AND tc.farm_id = '%s';
            """ % farmid
        info = self.operate(self.hostip,  sql)
        if info == ():
            return
        return info

    def query_near_cattle_list(self):
        """
        查询附近牲畜列表
        :return:
        """
        sql = """SELECT * FROM (SELECT tc.id cattle_id ,tc.farm_id,tc.birth_date,tc.cattle_name,tf.`value` variety_id,
        tc.device_id FROM `world-koala`.t_cattle tc LEFT JOIN `world-koala`.t_config tf ON tc.variety_id = tf.`key`
         WHERE tc.is_delete = '0' AND tc.device_id IS NOT NULL AND tf.`code` ='10003'
          AND tc.device_type = 1 ORDER BY tc.id DESC) AS tcf 
          LEFT JOIN (SELECT tc1.id,tf.`value` type  FROM `world-koala`.t_cattle tc1 
          LEFT JOIN `world-koala`.t_config tf ON tc1.sex = tf.`key` WHERE tf.`code` ='10002') AS tcf1 
          ON tcf.cattle_id = tcf1.id WHERE tcf.device_id in(SELECT tdp1.device_eui 
          FROM `world-shark`.t_device_position tdp1 WHERE tdp1.channel_device_eui = (SELECT tdp.device_eui 
          FROM `world-shark`.t_device_position tdp WHERE tdp.device_type = '2' AND tdp.farm_id IS NOT NULL 
          ORDER BY tdp.position_time DESC LIMIT 1) OR tdp1.device_eui = (SELECT tdp.device_eui 
          FROM `world-shark`.t_device_position tdp WHERE tdp.device_type = '2' AND tdp.farm_id IS NOT NULL 
          ORDER BY tdp.position_time DESC LIMIT 1));"""
        info = self.operate(self.hostip,  sql)
        if info == ():
            return
        return info

    def query_region_cattle_list(self):
        """
        查询围栏内牲畜列表以及定位信息
        :return:
        """
        sql = """
         SELECT * FROM (SELECT tc.id cattle_id ,tc.farm_id,tc.birth_date,tc.ear_tag_id,tf.`value` variety_id,
         tc.device_id,tc.region_id FROM `world-koala`.t_cattle tc LEFT JOIN `world-koala`.t_config tf 
         ON tc.variety_id = tf.`key` WHERE tc.is_delete = '0' AND tc.device_id IS NOT NULL AND tf.`code` ='10003'
          AND tc.device_type = 1 ORDER BY tc.id DESC) AS tcf LEFT JOIN (SELECT tc1.id,tf.`value` type  
          FROM `world-koala`.t_cattle tc1 LEFT JOIN `world-koala`.t_config tf ON tc1.type = tf.`key` 
          WHERE tf.`code` ='10002') AS tcf1 ON tcf.cattle_id = tcf1.id LEFT JOIN (SELECT farm_id,region_id 
          FROM `world-shark`.t_device_position WHERE farm_id IS NOT NULL GROUP BY farm_id ORDER BY farm_id 
          DESC ) as tdp ON tcf.farm_id = tdp.farm_id WHERE tcf.farm_id = tdp.farm_id 
          AND tcf.region_id = tdp.region_id;
         """
        info = self.operate(self.hostip,  sql)
        if info == ():
            return
        return info

    def query_cattle_trace(self, group=None):
        """
        查询牲畜轨迹
        :return:
        """
        group = "GROUP BY tdpr.device_eui" if group else ''
        sql = """
        SELECT tdpr.device_eui,tdpr.lat,tdpr.lng,tdpr.position_time,tdp.farm_id 
        FROM `world-shark`.t_device_position_record tdpr 
        LEFT JOIN (SELECT farm_id,region_id,device_eui 
        FROM `world-shark`.t_device_position WHERE farm_id IS NOT NULL 
        GROUP BY farm_id ORDER BY farm_id DESC)AS tdp 
        ON tdpr.device_eui = tdp.device_eui WHERE tdpr.device_eui = tdp.device_eui 
        AND tdpr.lat IS NOT NULL AND tdpr.position_time IS NOT NULL %s;
        """ % group
        info = self.operate(self.hostip,  sql)
        if info == ():
            return
        return info

    def query_default_farm_cattle_info_list(self, email, devicetype=None):
        """
        查询当前农场的所有绑定设备的牲畜
        :param farmid:
        :param devicetype:
        :return:
        """

        devicetype = "AND tc.device_type in(%s)" % devicetype if devicetype else ''

        sql = """
                SELECT
                    tc.id,
                    tc.device_id,
                    tc.farm_id,
                    tc.region_id
                FROM
                    `world-koala`.t_cattle tc
                    LEFT JOIN `world-shark`.t_sync_device_bind ts ON tc.id = ts.cattle_id 
                    LEFT JOIN `agr-ant`.t_device td ON tc.device_id = td.device_eui
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tc.farm_id = tfu.farm_id
                    LEFT JOIN `world-user`.t_user tu ON tu.id = tfu.user_id
                WHERE
                    tu.email = '%s'
                    AND tc.is_delete = '0' 
                    AND ts.is_delete = '0'
                    AND td.device_eui is not NULL
                    %s
              """ % (email, devicetype)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_map_heat(self, farmid, endtime, starttime, num=None):
        """
        查询热力图定位点
        :param farmid:
        :return:
        """
        num = "GROUP BY tr.device_eui" if num is not None else ""
        sql = """
                SELECT
                    tr.lat,
                    tr.lng
                FROM
                    `world-shark`.t_device_position_record tr 
                WHERE
                    tr.farm_id = '%s' 
                    AND tr.position_time >= '%s' 
                    AND tr.position_time <= '%s'
                    %s;
              """ % (farmid, starttime, endtime, num)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_may_device_update(self, email):
        """
        查询已加入农场的所有信号中继设备
        :param farmid:
        :return:
        """
        sql = """
                SELECT
                    tdp.device_eui,
                    tdp.farm_id
                FROM
                    `world-shark`.t_sync_device_bind tdp
                    LEFT JOIN `world-koala`.t_farm_user tf ON tdp.farm_id = tf.farm_id
                    LEFT JOIN `world-user`.t_user tu ON tf.user_id = tu.id 
                    LEFT JOIN `agr-ant`.t_device td ON tdp.device_eui = td.device_eui
                WHERE
                    tu.email = '%s' 
                    AND tf.is_delete = '0' 
                    AND tdp.cattle_id IS NULL
                    AND td.product_type = '耳标/LoRa耳标'
                    AND tdp.is_delete = '0';
              """ % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_device_remark(self, farmid, deviceno):
        """
        查询修改的信号中继
        :param farmid:
        :param deviceno:
        :return:
        """
        sql = """
                SELECT
                    * 
                FROM
                    `world-koala`.t_device_remark tr 
                WHERE
                    tr.farm_id = '%s' 
                    AND tr.device_no = '%s' 
                    AND tr.is_delete = '0'
              """ % (farmid, deviceno)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_bind_device_id(self, farmid, deviceid):
        """
        查询绑定的信号中继
        :param farmid:
        :param deviceid:
        :return:
        """
        sql = """
                SELECT
                    * 
                FROM
                    `world-shark`.t_sync_device_bind ts 
                WHERE
                    ts.farm_id = '%s' 
                    AND ts.device_eui = '%s' 
                    AND ts.is_delete = 0;
              """ % (farmid, deviceid)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_region_cattle_info_list(self, farmid, regionid, activeStatus=None, device_type=None,
                                           isBindDevice=None, cattle_name=None, vision_num=None):
        """
        查询围栏牲畜列表
        :param farmid: 农场ID
        :param regionid: 围栏ID
        :param activeStatus: 活动状态 1 活动正常  2 活动异常
        :param device_type: 绑定设备类型 1，2lora耳标，3蓝牙子耳标
        :param isBindDevice: 绑定设备状态 1已绑定 0 未绑定
        :param cattle_name: 牲畜名称全匹配搜索
        :param vision_num: 牲畜名称和视觉编码全匹配搜索
        :return:
        """
        activeStatus = "AND t.activeStatus in(%s)\n" % activeStatus if activeStatus else ''
        devicetype = "AND t.deviceType in(%s)\n" % device_type if device_type else ''
        isBindDevice = "AND t.isBindDevice in(%s)\n" % isBindDevice if isBindDevice else ''
        cattlename = "AND t.cattleName LIKE '%%s%\n'" % cattle_name if cattle_name else ''
        visionnum = "AND (t.cattleName LIKE '%%s%' OR t.visionNum LIKE '%%s%')\n" % vision_num if vision_num else ''
        sqlstr = activeStatus + devicetype + isBindDevice + cattlename + visionnum
        sql = """
                SELECT * FROM (SELECT
                    CASE tc.sex WHEN 100 THEN '公牛' WHEN 200 THEN '母牛' WHEN 300 THEN '阉牛' END AS sexName ,
                    CASE tc.type WHEN 1001 THEN '幼母牛' WHEN 1002 THEN '成年母牛' WHEN 1003 THEN '幼公牛' WHEN 1004 THEN '成年公牛' WHEN 1005 THEN '阉割幼牛' WHEN 1006 THEN '阉牛' WHEN 1007 THEN '种母牛' WHEN 1008 THEN '种公牛' END AS typeName,
                    CASE tc.`variety_id` WHEN 100 THEN '和牛' WHEN 200 THEN '安格斯牛' WHEN 300 THEN '海福特' WHEN 400 THEN '圣卡初塔斯' WHEN 500 THEN '抗旱王' WHEN 600 THEN '夏洛莱' WHEN 700 THEN '西门塔尔' WHEN 800 THEN '婆罗门' WHEN 900 THEN '其他' END AS varietyName,
                    CASE WHEN tp.device_eui IS NOT NULL THEN 1 WHEN tp.device_eui IS NULL THEN 0 END AS isBindDevice,
                    CASE WHEN tp.device_status = 4 OR tp.farm_id != tp.position_farm_id THEN 2 WHEN tp.device_status = 1 THEN 1 END AS activeStatus,
                    CASE WHEN tp.device_status = 4 OR tp.farm_id != tp.position_farm_id THEN '活动异常' WHEN tp.device_status = 1 THEN '活动正常' END AS activeStatusName,
                    CASE WHEN tp.device_status = 4 AND tp.farm_id = tp.position_farm_id THEN '原因：不在农场信号范围内' WHEN tp.farm_id != tp.position_farm_id OR tp.position_farm_id IS NULL THEN '原因：走出农场' END description,
                    CASE WHEN tp.device_status = 4 AND tp.farm_id = tp.position_farm_id THEN 5 WHEN tp.farm_id != tp.position_farm_id OR tp.position_farm_id IS NULL THEN 3 END positionType,
                    tc.sex,
                    tc.type,
                    tc.region_id,
                    tc.farm_id,
                    tc.variety_id as varietyId,
                    tc.vision_num as visionNum,
                    tc.id as 'id',
                    tc.cattle_name as cattleName,
                    tc.device_type as deviceType,
                    tp.device_eui as deviceId,
                    UNIX_TIMESTAMP(tc.birth_date) * 1000 AS birthDate,
                    UNIX_TIMESTAMP(tp.position_time) * 1000 AS positionTime
                FROM
                    `world-koala`.t_cattle tc 
                    LEFT JOIN `world-shark`.t_device_position tp ON tc.id = tp.cattle_id
                WHERE
                     tc.is_delete = '0' ) as t
                WHERE t.farm_id = '%s'
                AND t.region_id = '%s'
                %s
             """ % (farmid, regionid, sqlstr)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_is_position(self, farmid):
        """
        当前农场内有定位数据的设备
        :param farmid:
        :return:
        """
        sql = """
            SELECT * FROM `world-shark`.t_device_position tdp WHERE tdp.farm_id = '%s' AND tdp.cattle_id IS NOT NULL;
             """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_histry_position(self, device_id):
        """
        查询设备历史定位记录
        :param device_id:
        :return:
        """
        sql = """
                SELECT
                    tdpr1.device_eui AS deviceEui,
                    tdpr1.electricity AS electricity,
                    tdpr1.lat,
                    tdpr1.lng,
                    UNIX_TIMESTAMP(tdpr1.position_time)*1000 AS positionTime   
                FROM
                    `world-shark`.t_device_position_record tdpr1
                WHERE
                    tdpr1.device_eui = '%s' 
                    AND tdpr1.position_time IS NOT NULL 
                    AND tdpr1.lat IS NOT NULL
                    AND tdpr1.is_take = 0
                    AND tdpr1.position_time >= 	(SELECT DATE_SUB((SELECT position_time FROM `world-shark`.t_device_position_record WHERE device_eui = '%s' AND farm_id IS NOT NULL ORDER BY id DESC LIMIT 1),INTERVAL 3 DAY))
                    AND tdpr1.cattle_id = (SELECT tdp.cattle_id FROM `world-shark`.t_device_position tdp WHERE tdp.device_eui = '%s')
                    AND tdpr1.id > IFNULL((SELECT tdpr.id FROM `world-shark`.t_device_position_record tdpr WHERE tdpr.device_eui = '%s' AND tdpr.farm_id IS NULL GROUP BY tdpr.id DESC LIMIT 1 ),0 );
              """ % (device_id, device_id, device_id, device_id)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_device_bind_signal_relay(self, farmid):
        """
        根据农场id查询信号中继设备
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-shark`.t_sync_device_bind ts 
            WHERE
                ts.farm_id = %s
                AND ts.is_delete = 0
                AND ts.cattle_id IS NULL
                ORDER BY ts.id DESC;
              """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return
