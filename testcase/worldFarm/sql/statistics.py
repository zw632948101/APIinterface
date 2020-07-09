#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:19
__author__: wei.zhang
__remark__: 统计
"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery


class Statistics(FarmQuery):
    def __init__(self):
        super(Statistics, self).__init__()
        self.level = 'Statistics'

    def query_mobile_statistics_cattle_archive_count(self, farm_id):
        """
        移动端-统计-牲畜档案-牲畜统计 v1.2.4
        :param farm_id: 用户所在农场id
        :return:
        """
        sql = """
        SELECT
            tc.farm_id,
            count( 1 ) AS totalCount,
            if(ear_tag.taggedCount,ear_tag.taggedCount,0) taggedCount ,
            if(et.untaggedCount,et.untaggedCount,0) untaggedCount,
            if(heifer.Heifer,heifer.Heifer,0) heifer,
            if(bull_calves.Bull_calves,bull_calves.Bull_calves,0) bullCalves,
            if(cows.Cows,cows.Cows,0) cows,
            if(bulls.Bulls,bulls.Bulls,0) Bulls,
            if(abn.abnormal_cattles,abn.abnormal_cattles,0) abnormalCattles,
            if(ext.extraneous_cattles,ext.extraneous_cattles,0) extraneousCattles
        FROM
            `world-koala`.t_cattle tc
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS taggedCount FROM `world-koala`.t_cattle WHERE device_id IS NOT NULL AND is_delete = 0 GROUP BY farm_id ) AS ear_tag ON ear_tag.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS untaggedCount FROM `world-koala`.t_cattle WHERE device_id IS NULL AND is_delete = 0 GROUP BY farm_id ) AS et ON et.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Heifer FROM `world-koala`.t_cattle WHERE label_id = 1001 AND is_delete = 0 GROUP BY farm_id ) AS heifer ON heifer.farm_id = tc.farm_id
            LEFT JOIN (
        SELECT
            farm_id,
            COUNT( 1 ) AS Bull_calves 
        FROM
            `world-koala`.t_cattle 
        WHERE
            ( label_id = 1003 OR label_id = 1005 ) 
            AND is_delete = 0 
        GROUP BY
            farm_id 
            ) AS bull_calves ON bull_calves.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Cows FROM `world-koala`.t_cattle WHERE label_id = 1002 AND is_delete = 0 GROUP BY farm_id ) AS cows ON cows.farm_id = tc.farm_id
            LEFT JOIN (
        SELECT
            farm_id,
            COUNT( 1 ) AS Bulls 
        FROM
            `world-koala`.t_cattle 
        WHERE
            ( label_id = 1004 OR label_id = 1006 ) 
            AND is_delete = 0 
        GROUP BY
            farm_id 
            ) AS bulls ON bulls.farm_id = tc.farm_id
            LEFT JOIN (
        SELECT
            farm_id,
            COUNT( 1 ) abnormal_cattles 
        FROM
            `world-shark`.t_device_position 
        WHERE
            farm_id IS NOT NULL 
            AND cattle_id IS NOT NULL 
            AND ( device_status != 1 OR position_farm_id IS NULL ) 
        GROUP BY
            farm_id 
            ) AS abn ON abn.farm_id = tc.farm_id
            LEFT JOIN (
        SELECT
            farm_id,
            COUNT( 1 ) extraneous_cattles 
        FROM
            `world-shark`.t_device_position 
        WHERE
            farm_id IS NOT NULL 
            AND cattle_id IS NOT NULL 
            AND position_farm_id IS NOT NULL 
            AND farm_id != position_farm_id 
        GROUP BY
            farm_id 
            ) AS ext ON ext.farm_id = tc.farm_id 
        WHERE
            tc.is_delete = 0 
            AND tc.farm_id=%s
        GROUP BY
            tc.farm_id
        """ % farm_id
        info = self.operate(self.hostip,  sql)
        return info

    def query_mobile_statistics_home_cattle_count(self, farm_id):
        """
        移动端-统计-首页-牲畜统计
        :param farm_id: 用户所在农场id
        :return:
        """
        sql = """
        SELECT
            tc.farm_id,
            count( 1 ) AS cattles,
            if(ear_tag.Ear_tag,ear_tag.Ear_tag,0) Ear_tag,
            if(bulls.Bulls,bulls.Bulls,0) Bulls,
            if(cows.Cows,cows.Cows,0) Cows,
            if(oxs.Oxs,oxs.Oxs,0) Oxs,
            if(wagyu.Wagyu,wagyu.Wagyu,0) Wagyu,
            if(angus.Angus,angus.Angus,0) Angus,
            if(hereford.Hereford,hereford.Hereford,0) Hereford,
            if(drought_master.Drought_master,drought_master.Drought_master,0) Drought_master,
            if(charolais.Charolais,charolais.Charolais,0) Charolais,
            if(simmental.Simmental,simmental.Simmental,0) Simmental,
            if(brangus.Brangus,brangus.Brangus,0) Brangus,
        IF
            ( abn.abnormal_cattles, abn.abnormal_cattles, 0 ) abnormalCattles,
        IF
            ( ext.extraneous_cattles, ext.extraneous_cattles, 0 ) extraneousCattles 
        FROM
            `world-koala`.t_cattle tc
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Ear_tag FROM `world-koala`.t_cattle WHERE device_id IS NOT NULL AND is_delete = 0 GROUP BY farm_id ) AS ear_tag ON ear_tag.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Bulls FROM `world-koala`.t_cattle WHERE type = 100 AND is_delete = 0 GROUP BY farm_id ) AS bulls ON bulls.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Cows FROM `world-koala`.t_cattle WHERE type = 200 AND is_delete = 0 GROUP BY farm_id ) AS cows ON cows.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Oxs FROM `world-koala`.t_cattle WHERE type = 300 AND is_delete = 0 GROUP BY farm_id ) AS oxs ON oxs.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Wagyu FROM `world-koala`.t_cattle WHERE variety_id = 100 AND is_delete = 0 GROUP BY farm_id ) AS wagyu ON wagyu.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Angus FROM `world-koala`.t_cattle WHERE variety_id = 200 AND is_delete = 0 GROUP BY farm_id ) AS angus ON angus.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Hereford FROM `world-koala`.t_cattle WHERE variety_id = 300 AND is_delete = 0 GROUP BY farm_id ) AS hereford ON hereford.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Drought_master FROM `world-koala`.t_cattle WHERE variety_id = 500 AND is_delete = 0 GROUP BY farm_id ) AS drought_master ON drought_master.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Charolais FROM `world-koala`.t_cattle WHERE variety_id = 600 AND is_delete = 0 GROUP BY farm_id ) AS charolais ON charolais.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Simmental FROM `world-koala`.t_cattle WHERE variety_id = 700 AND is_delete = 0 GROUP BY farm_id ) AS simmental ON simmental.farm_id = tc.farm_id
            LEFT JOIN ( SELECT farm_id, COUNT( 1 ) AS Brangus FROM `world-koala`.t_cattle WHERE variety_id = 800 AND is_delete = 0 GROUP BY farm_id ) AS brangus ON brangus.farm_id = tc.farm_id
            LEFT JOIN (
        SELECT
            farm_id,
            COUNT( 1 ) abnormal_cattles 
        FROM
            `world-shark`.t_device_position 
        WHERE
            farm_id IS NOT NULL 
            AND cattle_id IS NOT NULL 
            AND ( device_status != 1 OR position_farm_id IS NULL ) 
        GROUP BY
            farm_id 
            ) AS abn ON abn.farm_id = tc.farm_id
            LEFT JOIN (
        SELECT
            farm_id,
            COUNT( 1 ) extraneous_cattles 
        FROM
            `world-shark`.t_device_position 
        WHERE
            farm_id IS NOT NULL 
            AND cattle_id IS NOT NULL 
            AND position_farm_id IS NOT NULL 
            AND farm_id != position_farm_id 
        GROUP BY
            farm_id 
            ) AS ext ON ext.farm_id = tc.farm_id 
        WHERE
            tc.is_delete = 0 
            AND tc.farm_id = %s 
        GROUP BY
            tc.farm_id
                """ % farm_id
        info = self.operate(self.hostip,  sql)
        return info

    def query_statistics_cattle_abnormal(self, farmid=None, devicetype=''):
        """
        查询活动异常牲畜列表
        V1.2.5 修改
        :return:
        """
        if farmid is not None:
            farmid = "AND tdp.farm_id = %s " % farmid
        else:
            farmid = "AND tdp.farm_id IS NOT NULL"
        if devicetype != '':
            devicetype = "AND tdp.device_type in('1','2')"

        sql = """
            SELECT
                tdp.farm_id,tdp.device_eui,tc.birth_date,tc.ear_tag_id,tdp.device_type,tdp.lat,tdp.lng,tdp.position_farm_id,tdp.position_region_id,tdp.region_id
            FROM
                `world-shark`.t_device_position tdp
                LEFT JOIN `world-shark`.t_sync_device_bind ts ON tdp.device_eui = ts.device_eui 
                LEFT JOIN  `world-koala`.t_cattle tc ON tdp.device_eui = tc.device_id
            WHERE
                ts.is_delete = '0' 
                %s 
                %s
                AND ( tdp.device_status != 1 OR tdp.position_farm_id IS NULL OR tdp.position_farm_id != tdp.farm_id )
                ORDER BY tdp.position_time DESC;
        """ % (farmid, devicetype)
        info = self.operate(self.hostip,  sql)
        if info == ():
            return
        return info

    def query_statistics_cattle_intrude(self, farm_id=None, devicetype=None, positionStatus=None, deviceeui=None):
        """
        查询异常牲畜
        :return:
        """
        if positionStatus is not None:
            positionStatus = 'AND tdp.farm_id = tdp.position_farm_id AND tdp.device_status = %s' % positionStatus
        else:
            positionStatus = "AND (tdp.farm_id != tdp.position_farm_id or tdp.position_farm_id is null)"
        if devicetype is not None and devicetype != 3:
            positionStatus += " AND tdp.device_type = %s " % devicetype
        elif devicetype == 3:
            positionStatus += " AND tdp.device_type != %s " % devicetype
        if deviceeui:
            positionStatus += "AND ( tdp.device_eui = '%s' OR tdp.channel_device_eui = '%s' )" % (deviceeui, deviceeui)

        sql = """
                SELECT
                    tdp.farm_id, 
                    tdp.device_eui,
                    tc.birth_date,
                    tc.cattle_name,
                    CASE tc.sex WHEN 100 THEN '公牛' WHEN 200 THEN '母牛' WHEN 300 THEN '阉牛' END AS sex ,
                    CASE tc.type WHEN 1001 THEN '幼母牛' WHEN 1002 THEN '成年母牛' WHEN 1003 THEN '幼公牛' WHEN 1004 THEN '成年公牛' WHEN 1005 THEN '阉割幼牛' WHEN 1006 THEN '阉牛' WHEN 1007 THEN '种母牛' WHEN 1008 THEN '种公牛' END AS label_id,
                    CASE tc.`variety_id` WHEN 100 THEN '和牛' WHEN 200 THEN '安格斯牛' WHEN 300 THEN '海福特' WHEN 400 THEN '圣卡初塔斯' WHEN 500 THEN '抗旱王' WHEN 600 THEN '夏洛莱' WHEN 700 THEN '西门塔尔' WHEN 800 THEN '婆罗门' WHEN 820 THEN '黄牛' WHEN 900 THEN '其他' END AS variety_id,
                    tdp.device_type,
                    tdp.lat,
                    tdp.lng,
                    tdp.position_farm_id,
                    tdp.position_region_id,
                    tdp.region_id 
                FROM
                    `world-shark`.t_device_position tdp
                    LEFT JOIN `world-koala`.t_cattle tc ON tdp.device_eui = tc.device_id 
                WHERE
                    tdp.farm_id = '%s'
                    %s
                ORDER BY
                    tdp.position_time DESC;
                """ % (farm_id, positionStatus)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_cattle_location_map_info(self, farmid, type=None, stage=None):
        """
        查询分组地图牲畜列表
        :param farmid:
        :param type:
        :param stage:
        :return:
        """
        if type:
            type = "AND tc.type in(%s)" % type
            stage = ''
        else:
            type = ''
            stage = "AND tc.stage_status in(%s)" % stage

        sql = """
            SELECT
                tc.id as cattleId,
                tc.cattle_name as cattleName,
                tc.birth_date as birthDate,
                CASE tc.type WHEN 1001 THEN '幼母牛' WHEN 1002 THEN '成年母牛' WHEN 1003 THEN '幼公牛' WHEN 1004 THEN '成年公牛' WHEN 1005 THEN '阉割幼牛' WHEN 1006 THEN '阉牛' WHEN 1007 THEN '种母牛' WHEN 1008 THEN '种公牛' END AS typeName,
                CASE tc.`variety_id` WHEN 100 THEN '和牛' WHEN 200 THEN '安格斯牛' WHEN 300 THEN '海福特' WHEN 400 THEN '圣卡初塔斯' WHEN 500 THEN '抗旱王' WHEN 600 THEN '夏洛莱' WHEN 700 THEN '西门塔尔' WHEN 800 THEN '婆罗门' END AS varietyName,
                tc.type,
                tc.`variety_id` as varietyId,
                tdp.device_eui as eui,
                tdp.lat,
                tdp.lng	
            FROM
                `world-shark`.t_device_position tdp
                LEFT JOIN `world-koala`.t_cattle tc ON tdp.cattle_id = tc.id
                LEFT JOIN `world-shark`.t_sync_device_bind ts ON tdp.cattle_id = ts.cattle_id 
            WHERE
                tc.farm_id = '%s'
                AND ts.is_delete = '0'
                %s
                %s
            """ % (farmid, type, stage)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_list_statistics_number(self, farmid):
        """
        查询牲畜管理列表统计数量
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                tc.farm_id,
                count( tc.id ) cattle_num,
                IFNULL( sum( CASE WHEN tc.type IN ( '1003', '1005' ) THEN 1 END ), 0 ) AS '幼公牛',
                IFNULL( sum( CASE WHEN tc.type = '1001' THEN 1 END ), 0 ) AS '幼母牛',
                IFNULL( sum( CASE WHEN tc.type IN ( '1004', '1006','1008' ) THEN 1 END ), 0 ) AS '成年公牛',
                IFNULL( sum( CASE WHEN tc.type in ('1002','1007') THEN 1 END ), 0 ) AS '成年母牛',
                IFNULL( sum( CASE WHEN tc.stage_status = '10' AND tc.type in('1001','1003', '1005') THEN 1 END ), 0 ) AS '未断奶牲畜',
                IFNULL( sum( CASE WHEN tc.stage_status IN ( '30', '33', '32', '31' ) AND tc.type in('1002','1007') THEN 1 END ), 0 ) AS '待交配牲畜',
                IFNULL( sum( CASE WHEN tc.stage_status = '40' AND tc.type in('1002','1007') THEN 1 END ), 0 ) AS '已交配牲畜',
                IFNULL( sum( CASE WHEN tc.stage_status = '50' AND tc.type in('1002','1007') THEN 1 END ), 0 ) AS '已怀孕牲畜',
                IFNULL( sum( CASE WHEN tc.device_id IS NOT NULL AND tc.device_id != '' THEN 1 END ), 0 ) AS taggedCount,
                IFNULL( sum( CASE WHEN tc.device_id IS NULL OR tc.device_id = '' THEN 1 END ), 0 ) AS totalCount 
            FROM
                `world-koala`.t_cattle tc
            WHERE
                tc.is_delete = '0' 
                AND tc.farm_id = '%s'
            GROUP BY
                tc.farm_id 
            ORDER BY
                tc.farm_id DESC;
                """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def qyery_statistics_abnormal(self, farmid):
        """
        查询走出农场和活动异常的牲畜
        :param farmid:
        :return:
        """
        sql = """
                SELECT
                    IFNULL(tdp.farm_id,'%s') as farm_id,
                    IFNULL(SUM(CASE WHEN tdp.device_status != 1 AND tdp.farm_id = tdp.position_farm_id THEN 1	END),0) as '未上报定位牲畜',
                    IFNULL(SUM(CASE WHEN tdp.farm_id != tdp.position_farm_id OR tdp.position_farm_id is NULL THEN 1	END),0) as '走出农场牲畜'
                FROM
                    `world-shark`.t_device_position tdp 
                WHERE
                    tdp.farm_id = '%s';
              """ % (farmid, farmid)
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_statistics_group_detail(self, farmid, cattle_tyle, cattle_stagge):
        """
        查询分组统计
        :param farmid:
        :param cattle_tyle:
        :param cattle_stagge:
        :return:
        """
        if cattle_tyle:
            cattle_tyle = "AND tc.type in(%s)" % cattle_tyle
            cattle_stagge = ''
        else:
            cattle_tyle = ''
            cattle_stagge = "and tc.stage_status in(%s)" % cattle_stagge
        sql = """
                SELECT
                    tc.farm_id,
                    count( tc.id ) cattle_num,
                    IFNULL(sum( CASE WHEN tc.device_id IS NOT NULL AND tc.device_id != '' THEN 1 END ),0) AS tagged_num,
                    IFNULL(sum( CASE WHEN tc.device_id IS NULL OR tc.device_id = '' THEN 1 END ),0) AS untagged_num 
                FROM
                    `world-koala`.t_cattle tc
                WHERE
                    tc.is_delete = '0' 
                    AND tc.farm_id = '%s'
                    %s%s
                GROUP BY
                    tc.farm_id 
                ORDER BY
                    tc.farm_id DESC;                
              """ % (farmid, cattle_tyle, cattle_stagge)
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return
