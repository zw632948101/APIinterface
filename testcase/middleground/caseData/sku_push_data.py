#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
class Random:

    # 随机名字
    def create_name(self):
        mz = ["花蜜","眼蜜","枝蜜","条蜜","树蜜","英蜜","樨蜜","槐蜜","葵蜜","菜蜜","子蜜","胶蜜","麦蜜","瓜蜜","桔蜜","刺蜜","木蜜","橘蜜","桕蜜"]
        sj = time.strftime('%S', time.localtime(time.time())) # 获取当前时间秒
        name = "追花族-" + random.choice(mz) + sj + '-kg'
        return name
class push_sku:
    list_sku = [{'code': 'T0101010042', 'name': '追花族-枝蜜08-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609139949000}, {'code': 'T0101010041', 'name': '追花族-枝蜜34-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609139916000}, {'code': 'T0101010040', 'name': '追花族-桕蜜08-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609139830000}, {'code': 'T0101010039', 'name': '追花族-花蜜23-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609139784000}, {'code': 'T0101010038', 'name': '追花族-子蜜00-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609139761000}, {'code': 'T0101010037', 'name': '追花族-樨蜜12-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609139714000}, {'code': 'T0101010036', 'name': '追花族-胶蜜06-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609138207000}, {'code': 'T0101010035', 'name': '追花族-花蜜48-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609138190000}, {'code': 'T0101010034', 'name': '追花族-麦蜜02-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 2, 'editor': '张三呵呵呵', 'editTime': 1609138145000}, {'code': 'T0101010033', 'name': '追花族-树蜜09-kg', 'alias': '荷花粉2.5kg', 'class1': '一级分类', 'class2': '二级分类', 'class3': '三级分类', 'basicCost': 1, 'minimumPrice': 2, 'marketPrice': 2, 'hasSourceCode': 1, 'inventoryUnit': 1, 'inventoryUnitName': '千克', 'status': 1, 'editor': '张三呵呵呵', 'editTime': 1609138090000}]
    # sku_add = [{"title":"新增商品",
    #             "data":{"name_":"测试22",             # 名字
    #                     "alias_":"222测试",            # 展示别名
    #                     "class1_":"C01",           # 一级分类码
    #                     "class2_":"C0101",           # 二级分类码
    #                     "class3_":"C010101",           # 三级分类码
    #                     "brandId_":2,          # 品牌
    #                     "basicCost_":0.01,        # 成本价
    #                     "minimumPrice_":0.01,     # 最低售价
    #                     "marketPrice_":0.01,      # 市场价
    #                     "validity_":12,         # 有效期
    #                     "validityUnit_":"MONTH",     # 有效期单位
    #                     "netWeight_":2.5,        # 净重
    #                     "grossWeight_":2.5,      # 毛重
    #                     # "baseUnit_":"",         # 基本单位
    #                     # "isSale_":1,           # 是否直接销售
    #                     "airTransport_":0,     # 是否可空运
    #                     "basicAttr_":[{"id":5,"attrName":"制作工艺","attrValue":"烘干"}],        # 属性
    #                     "saleAttr_":[{"id":6,"attrName":"重量","attrValue":"2.5kg"}],         # 规格
    #                     "length_":50,           # 长
    #                     "width_":10,            # 宽
    #                     "height_":30,           # 高
    #                     "volume_":50,           # 体积
    #                     "barCode_":6903244679206,          # SKU条码
    #                     "batchMnt_":1,         # 是否批次管理
    #                     "hasSourceCode_":1,    # 是否朔源商品
    #                     "needWeigh_":1,        # 是否需要称重
    #                     "inventoryUnit_":"千克",    # 库存计量单位
    #                     "purchaseUnit_":"千克",     # 采购计量单位
    #                     "salesUnit_":"克",        # 销售计量单位
    #                     "salesUnitQuantity_":"克",# 销售单位数量
    #                     "purchaseUnitQuantity_":"千克",# 采购单位数量
    #                     "purchaseTaxId_":7,    # 采购税编码
    #                     "salesTaxId_":1,       # 一般纳税人编码
    #                     "salesTaxId2_":7,      # 小规模纳税人
    #                     "accessoryCost_":20,    # 辅料成本
    #                     "productType_":2,      # 商品类型
    #                     "skuRelatedStr_":""},   # 关联sku
    #             "expect":""},
    sku_add = [{"title":"",
                    "data":{
                            "brandId_": 1,
                            "name_": Random().create_name(),
                            "alias_": "荷花粉2.5kg",
                            "marketPrice_": 2,
                            "basicCost_": 1,
                            "minimumPrice_": 2,
                            "barCode_": 6926032345022,
                            "batchMnt_": 1,
                            "hasSourceCode_": 1,
                            "needWeigh_": 1,
                            "productType_": 3,
                            "salesTaxId_": 8,
                            "salesTaxId2_": 7,
                            "purchaseTaxId_": 4,
                            "inventoryUnit_": 1,
                            "purchaseUnit_": 1,
                            "salesUnit_": 1,
                            "purchaseUnitQuantity_": 100,
                            "salesUnitQuantity_": 1,
                            "accessoryCost_": 5,
                            "validity_": 12,
                            "validityUnit_": "MONTH",
                            "grossWeight_": 32,
                            "netWeight_": 20,
                            "volume_": 30,
                            "airTransport_": 0,
                            "length_": 50,
                            "width_": 30,
                            "height_": 20,
                            "class1_": "T01",
                            "class2_": "T0101",
                            "class3_": "T010101",
                            "saleAttr_": [{"id": 25,"attrName": "2.6-5kg","attrValue": "3kg"}],
                            "basicAttr_": [{"id": 45,"attrName": "现摇","attrValue": "荷花粉"}],
                            "skuRelatedStr_":""
                    },
                    "expect":"OK"}]


if __name__ == '__main__':
    sku = []
    t = push_sku().list_sku
    for i in t:
      print(i)
      sku.append(i['code'])
    print(sku)