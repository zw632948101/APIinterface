



class warehouse_data:


    admin_warehouse_add = [
        {"title":"新增仓库-正常新增","url":"/mp-wms/admin/warehouse/add",
         "data":{"name":"快消品仓库",
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
         "expect":"OK"}
        # {"title":"仓库名字为空","url":"/mp-wms/admin/warehouse/add",
        #  "data":{
        #     "name":None,
        #     "outWarehouseCode":"",
        #     "companyCode":1,
        #     "warehouseTypeId":1,
        #     "contactId":"18593",
        #     "province":"110000",
        #     "city":"110100",
        #     "county":"110101",
        #     "lng":"104.044891",
        #     "lat":"30.550085",
        #     "address":"成都市高新区软件园D区吉泰路5号",
        #     "status":"1",
        #     "isThird":"0",
        #     "isVirtual":"0",
        #     "remark":"测试仓库新增"
        # },"expect":"ERROR"},
        # {"title":"归属为空","url":"/mp-wms/admin/warehouse/add",
        #  "data":{
        #     "name":"测试仓库002",
        #     "outWarehouseCode":"",
        #     "companyCode":None,
        #     "warehouseTypeId":1,
        #     "contactId":"18516",
        #     "province":"110000",
        #     "city":"110100",
        #     "county":"110101",
        #     "lng":"104.044891",
        #     "lat":"30.550085",
        #     "address":"成都市高新区软件园D区吉泰路5号",
        #     "status":"1",
        #     "isThird":"0",
        #     "isVirtual":"0",
        #     "remark":"测试仓库新增"},"expect":"ERROR"},
        # {"title":"仓库类型为空","url":"/mp-wms/admin/warehouse/add",
        #  "data":{
        #     "name":"测试仓库002",
        #     "outWarehouseCode":"",
        #     "companyCode":1,
        #     "warehouseTypeId":None,
        #     "contactId":"18593",
        #     "province":"110000",
        #     "city":"110100",
        #     "county":"110101",
        #     "lng":"104.044891",
        #     "lat":"30.550085",
        #     "address":"成都市高新区软件园D区吉泰路5号",
        #     "status":"1",
        #     "isThird":"0",
        #     "isVirtual":"0",
        #     "remark":"测试仓库新增"},"expect":"ERROR"},
        # {"title":"仓库联系人为空","url":"/mp-wms/admin/warehouse/add",
        #  "data":{
        #     "name":"测试仓库002",
        #     "outWarehouseCode":"",
        #     "companyCode":1,
        #     "warehouseTypeId":1,
        #     "contactId":None,
        #     "province":"110000",
        #     "city":"110100",
        #     "county":"110101",
        #     "lng":"104.044891",
        #     "lat":"30.550085",
        #     "address":"成都市高新区软件园D区吉泰路5号",
        #     "status":"1",
        #     "isThird":"0",
        #     "isVirtual":"0",
        #     "remark":"测试仓库新增"},"expect":"ERROR"},
        # {"title":"仓库详细地址为空","url":"/mp-wms/admin/warehouse/add",
        #  "data":{
        #     "name":"测试仓库002",
        #     "outWarehouseCode":"",
        #     "companyCode":1,
        #     "warehouseTypeId":1,
        #     "contactId":18593,
        #     "province":"110000",
        #     "city":"110100",
        #     "county":"110101",
        #     "lng":"104.044891",
        #     "lat":"30.550085",
        #     "address":None,
        #     "status":"1",
        #     "isThird":"0",
        #     "isVirtual":"0",
        #     "remark":"测试仓库新增"},"expect":"ERROR"}
    ]
    admin_warehouse_additional_update = [

    ]
    admin_warehouse_count = []
    admin_warehouse_del = []
    admin_warehouse_detail = []
    admin_warehouse_list = []
    admin_warehouse_page_list = []
    admin_warehouse_push_to_erp = []
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


