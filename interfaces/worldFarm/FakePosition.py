# encoding: utf-8
import datetime
import random
import time

from tools.Request import Request

import json


class FakePosition(object):

    def __init__(self, evn):
        self.log = Log('Koala')
        self.request = Request()
        url_dict = {'WORLD_QA': 'http://qa-shark.worldfarm.com', 'WORLD_PROD': 'http://shark.worldfarm.com',
                    'WORLD_DEV': 'http://dev-shark.worldfarm.com'}
        self.url = url_dict.get(evn)

    def trans_position(self, deviceEui, lat, lng, deviceType, currentFrequency, positionUniqueNo, isTake,
                       channelType=None, channelDeviceEui=None, distance=None, hdop=None, positionTime=None,
                       uploadTime=None):
        """
        设备转场
        :param deviceEui: 设备ID
        :param lat: 维度
        :param lng: 经度
        :param deviceType: 耳标类型  1lora耳标  2蓝牙耳标 3蓝牙子耳标
        :param currentFrequency:  当前上传频率 单位:分钟
        :param positionUniqueNo:  定位唯一编号(确保不相同)
        :param isTake:  是否为携带数据(0不是, 1是) 携带数据不更新定位表,只新增定位记录表
        :param channelType:   数据传输渠道设备类型  1通过母耳标上传  2通过网关上传 注 子耳标才有
        :param channelDeviceEui: 数据传输渠道设备编号(信号放大器),子耳标才有值
        :param distance:  子耳标到传输渠道设备的距离(m),子耳标才有值
        :param hdop:  精度因子
        :param positionTime: 定位时间(有可能为空),时间戳
        :param uploadTime:  数据上传时间,时间戳
        :return:
        """
        if uploadTime is None:
            uploadTime = str(time.time() * 1000).split('.')[0]
        if positionTime is None:
            positionTime = str(time.time() * 1000).split('.')[0]
        data = {'deviceEui': deviceEui, 'lat': lat, 'lng': lng, 'hdop': hdop, 'deviceType': deviceType,
                'currentFrequency': currentFrequency, 'positionUniqueNo': positionUniqueNo, 'isTake': isTake,
                'channelType': channelType, 'channelDeviceEui': channelDeviceEui, 'distance': distance,
                'positionTime': positionTime, 'uploadTime': uploadTime}
        response = self.request.post(url=self.url + '/test/device-position/mock-position', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")


class Transitions(FakePosition):
    def __init__(self, env):
        super(Transitions, self).__init__(env)

    def __bubbling__(self, coordinate):
        """
        冒泡排序由小到大  废弃
        :param coordinate:
        :return:
        """
        n = len(coordinate)
        for i in range(n):
            for j in range(0, n - i - 1):
                if coordinate[j] < coordinate[j + 1]:
                    coordinate[j], coordinate[j + 1] = coordinate[j + 1], coordinate[j]
        return coordinate

    def __dispose_data__(self, coordinatelist):
        """
        拆分定位集数据,通过遍历后取第一个和最后一个值返回
        :param coordinatelist:
        :return:
        """
        lng_list = []
        lat_list = []
        for i in coordinatelist:
            lng_list.append(i.get('lng'))
            lat_list.append(i.get('lat'))
        lng = [min(lng_list), max(lng_list)]
        lat = [min(lat_list), max(lat_list)]
        return lng, lat

    def all_case(self, coordinatelist):
        print(self.__dispose_data__(coordinatelist))

    def create_transitions(self, coordinate_outer, coordinate_within=None):
        """
        生成一个随机定位点,
        coordinate_outer 传参只会生成内圈的随机点
        coordinate_within 不为空时,生成大于内圈小于外圈的随机点
        :list coordinate_outer:生成随机点的内圈
        :list coordinate_within:生成随机点的外圈
        :return:
        """
        lng_lo, lat_lo = self.__dispose_data__(coordinate_outer)
        if coordinate_within is None:
            lng = random.uniform(lng_lo[0], lng_lo[1])
            lat = random.uniform(lat_lo[0], lat_lo[1])
            return lng, lat

        lng_lw, lat_lw = self.__dispose_data__(coordinate_within)
        lat = lng = 0
        while True:
            if lng == 0:
                lng = random.uniform(lng_lo[0], lng_lo[1])
            if lat == 0:
                lat = random.uniform(lat_lo[0], lat_lo[1])
            if not (lng_lw[0] < lng < lng_lw[1]):
                lng = 0
            if not (lat_lw[0] < lat < lat_lw[1]):
                lat = 0
            if (lng_lw[0] < lng < lng_lw[1]) and (lat_lw[0] < lat < lat_lw[1]):
                break
        return lng, lat

    def transitions(self, lat, lng, deviceEui: str = ..., deviceType: int = ...,
                    historical_time=None, channelDeviceEui=None, minutes=None, channelType=1):
        """
        手动转场
        :param deviceEui:  设备ID
        :param deviceType: 设备型号  1lora耳标 2蓝牙母耳标 3蓝牙子耳标
        :param lat:
        :param lng:
        :param historical_time:  历史时间,单位小时 int
        :param channelDeviceEui: 关联母耳标ID (子耳标特有)
        :param minutes: 历史时间,单位分 int
        :return:
        """
        if historical_time is not None and minutes is not None:
            untime = datetime.datetime.now() - datetime.timedelta(hours=historical_time, minutes=minutes)
            positionTime = uploadTime = str(untime.timestamp() * 1000).split('.')[0]
        elif historical_time is not None:
            untime = datetime.datetime.now() - datetime.timedelta(hours=historical_time)
            positionTime = uploadTime = str(untime.timestamp() * 1000).split('.')[0]
        else:
            positionTime = uploadTime = None

        positionUniqueNo = str(time.time() * 1000).split('.')[0]

        if deviceType == 3:
            self.trans_position(deviceEui=deviceEui, deviceType=deviceType, lng=lng,
                                lat=lat, currentFrequency=40, positionUniqueNo=positionUniqueNo,
                                isTake=0, channelType=channelType, channelDeviceEui=channelDeviceEui,
                                distance=random.randint(10, 40),
                                positionTime=positionTime, uploadTime=uploadTime, hdop=10)
        elif deviceType == 1:
            self.trans_position(deviceEui=deviceEui, deviceType=deviceType, lng=lng, lat=lat,
                                currentFrequency=40, positionUniqueNo=positionUniqueNo,
                                isTake=0, positionTime=positionTime, uploadTime=uploadTime, hdop=10)
        elif deviceType == 2:
            self.trans_position(deviceEui=deviceEui, deviceType=deviceType, lng=lng, lat=lat,
                                currentFrequency=40, positionUniqueNo=positionUniqueNo,
                                isTake=0, positionTime=positionTime, uploadTime=uploadTime, hdop=10)
            self.trans_position(deviceEui=deviceEui, deviceType=deviceType, lng=lng, lat=lat,
                                currentFrequency=40, positionUniqueNo=positionUniqueNo,
                                isTake=1, positionTime=positionTime, uploadTime=uploadTime, hdop=10)

    def transitions_bluetooth(self, lat: float = ..., lng: float = ..., deviceEui: str = ...,
                              bluetooth_list=None, historical_time=None, minutes=None):
        """
        手动转场,单个蓝牙母耳标携带多个子耳标,也可单个蓝牙母耳标转场
        :float lat:
        :float lng:
        :str deviceEui: 母耳标编号
        :int minutes: 历史时间,单位分
        :int historical_time: 历史时间单位 小时
        :list bluetooth_list: 子耳标列表
        :return:
        """
        # self.log.logger.info(msg=''datetime.datetime.time().fold())
        if len(deviceEui) < 16:
            self.log.logger.warning('编号:"%s" 不符合规则' % deviceEui)
            return
        self.transitions(deviceEui=deviceEui, deviceType=2, lat=lat, lng=lng,
                         historical_time=historical_time, minutes=minutes)
        if bluetooth_list is not None:
            for x in bluetooth_list:
                self.transitions(deviceEui=x, deviceType=3, lat=lat, lng=lng, historical_time=historical_time,
                                 channelDeviceEui=deviceEui, minutes=minutes)

    def transitions_lora_baseStation(self, lat: float = ..., lng: float = ..., deviceEui: str = ...,
                                     bluetooth_list=None, historical_time=None, minutes=None):
        """
        手动转场,单个蓝牙母耳标携带多个子耳标,也可单个蓝牙母耳标转场
        :float lat:
        :float lng:
        :str deviceEui: 母耳标编号
        :int minutes: 历史时间,单位分
        :int historical_time: 历史时间单位 小时
        :list bluetooth_list: 子耳标列表
        :return:
        """
        for x in bluetooth_list:
            self.transitions(deviceEui=x, deviceType=2, lat=lat, lng=lng, historical_time=historical_time,
                             channelDeviceEui=deviceEui, minutes=minutes, channelType=2)

    def transitions_bluetooth_baseStation(self, lat: float = ..., lng: float = ..., deviceEui: str = ...,
                                          bluetooth_list=None, historical_time=None, minutes=None):
        """
        手动转场,单个蓝牙母耳标携带多个子耳标,也可单个蓝牙母耳标转场
        :float lat:
        :float lng:
        :str deviceEui: 母耳标编号
        :int minutes: 历史时间,单位分
        :int historical_time: 历史时间单位 小时
        :list bluetooth_list: 子耳标列表
        :return:
        """
        for x in bluetooth_list:
            self.transitions(deviceEui=x, deviceType=3, lat=lat, lng=lng, historical_time=historical_time,
                             channelDeviceEui=deviceEui, minutes=minutes, channelType=2)

    def transitions_lora(self, lat: float = ..., lng: float = ..., deviceEui: str = ...,
                         historical_time=None, minutes=None):
        """
        手动转场,单个lora耳标,
        :float lat:
        :float lng:
        :str deviceEui: lora耳标
        :int minutes: 历史时间,单位分
        :int historical_time: 历史时间单位 小时
        :return:
        """
        if len(deviceEui) < 16:
            self.log.logger.warning('编号:"%s" 不符合规则' % deviceEui)
            return
        self.transitions(deviceEui=deviceEui, deviceType=1, lat=lat, lng=lng,
                         historical_time=historical_time, minutes=minutes)

    def crazy_transitions_bluetooth(self, coordinatelist: list = ..., deviceEui: str = ..., historical_time=None,
                                    number=20, bluetooth_list=None, minutes=None, coordinate_within=None):
        """
        随机定位一个范围内,默认随机二十次,适用于在农场内圈生成牲畜轨迹,该方法适用于蓝牙子母耳标
        :list coordinatelist:坐标集列表
        :str deviceEui:设备编号
        :int bluetooth_list:蓝牙子耳标列表
        :int historical_time:生成历史时间定位,单位小时 int
        :int number: 循环次数
        :int minutes: 生成历史时间定位,单位分 int
        :return: None
        """
        for i in range(number):
            if coordinate_within is None:
                lng, lat = self.create_transitions(coordinatelist)
            elif coordinate_within is not None:
                lng, lat = self.create_transitions(coordinatelist, coordinate_within)
            self.transitions_bluetooth(lat=lat, lng=lng, deviceEui=deviceEui, bluetooth_list=bluetooth_list,
                                       historical_time=historical_time, minutes=minutes)

    def crazy_transitions_lora(self, coordinatelist: list = ..., deviceEui: str = ..., historical_time=None,
                               number=20, minutes=None, coordinate_within=None):
        """
        随机定位一个范围内,默认随机二十次,该方法适用于lora耳标
        :list coordinatelist:坐标集列表
        :str deviceEui:设备编号
        :int historical_time:生成历史时间定位,单位小时 int
        :int number: 循环次数
        :int minutes: 生成历史时间定位,单位分 int
        :return: None
        """
        for i in range(number):
            if coordinate_within is None:
                lng, lat = self.create_transitions(coordinatelist)
            if coordinate_within is not None:
                lng, lat = self.create_transitions(coordinatelist, coordinate_within)
            self.transitions_lora(lat=lat, lng=lng, deviceEui=deviceEui, minutes=minutes,
                                  historical_time=historical_time)

    def much_transitions_bluetooth(self, coordinatelist: list = ..., lora_list: list = ..., historical_time=None,
                                   number=1, bluetooth_list=None, minutes=None, coordinate_within=None):
        """
        批量转场母耳标或者母耳标携带子耳标
        :param coordinatelist:
        :param lora_list:
        :param historical_time:
        :param number:
        :param bluetooth_list:
        :param minutes:
        :param coordinate_within:
        :return:
        """
        for device_eui in lora_list:
            if bluetooth_list is None:
                self.crazy_transitions_bluetooth(coordinatelist=coordinatelist, deviceEui=device_eui,
                                                 historical_time=historical_time, number=number, minutes=minutes,
                                                 coordinate_within=coordinate_within)
                return
            bluetiigth = random.randint(0, len(bluetooth_list) - 1)
            b_l = []
            if bluetiigth == len(bluetooth_list) - 1:
                b_l = bluetooth_list
            else:
                for x in range(bluetiigth):
                    b = random.choice(bluetooth_list)
                    b_l.append(b)
                    bluetooth_list.remove(b)
            self.crazy_transitions_bluetooth(coordinatelist=coordinatelist, deviceEui=device_eui,
                                             historical_time=historical_time, number=number, minutes=minutes,
                                             coordinate_within=coordinate_within, bluetooth_list=b_l)

    def much_transitions_lora(self, coordinatelist: list = ..., lora_list: list = ..., historical_time=None,
                              number=1, minutes=None, coordinate_within=None):
        """
        批量转场lora耳标
        :param coordinatelist:
        :param lora_list:
        :param historical_time:
        :param number:
        :param bluetooth_list:
        :param minutes:
        :param coordinate_within:
        :return:
        """
        for device_eui in lora_list:
            self.crazy_transitions_lora(coordinatelist=coordinatelist, deviceEui=device_eui,
                                        historical_time=historical_time, number=number, minutes=minutes,
                                        coordinate_within=coordinate_within)


if __name__ == '__main__':
    t = Transitions('WORLD_PROD')
    # within_list = [{"lng": 150.57414781610612, "lat": -27.519481783673406},
    #                {"lng": 150.56478489414854, "lat": -27.655273904126425},
    #                {"lng": 150.75885273118996, "lat": -27.663001447400987},
    #                {"lng": 150.76864124051968, "lat": -27.520991508341282}
    #                ]
    # outer_list = [{"lng": 150.52162484753785, "lat": -27.687174705579203},
    #               {"lng": 150.5207651438139, "lat": -27.709122325271863},
    #               {"lng": 150.5548667256765, "lat": -27.711151939921947},
    #               {"lng": 150.55715926900285, "lat": -27.700369179476354}]

    outer_list = [{"lng": 104.0637184721982, "lat": 30.54485225837966},
                  {"lng": 104.0620286913522, "lat": 30.543261173741872},
                  {"lng": 104.0619367580414, "lat": 30.541270415507729},
                  {"lng": 104.06314502320591, "lat": 30.538827156336382},
                  {"lng": 104.0666902366698, "lat": 30.536609911701479},
                  {"lng": 104.0704274462944, "lat": 30.53887240211537},
                  {"lng": 104.07106954871951, "lat": 30.540376822721139},
                  {"lng": 104.0710235819122, "lat": 30.542972742124761},
                  {"lng": 104.0707215157679, "lat": 30.544742904622911},
                  {"lng": 104.0674526506965, "lat": 30.546654547770601},
                  {"lng": 104.0637184721982, "lat": 30.54485225837966}]
    bluetooth_list = ["0102020000001508"]
    device_eui_list = ["0101050000000566", "1201050300000073", "1201050300000066"]
    lora_list = ["1101030300000012", "1101010300000025"]

    # 单个母耳标携带子耳标转场
    # # 当前农场的母耳标
    # t.transitions_bluetooth(deviceEui='0101050000000573', bluetooth_list=bluetooth_list, lat=-27.592542919619923,
    #                         lng=150.6670627836083)

    # 单个母耳标不携带子耳标转场
    # t.transitions_bluetooth(deviceEui='0101050000000539', lat=30.540903411901823, lng=104.06596182539641)

    # # 多个母耳标携带子耳标转场   随机定位点
    t.much_transitions_bluetooth(coordinatelist=outer_list, lora_list=device_eui_list, bluetooth_list=bluetooth_list,
                                 number=1)

    # 多个母耳标转场   随机定位点
    # t.much_transitions_bluetooth(coordinatelist=outer_list, lora_list=device_eui_list)

    # 多个lora耳标转场  随机定位
    t.much_transitions_lora(coordinatelist=outer_list, lora_list=lora_list, number=1)

    # 单个lora耳标转场
    # t.transitions_lora(deviceEui='0102020000001535', lat=25.906495, lng=106.136292)
    # t.transitions_lora(deviceEui='0102020000001535', lat=25.906703, lng=106.13558)
    # t.transitions_lora(deviceEui='1101030300000014', lat=30.540709939979592, lng=104.0664540552209)
    # time.sleep(3)
    # t.transitions_lora(deviceEui='11020203f0000030', lat=-27.59055420476993, lng=150.66316222054792)
    # time.sleep(3)
    # t.transitions_lora(deviceEui='1101030300000014', lat=-27.607304685415095, lng=150.65288892748032)
    # time.sleep(3)
    # t.transitions_lora(deviceEui='1101030300000014', lat=-27.607304685415095, lng=150.65288892748032)
    # t.transitions_lora(deviceEui='11020203a0000850', lat=30.540709939979592, lng=104.0664540552209)
    # 线上演示mock坐标

    # t.trans_position(deviceEui='1101030300000003', deviceType='1', currentFrequency='40', positionUniqueNo='1101030300000015', isTake='0', lat=None, lng=None,
    #                  channelType=None, channelDeviceEui=None, distance=None, hdop=0, positionTime=None,
    #                  uploadTime=None)

    # t.transitions_bluetooth(deviceEui='1234567890000005', bluetooth_list=bluetooth_list, lat=30.17985196995849,
    #                         lng=104.09331266121478)

    # t.transitions_lora(deviceEui='1101010300000031', lat=-27.602025087762186, lng=150.66983417170098)
    # time.sleep(5)
    # t.transitions_lora(deviceEui='1101010300000031', lat=-27.593289786828294, lng=150.67567241868483)
    # time.sleep(5)
    # t.transitions_lora(deviceEui='1101010300000031', lat=-27.59268500947544, lng=150.6814348442482)
    # time.sleep(5)
    # t.transitions_lora(deviceEui='1101010300000031', lat=-27.59496970646532, lng=150.69045758954627)
