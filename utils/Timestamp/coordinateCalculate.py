#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

"""
import json
from random import uniform


class coordinateCalculate(object):
    def __init__(self):
        super(coordinateCalculate, self).__init__()

    @staticmethod
    def dispose_data(coordinatelist):
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

    @staticmethod
    def create_transitions(coordinate_outer, coordinate_within=None):
        """
        生成一个随机定位点,
        coordinate_outer 传参只会生成内圈的随机点
        coordinate_within 不为空时,生成大于内圈小于外圈的随机点
        :list coordinate_outer:生成随机点的内圈
        :list coordinate_within:生成随机点的外圈
        :return:
        """
        lng_lo, lat_lo = coordinateCalculate.dispose_data(coordinate_outer)
        if coordinate_within is None:
            lng = uniform(lng_lo[0], lng_lo[1])
            lat = uniform(lat_lo[0], lat_lo[1])
            return lng, lat

        lng_lw, lat_lw = coordinateCalculate.dispose_data(coordinate_within)
        lat = lng = 0
        while True:
            if lng == 0:
                lng = uniform(lng_lo[0], lng_lo[1])
            if lat == 0:
                lat = uniform(lat_lo[0], lat_lo[1])
            if not (lng_lw[0] < lng < lng_lw[1]):
                lng = 0
            if not (lat_lw[0] < lat < lat_lw[1]):
                lat = 0
            if (lng_lw[0] < lng < lng_lw[1]) and (lat_lw[0] < lat < lat_lw[1]):
                break
        return lng, lat

    @staticmethod
    def assemble_circuit_location(one_circuit, bifurcate_circuit1, bifurcate_circuit2):
        """
        组合线型地标坐标集
        :param one_circuit:
        :param bifurcate_circuit1:
        :param bifurcate_circuit2:
        :return:
        """
        leafNodes = {
            "branchNode": False,
            "leafNodes": [
            ],
            "location": {
                "lat": -27.61998178738515,
                "lng": 150.6437266043214
            }
        }
        leafNodes_b = leafNodes.copy()
        leafNodes_u = leafNodes.copy()
        leafNodes = {}
        pl = [i for i in range(3)]
        pl.sort(reverse=True)
        for i in pl:
            leafNodes_p_bl = leafNodes.copy()
            leafNodes_p_ul = leafNodes.copy()
            if i == 2:
                leafNodes_p_bl['branchNode'] = True
            leafNodes_p_bl['location'] = bifurcate_circuit1[i]
            leafNodes_p_ul['location'] = bifurcate_circuit2[i]
            if i < 2:
                leafNodes_p_bl['leafNodes'] = [leafNodes_b]
                leafNodes_p_ul['leafNodes'] = [leafNodes_u]
            leafNodes_b = leafNodes_p_bl
            leafNodes_u = leafNodes_p_ul

        for i in pl:
            if i < pl[0]:
                leafNodes1 = leafNodes.copy()
                leafNodes1['location'] = one_circuit[i]
                if i == 1:
                    leafNodes1['leafNodes'] = [leafNodes_p_bl, leafNodes_p_ul]
                if i == 0:
                    leafNodes1['leafNodes'] = [leafNodes]
                leafNodes = leafNodes1
        leafNodes = json.dumps(leafNodes)
        return leafNodes

    @staticmethod
    def linetype_land(coordinate_outer, kind):
        lng, lat = coordinateCalculate.dispose_data(coordinate_outer)
        centre_lng = (lng[1] - lng[0]) / 2 + lng[0]
        centre_lat = (lat[1] - lat[0]) / 2 + lat[0]
        distance = 0.002500
        if kind == '10160':
            p = [{"lng": (centre_lng + distance * i), "lat": (centre_lat + distance * i)} for i in
                 range(1, 3)]

            p_bl = [{"lng": (p[1].get('lng') + distance * (i / 2)), "lat": (p[1].get('lat') + distance * i)} for i in
                    range(1, 4)]
            p_ul = [{"lng": (p[1].get('lng') + distance * (i / 2)), "lat": (p[1].get('lat') - distance * i)} for i in
                    range(1, 4)]
        if kind == '10170':
            p = [{"lng": (centre_lng - distance * i), "lat": (centre_lat - distance * i)} for i in
                 range(1, 3)]

            p_bl = [{"lng": (p[1].get('lng') - distance * (i / 2)), "lat": (p[1].get('lat') + distance * i)} for i in
                    range(1, 4)]
            p_ul = [{"lng": (p[1].get('lng') - distance * (i / 2)), "lat": (p[1].get('lat') - distance * i)} for i in
                    range(1, 4)]

        if kind == '10220':
            p = [{"lng": (centre_lng), "lat": (centre_lat - distance * i)} for i in
                 range(1, 3)]

            p_bl = [{"lng": (p[1].get('lng') - distance * (i / 2)), "lat": (p[1].get('lat') - distance * i)} for i in
                    range(1, 4)]
            p_ul = [{"lng": (p[1].get('lng') + distance * (i / 2)), "lat": (p[1].get('lat') - distance * i)} for i in
                    range(1, 4)]

        leafNodes = coordinateCalculate.assemble_circuit_location(p, p_bl, p_ul)
        return leafNodes

    @staticmethod
    def dot_land(coordinate_outer):
        lng, lat = coordinateCalculate.create_transitions(coordinate_outer)
        return str({'lat': lat, 'lng': lng})
