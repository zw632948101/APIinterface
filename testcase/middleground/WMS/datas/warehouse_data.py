import random

from testcase.middleground.WMS.common.Mysql import mp_label

class warehouse_data:


    admin_warehouse_add = [
        {"title":"新增仓库-正常新增","url":"/admin/warehouse/add",
         "data":{"name":"快消品仓库-2",
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
                 "remark":"测试仓库新增"},
         "expect":"OK"},
        {"title":"仓库名字为空","url":"/admin/warehouse/add",
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
        },"expect":"ERROR"},
        {"title":"归属为空","url":"/admin/warehouse/add",
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
            "remark":"测试仓库新增"},"expect":"ERROR"},
        {"title":"仓库类型为空","url":"/admin/warehouse/add",
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
            "remark":"测试仓库新增"},"expect":"ERROR"},
        {"title":"仓库联系人为空","url":"/admin/warehouse/add",
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
            "remark":"测试仓库新增"},"expect":"ERROR"},
        {"title":"仓库详细地址为空","url":"/admin/warehouse/add",
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
            "remark":"测试仓库新增"},"expect":"ERROR"}
    ]
    admin_warehouse_additional_update = [
                                            {"title":"更新附加属性",
                                          "data":{"images":"https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00771-3762.jpg","id":"1","area":"800","capacity":"2","cargoType":"洋槐蜜"},
                                          "expect":"OK"},
                                            {
                                                "title":"图片-非法格式",
                                                "data":{
                                                        "images":"https://gif.sina.com.cn/f.sinaimg.cn/tech/transform/528/w274h254/20210104/1d69-kherpxx5074547.gif",
                                                        "id":"1",
                                                        "area":"800",
                                                        "capacity":"2",
                                                        "cargoType":"洋槐蜜"
                                                        },
                                                "expect":"ERROR"
                                            },
                                            {
                                                "title":"id-为空值",
                                                "data":{
                                                            "images":"https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00771-3762.jpg",
                                                            "id":None,
                                                            "area":"800",
                                                            "capacity":"2",
                                                            "cargoType":"洋槐蜜"},
                                                "expect":"ERROR"
                                            },
                                            {
                                                "title":"货物类型-为空值",
                                                "data":{
                                                            "images":"https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00771-3762.jpg",
                                                            "id":"1",
                                                            "area":"800",
                                                            "capacity":"2",
                                                            "cargoType":None
                                                        },
                                                "expect":"OK"
                                            },
                                            {
                                                "title":"图片-图片为空",
                                                "data":{
                                                        "images":"",
                                                        "id":"1",
                                                        "area":"800",
                                                        "capacity":"2",
                                                        "cargoType":"洋槐蜜"
                                                        },
                                                "expect":"OK"}
                                        ]
    admin_warehouse_count = [
                                {'title':"仓库统计-统计","data":{},"expect":"OK"},
                                {"title":"仓库统计-为空","data":{},"expect":"OK"}
                             ]
    admin_warehouse_del = []
    admin_warehouse_detail = [{"title":"详情-附加属性","data":{"id":1},"expect":"OK"},
                              {"title":"id传空","data":{"id":None},"expect":"ERROR"},
                              {"title":"id传负值", "data": {"id":-100}, "expect":"ERROR"}
                              ]
    admin_warehouse_list = [{"title":"仓库列表-已停用","data":{"status":0},"expect":"OK"},
                            {"title":"仓库列表-已启用","data":{"status":1},"expect":"OK"},
                            {"title":"仓库列表-默认","data":{"status":None},"expect":"OK"}

                            ]
    admin_warehouse_page_list = [{"title":"",
                                  "data":{"pn":"1",
                                          "ps":"10",
                                          "nameOrCode":"",
                                          "status":"",
                                          "typeId":"",
                                          "companyName":"",
                                          "province":"",
                                          "city":"",
                                          "county":"",
                                          "adminNameOrPhone":""},
                                  "expect":"OK"}]
    admin_warehouse_push_to_erp = [
                                    {"title":"同步erp","data":{"id":56},"expect":"OK"},
                                    {"title":"id-为空","data":{"id":None},"expect":"ERROR"}
                                   ]
    admin_warehouse_update = [{"title":"修改仓库信息-正常修改","url":"/admin/warehouse/update",
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
                 "remark":"测试仓库新增"},
         "expect":"OK"}]
    admin_wraehouse_rename = [{"title":"修改设备名","url":"/admin/warehouse/monitor/rename",
                               "data":{"name":"乐山监控001"},
                               "expect":"OK"},
                              {"title":"名字传空","url":"/admin/warehouse/monitor/rename",
                               "data":{"name":None},
                               "expect":"ERROR"},
                              {"title":"名字长度超限","url":"/admin/warehouse/monitor/rename",
                               "data": {"name":"进取参加班级学校组织的各种课内外活动喜欢和同学讨论并解决问题"},
                               "expect":"ERROR"}
                              ]
    admin_warehouse_monitor_list = [{"title":"获取绑定的列表","url":"/admin/warehouse/monitor/list","data":{"id":"1"},"expect":"OK"},
                                    {"title":"id传空","url":"/admin/warehouse/monitor/list","data":{"id":None},"expect":"ERROR"}]
    admin_wraehouse_employee_add = [
                                    {"title":"员工关联-正常关联",
                                     "data":{"userIds":[18457,18607,18595,18511,18315],"warehouseId":random.choice(mp_label().git_warehouse_status())['id']},
                                     "expect":"OK"},{"title":"员工关联-id为空",
                                     "data":{"userIds":"","warehouseId":"111"},
                                     "expect":"ERROR"},{"title":"员工关联-id不存在",
                                     "data":{"userIds":"[99999,88888]","warehouseId":"111"},
                                     "expect":"ERROR"},{"title":"员工关联-仓库id为空",
                                     "data":{"userIds":"[18457,18607,18595,18511,18315]","warehouseId":""},
                                     "expect":"ERROR"},{"title":"员工关联-仓库id不存在",
                                     "data":{"userIds":"[18457,18607,18595,18511,18315]","warehouseId":"99999999"},
                                     "expect":"ERROR"}
                                    ]
    admin_wraehouse_employee_del = [{"title":"解除绑定-正常解除",
                                     "data":{"warehouseEmployeeId":mp_label().git_warehouse_employee()[0]['id']},
                                     "expect":"OK"},
                                    {"title":"解除绑定-id为空","data":{"warehouseEmployeeId":""},"expect":"ERROR"},
                                    {"title":"解除绑定-id不存在","data":{"warehouseEmployeeId":"777777777"},"expect":"ERROR"}]
    admin_wraehouse_employee_list = [
                                        {"title":"",
                                         "data":{"id":mp_label().git_warehouse_employee()[0]['id']},
                                         "expect":"OK"},
                                        {"title":"",
                                         "data":{"id":''},
                                         "expect":"ERROR"}
                                    ]





