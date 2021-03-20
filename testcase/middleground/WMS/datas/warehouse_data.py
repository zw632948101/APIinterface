import random
import json
from testcase.middleground.WMS.common.listName import Random

from testcase.middleground.WMS.common.Mysql import mp_label

class warehouse_data:
    order_add = [
        {
            "title": "新增仓库",
            "data": {

                        "relevanceCode_": "测试从", # 关联单据编号
                        "source_": "ERP", # 来源系统
                        "type_": "RK02", # 单据类型
                        "warehouseCode_": 30020, # 入库仓库
                        "company_": 100001, # 所属公司
                        "supplier_": None, # 供应商
                        "supplierName_": None, # 供应商名称
                        "initiator_": 18593, # 发起人ID
                        "remark_": "", # 备注
                        "erpType_": 104.068556, # erp单据类型
                        "erpDocNum_": 30.537945, # erp业务系统采购订单号(企业微信单号)
                        "productInfo_": "四川省成都市武侯区天府软件园E区5-1号楼" # 商品信息JSON数组
                    },
            "expect": "OK"}
                ]
    warehouse_add = [
                        {
                            "title": "新增仓库",
                            "data":{
                                    "name_":"测试从",
                                    "outWarehouseCode_":None,
                                    "companyCode_":100002,
                                    "shopCode_":None,
                                    "warehouseTypeId_":3,
                                    "contactId_":18593,
                                    "province_":510000,
                                    "city_":510100,
                                    "county_":510107,
                                    "lng_":104.068556,
                                    "lat_":30.537945,
                                    "address_":"四川省成都市武侯区天府软件园E区5-1号楼",
                                    "status_":1,
                                    "isThird_":0,
                                    "isVirtual_":0,
                                    "isMonitor_":0,
                                    "remark_":None},
                            "expect":"OK"},
                        {
                            "title": "库名为空",
                            "data": {
                                "name_": None,
                                "outWarehouseCode_": None,
                                "companyCode_": 100002,
                                "shopCode_": None,
                                "warehouseTypeId_": 3,
                                "contactId_": 18593,
                                "province_": 510000,
                                "city_": 510100,
                                "county_": 510107,
                                "lng_": 104.068556,
                                "lat_": 30.537945,
                                "address_": "四川省成都市武侯区天府软件园E区5-1号楼",
                                "status_": 1,
                                "isThird_": 0,
                                "isVirtual_": 0,
                                "isMonitor_": 0,
                                "remark_": None},
                            "expect": "ERROR"
                        },
                        {
                            "title": "属公司空",
                            "data": {
                                "name_": "测试从",
                                "outWarehouseCode_": None,
                                "companyCode_": None,
                                "shopCode_": None,
                                "warehouseTypeId_": 3,
                                "contactId_": 18593,
                                "province_": 510000,
                                "city_": 510100,
                                "county_": 510107,
                                "lng_": 104.068556,
                                "lat_": 30.537945,
                                "address_": "四川省成都市武侯区天府软件园E区5-1号楼",
                                "status_": 1,
                                "isThird_": 0,
                                "isVirtual_": 0,
                                "isMonitor_": 0,
                                "remark_": None},
                            "expect": "ERROR"
                        },
                        {
                            "title": "公司编号不存在",
                            "data": {
                                "name_": "测试从",
                                "outWarehouseCode_": None,
                                "companyCode_": -000000,
                                "shopCode_": None,
                                "warehouseTypeId_": 3,
                                "contactId_": 18593,
                                "province_": 510000,
                                "city_": 510100,
                                "county_": 510107,
                                "lng_": 104.068556,
                                "lat_": 30.537945,
                                "address_": "四川省成都市武侯区天府软件园E区5-1号楼",
                                "status_": 1,
                                "isThird_": 0,
                                "isVirtual_": 0,
                                "isMonitor_": 0,
                                "remark_": None},
                            "expect": "ERROR"
                        },
                        {
                            "title": "启用状态异常",
                            "data": {
                                "name_": "测试从",
                                "outWarehouseCode_": None,
                                "companyCode_": 100002,
                                "shopCode_": None,
                                "warehouseTypeId_": 3,
                                "contactId_": 18593,
                                "province_": 510000,
                                "city_": 510100,
                                "county_": 510107,
                                "lng_": 104.068556,
                                "lat_": 30.537945,
                                "address_": "四川省成都市武侯区天府软件园E区5-1号楼",
                                "status_": 3,
                                "isThird_": 0,
                                "isVirtual_": 0,
                                "isMonitor_": 0,
                                "remark_": None},
                            "expect": "ERROR"
                        },
                        {"title": "仓库联系人为空",
                            "data": {
                                "name_": "测试从",
                                "outWarehouseCode_": None,
                                "companyCode_": 100002,
                                "shopCode_": None,
                                "warehouseTypeId_": 3,
                                "contactId_": None,
                                "province_": 510000,
                                "city_": 510100,
                                "county_": 510107,
                                "lng_": 104.068556,
                                "lat_": 30.537945,
                                "address_": "四川省成都市武侯区天府软件园E区5-1号楼",
                                "status_": 3,
                                "isThird_": 0,
                                "isVirtual_": 0,
                                "isMonitor_": 0,
                                "remark_": None},
                            "expect": "ERROR"},
                        {
                            "title": "仓库联系人ID不存在",
                            "data": {
                                "name_": "测试从",
                                "outWarehouseCode_": None,
                                "companyCode_": 100002,
                                "shopCode_": None,
                                "warehouseTypeId_": 3,
                                "contactId_": -000000,
                                "province_": 510000,
                                "city_": 510100,
                                "county_": 510107,
                                "lng_": 104.068556,
                                "lat_": 30.537945,
                                "address_": "四川省成都市武侯区天府软件园E区5-1号楼",
                                "status_": 3,
                                "isThird_": 0,
                                "isVirtual_": 0,
                                "isMonitor_": 0,
                                "remark_": None},
                            "expect": "ERROR"
                        },
                        {
                            "title": "备注超限",
                            "data": {
                                "name_": "测试从",
                                "outWarehouseCode_": None,
                                "companyCode_": 100002,
                                "shopCode_": None,
                                "warehouseTypeId_": 3,
                                "contactId_": 18593,
                                "province_": 510000,
                                "city_": 510100,
                                "county_": 510107,
                                "lng_": 104.068556,
                                "lat_": 30.537945,
                                "address_": "四川省成都市武侯区天府软件园E区5-1号楼",
                                "status_": 3,
                                "isThird_": 0,
                                "isVirtual_": 0,
                                "isMonitor_": 0,
                                "remark_": "我萌芽在春天里和你一起成长夏天到来的时候我羞惭惭的抬起了小小的脑袋瓜儿你看不到我我便奋力成长生怕这一生在你的世界里留不下什么印象我拼命地想和你一样于是开出了你阳光般金色的花瓣成了一株小太阳我使劲的绽放为你绽放为你张开笑不成想竟招来了多彩的蝴蝶勤劳的蜜蜂还有不知名的小昆虫唯独你不曾为我多停留一秒渺茫的往事不断在脑海里浮现隐隐约约仿佛花絮般被编入人生的时间总是那么的飞快面对每天所发生的故事我仿佛化身为了拾荒者序章时常对着镜子倾诉总以为自己爱着自"},
                            "expect": "ERROR"
                        }
                        ]

    admin_warehouse_add = [
                            {
                                "title":"新增仓库-正常新增","url":"/admin/warehouse/add",
                                "data":{
                                            "name":"快消品仓库-2",
                                            "outWarehouseCode":"",
                                            "companyCode":1,
                                            "warehouseTypeId":1,
                                            "contactId":"18593",
                                            "province":"110000",
                                            "city":"110100",
                                            "county":"110101",
                                            "lng":"104.044891",
                                            "lat":"30.550085",
                                            "address":"成都市高新区软件园D区吉泰路5号",
                                            "status":"1",
                                            "isThird":"0",
                                            "isVirtual":"0",
                                            "remark":"测试仓库新增"
                                        },
                                "expect":"OK"
                            },
                            {
                                "title":"仓库名字为空","url":"/admin/warehouse/add",
                                "data":{
                                            "name":None,
                                            "outWarehouseCode":"",
                                            "companyCode":1,
                                            "warehouseTypeId":1,
                                            "contactId":"18593",
                                            "province":"110000",
                                            "city":"110100",
                                            "county":"110101",
                                            "lng":"104.044891",
                                            "lat":"30.550085",
                                            "address":"成都市高新区软件园D区吉泰路5号",
                                            "status":"1",
                                            "isThird":"0",
                                            "isVirtual":"0",
                                            "remark":"测试仓库新增"
                                        },
                                "expect":"ERROR"
                            },
                            {
                                "title":"归属为空","url":"/admin/warehouse/add",
                                "data":{
                                            "name":"测试仓库002",
                                            "outWarehouseCode":"",
                                            "companyCode":None,
                                            "warehouseTypeId":1,
                                            "contactId":"18516",
                                            "province":"110000",
                                            "city":"110100",
                                            "county":"110101",
                                            "lng":"104.044891",
                                            "lat":"30.550085",
                                            "address":"成都市高新区软件园D区吉泰路5号",
                                            "status":"1",
                                            "isThird":"0",
                                            "isVirtual":"0",
                                            "remark":"测试仓库新增"
                                        },
                                "expect":"ERROR"
                            },
                            {
                                "title":"仓库类型为空","url":"/admin/warehouse/add",
                                "data":{
                                            "name":"测试仓库002",
                                            "outWarehouseCode":"",
                                            "companyCode":1,
                                            "warehouseTypeId":None,
                                            "contactId":"18593",
                                            "province":"110000",
                                            "city":"110100",
                                            "county":"110101",
                                            "lng":"104.044891",
                                            "lat":"30.550085",
                                            "address":"成都市高新区软件园D区吉泰路5号",
                                            "status":"1",
                                            "isThird":"0",
                                            "isVirtual":"0",
                                            "remark":"测试仓库新增"
                            },
                                "expect":"ERROR"
                            },
                            {
                                "title":"仓库联系人为空","url":"/admin/warehouse/add",
                                "data":{
                                            "name":"测试仓库002",
                                            "outWarehouseCode":"",
                                            "companyCode":1,
                                            "warehouseTypeId":1,
                                            "contactId":None,
                                            "province":"110000",
                                            "city":"110100",
                                            "county":"110101",
                                            "lng":"104.044891",
                                            "lat":"30.550085",
                                            "address":"成都市高新区软件园D区吉泰路5号",
                                            "status":"1",
                                            "isThird":"0",
                                            "isVirtual":"0",
                                            "remark":"测试仓库新增"
                                        },
                                "expect":"ERROR"
                            },
                            {
                                "title":"仓库详细地址为空","url":"/admin/warehouse/add",
                                "data":{
                                            "name":"测试仓库002",
                                            "outWarehouseCode":"",
                                            "companyCode":1,
                                            "warehouseTypeId":1,
                                            "contactId":18593,
                                            "province":"110000",
                                            "city":"110100",
                                            "county":"110101",
                                            "lng":"104.044891",
                                            "lat":"30.550085",
                                            "address":None,
                                            "status":"1",
                                            "isThird":"0",
                                            "isVirtual":"0",
                                            "remark":"测试仓库新增"
                                        },
                                "expect":"ERROR"
                            }
                            ]
    admin_warehouse_additional_update = [
                                            {
                                                "title":"更新附加属性",
                                                "data":{
                                                            "images_":Random().create_name(1),
                                                            "id_":"",
                                                            "area_":1000,
                                                            "capacity_":100,
                                                            "cargoType_":"测试附加属性更新"
                                                        },
                                                "expect":"OK"
                                            },
                                            {
                                                "title": "面积不填",
                                                "data": {
                                                    "images_": Random().create_name(1),
                                                    "id_": "",
                                                    "area_": None,
                                                    "capacity_": 100,
                                                    "cargoType_": "测试附加属性更新"
                                                },
                                                "expect": "ERROR"
                                            },
                                            {
                                                "title": "容量不填",
                                                "data": {
                                                    "images_": Random().create_name(1),
                                                    "id_": "",
                                                    "area_": 1000,
                                                    "capacity_": None,
                                                    "cargoType_": "测试附加属性更新"
                                                },
                                                "expect": "ERROR"
                                            },
                                            {
                                                "title": "面积错误填写",
                                                "data": {
                                                    "images_": Random().create_name(1),
                                                    "id_": "",
                                                    "area_": "这是面积",
                                                    "capacity_": 100,
                                                    "cargoType_": "测试附加属性更新"
                                                },
                                                "expect": "ERROR"
                                            },
                                            {
                                                "title": "容量填写错误",
                                                "data": {
                                                    "images_": Random().create_name(1),
                                                    "id_": "",
                                                    "area_": 1000,
                                                    "capacity_": "英语.丝享",
                                                    "cargoType_": "测试附加属性更新"
                                                },
                                                "expect": "ERROR"
                                            }
                                        ]
    admin_warehouse_count = [
                                {
                                    'title':"仓库统计-统计",
                                    "data":{},
                                    "expect":"OK"
                                },
                                {
                                    "title":"仓库统计-为空",
                                    "data":{},
                                    "expect":"OK"
                                }
                             ]
    admin_warehouse_del = []
    admin_warehouse_detail = [
                                {
                                    "title":"详情-附加属性",
                                    "data":{"id":1},
                                    "expect":"OK"
                                },
                                {
                                    "title":"id传空",
                                    "data":{"id":None},
                                    "expect":"ERROR"
                                 },
                                {
                                    "title":"id传负值",
                                    "data": {"id":-100},
                                    "expect":"ERROR"
                                }
                              ]
    admin_warehouse_list = [
                                {
                                    "title":"仓库列表-已停用",
                                    "data":{"status":0},
                                    "expect":"OK"
                                 },
                                {
                                    "title":"仓库列表-已启用",
                                    "data":{"status":1},
                                    "expect":"OK"
                                },
                                {
                                    "title":"仓库列表-默认",
                                    "data":{"status":None},
                                    "expect":"OK"
                                }
                            ]
    admin_warehouse_page_list = [
                                    {
                                        "title":"",
                                        "data":{
                                                    "pn":"1",
                                                    "ps":"10",
                                                    "nameOrCode":"",
                                                    "status":"",
                                                    "typeId":"",
                                                    "companyName":"",
                                                    "province":"",
                                                    "city":"",
                                                    "county":"",
                                                    "adminNameOrPhone":""
                                                },
                                        "expect":"OK"
                                    }
                                ]
    admin_warehouse_push_to_erp = [
                                    {
                                        "title":"同步erp",
                                        "data":{"id":56},
                                        "expect":"OK"
                                    },
                                    {
                                        "title":"id-为空",
                                        "data":{"id":None},
                                        "expect":"ERROR"
                                    }
                                   ]
    admin_warehouse_update = [
                                {
                                    "title":"修改仓库信息-正常修改",
                                    "url":"/admin/warehouse/update",
                                    "data":{
                                                "name":"资产仓库1",
                                                "outWarehouseCode":None,
                                                "companyCode":"tongren",
                                                "warehouseTypeId":1,
                                                "contactId":"18515",
                                                "province":"510000",
                                                "city":"510100",
                                                "county":"510107",
                                                "lng":"30.585562",
                                                "lat":"104.070358",
                                                "address":"四川省成都市武侯区成都银泰中心2号楼",
                                                "status":1,
                                                "isThird":1,
                                                "isVirtual":1,
                                                "remark":"测试仓库新增"
                                            },
                                    "expect":"OK"
                                }
                            ]
    admin_wraehouse_rename = [
                                {
                                    "title":"修改设备名",
                                    "url":"/admin/warehouse/monitor/rename",
                                    "data":{
                                                "name":"乐山监控001"
                                            },
                                    "expect":"OK"
                                },
                                {
                                    "title":"名字传空",
                                    "url":"/admin/warehouse/monitor/rename",
                                    "data":{
                                                "name":None
                                            },
                                    "expect":"ERROR"
                                },
                                {
                                    "title":"名字长度超限",
                                    "url":"/admin/warehouse/monitor/rename",
                                    "data": {
                                                "name":"进取参加班级学校组织的各种课内外活动喜欢和同学讨论并解决问题"
                                            },
                                    "expect":"ERROR"
                                }
                              ]
    admin_warehouse_monitor_list = [
                                        {
                                            "title":"获取绑定的列表",
                                            "url":"/admin/warehouse/monitor/list",
                                            "data":{
                                                        "id":"1"
                                                    },
                                            "expect":"OK"
                                        },
                                        {
                                            "title":"id传空",
                                            "url":"/admin/warehouse/monitor/list",
                                            "data":{
                                                        "id":None
                                                    },
                                            "expect":"ERROR"}
                                    ]
    admin_wraehouse_employee_add = [
                                    {"title":"员工关联-正常关联",
                                     "data":{
                                                "userIds":[18457,18607,18595,18511,18315],
                                                "warehouseId":random.choice(mp_label().git_warehouse_status())['id']
                                            },
                                     "expect":"OK"
                                     },
                                    {"title":"员工关联-id为空",
                                     "data":{
                                                "userIds":"",
                                                "warehouseId":"111"
                                            },
                                     "expect":"ERROR"},
                                    {
                                        "title":"员工关联-id不存在",
                                        "data":{
                                                    "userIds":"[99999,88888]",
                                                    "warehouseId":"111"
                                                },
                                        "expect":"ERROR"
                                    },
                                    {
                                        "title":"员工关联-仓库id为空",
                                        "data":{
                                                    "userIds":"[18457,18607,18595,18511,18315]",
                                                    "warehouseId":""
                                                },
                                        "expect":"ERROR"
                                    },
                                    {
                                        "title":"员工关联-仓库id不存在",
                                        "data":{
                                                    "userIds":"[18457,18607,18595,18511,18315]",
                                                    "warehouseId":"99999999"
                                                },
                                        "expect":"ERROR"}
                                    ]
    admin_wraehouse_employee_del = [
                                    {
                                        "title":"解除绑定-正常解除",
                                        "data":{
                                                    "warehouseEmployeeId":mp_label().git_warehouse_employee()[0]['id']
                                                },
                                        "expect":"OK"
                                    },
                                    {
                                        "title":"解除绑定-id为空",
                                        "data":{
                                                    "warehouseEmployeeId":""
                                                },
                                        "expect":"ERROR"
                                    },
                                    {
                                        "title":"解除绑定-id不存在",
                                        "data":{
                                                    "warehouseEmployeeId":"777777777"
                                                },
                                        "expect":"ERROR"
                                    }
                                    ]
    admin_wraehouse_employee_list = [
                                        {
                                            "title":"",
                                            "data":{
                                                        "id":mp_label().git_warehouse_employee()[0]['id']
                                                    },
                                            "expect":"OK"
                                        },
                                        {
                                            "title":"",
                                            "data":{
                                                        "id":''
                                                    },
                                            "expect":"ERROR"
                                        }
                                    ]





