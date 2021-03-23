from testcase.beefcattle.sql.Bullpen_sql import Bullpen
import random
import time
import json
class Random:
    # 只能传list
    def __init__(self,city=None,name=None,now=None):
        if city == None:
            self.city = ["铜仁","郫县","溶洞","音乐空间"]
        else:
            self.city = city
        if name == None:
            self.name = ["行政仓","车间仓","项目仓"]
        else:
            self.name = name
        if now == None:
            self.now = time.strftime('%S', time.localtime(time.time()))
        else:
            self.now = now

        self.img_url = ["https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1767448974,2051103783&fm=26&gp=0",
                        "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3112097844,4213331226&fm=26&gp=0",
                        "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2196976096,3047104416&fm=26&gp=0",
                        "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2013274768,216829781&fm=26&gp=0"]

    def create_name(self,create=None):
        if create == None:
            new_name = random.choice(self.city) \
                       + random.choice(self.name)

            return new_name

        elif create != None:
            new_img = random.choice(self.img_url) + ".jpg"
            return new_img

class bullpen_case:
    admin_cattle_add = [
        {
            "title":"牛只信息-正常新增",
            "data":
                    {
                        "cattleEarTagNo_":"EB"+str(1616402101000+random.randint(0,99)),
                        "cattleFenceId_":Bullpen().get_cattle_fence()[0]['id'],
                        "variety_":random.choice([1000,1001,1002,1003,1004,1005,1006,1007]),
                        "gender_":random.choice([1001,1003,1002]),
                        "birthday_":1579453179000,
                        "entryDate_":1611075579000,
                        "currentChildTime_":"",
                        "birthWeight_":259.99,
                        "feedType_":random.choice(["繁育","育肥"]),
                        "fatherNo_":"F001",
                        "motherNo_":"M001",
                        "rfidCode_":"RF-" + str(random.randint(0,9)),
                        "nucleusGroupStatus_":1,
                        "insureNo_":"",
                        "purchaseOrderNo_":"",
                        "skuCode_":Bullpen().get_product_category_mapping()[0]['sku_code'],
                        "usedNo_":random.choice(['HD0100120','HD0100121','HD0100122','HD0100123','HD0100124']),
                        "pics_":""
                    },
            "expect":"OK",
            "actual":""
        },
        {"title":"牛只信息-牛号不传",
            "data":
                    {
                        "cattleEarTagNo_":"",
                        "cattleFenceId_":Bullpen().get_cattle_fence()[0]['id'],
                        "variety_":random.choice([1000,1001,1002,1003,1004,1005,1006,1007]),
                        "gender_":random.choice([1001,1003,1002]),
                        "birthday_":1579453179000,
                        "entryDate_":1611075579000,
                        "currentChildTime_":"",
                        "birthWeight_":259.99,
                        "feedType_":random.choice(["繁育","育肥"]),
                        "fatherNo_":"F001",
                        "motherNo_":"M001",
                        "rfidCode_":"RF-" + str(random.randint(0,9)),
                        "nucleusGroupStatus_":1,
                        "insureNo_":"",
                        "purchaseOrderNo_":"",
                        "skuCode_":Bullpen().get_product_category_mapping()[0]['sku_code'],
                        "usedNo_":random.choice(['HD0100120','HD0100121','HD0100122','HD0100123','HD0100124']),
                        "pics_":""
                    },
            "expect":"ERROR",
            "actual":""},
        {
            "title": "牛只信息-牛栏不传",
            "data":
                {
                    "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                    "cattleFenceId_": "",
                    "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                    "gender_": random.choice([1001, 1003, 1002]),
                    "birthday_": 1579453179000,
                    "entryDate_": 1611075579000,
                    "currentChildTime_": "",
                    "birthWeight_": 259.99,
                    "feedType_": random.choice(["繁育", "育肥"]),
                    "fatherNo_": "F001",
                    "motherNo_": "M001",
                    "rfidCode_": "RF-" + str(random.randint(0, 9)),
                    "nucleusGroupStatus_": 1,
                    "insureNo_": "",
                    "purchaseOrderNo_": "",
                    "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                    "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                    "pics_": ""
                },
            "expect": "ERROR",
            "actual": ""
        },
        {
            "title": "牛只信息-母牛不传胎次",
            "data":
                {
                    "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                    "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                    "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                    "gender_": 1002,
                    "birthday_": 1579453179000,
                    "entryDate_": 1611075579000,
                    "currentChildTime_":None,
                    "birthWeight_": 259.99,
                    "feedType_": random.choice(["繁育", "育肥"]),
                    "fatherNo_": "F001",
                    "motherNo_": "M001",
                    "rfidCode_": "RF-" + str(random.randint(0, 9)),
                    "nucleusGroupStatus_": 1,
                    "insureNo_": "",
                    "purchaseOrderNo_": "",
                    "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                    "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                    "pics_": ""
                },
            "expect": "ERROR",
            "actual": ""

        },
        {
            "title": "牛只信息-公牛传入胎次",
            "data":
                {
                    "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                    "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                    "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                    "gender_": 1003,
                    "birthday_": 1579453179000,
                    "entryDate_": 1611075579000,
                    "currentChildTime_": "",
                    "birthWeight_": 259.99,
                    "feedType_": random.choice(["繁育", "育肥"]),
                    "fatherNo_": "F001",
                    "motherNo_": "M001",
                    "rfidCode_": "RF-" + str(random.randint(0, 9)),
                    "nucleusGroupStatus_": 1,
                    "insureNo_": "",
                    "purchaseOrderNo_": "",
                    "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                    "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                    "pics_": ""
                },
            "expect": "ERROR",
            "actual": ""
        },
        {
            "title": "牛只信息-SKU码不传",
            "data":
                {
                    "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                    "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                    "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                    "gender_": random.choice([1001, 1003, 1002]),
                    "birthday_": 1579453179000,
                    "entryDate_": 1611075579000,
                    "currentChildTime_": "",
                    "birthWeight_": 259.99,
                    "feedType_": random.choice(["繁育", "育肥"]),
                    "fatherNo_": "F001",
                    "motherNo_": "M001",
                    "rfidCode_": "RF-" + str(random.randint(0, 9)),
                    "nucleusGroupStatus_": 1,
                    "insureNo_": "",
                    "purchaseOrderNo_": "",
                    "skuCode_": None,
                    "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                    "pics_": ""
                },
            "expect": "ERROR",
            "actual": ""

        },
        {
            "title": "牛只信息-曾用牛号不传",
            "data":
                {
                    "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                    "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                    "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                    "gender_": random.choice([1001, 1003, 1002]),
                    "birthday_": 1579453179000,
                    "entryDate_": 1611075579000,
                    "currentChildTime_": "",
                    "birthWeight_": 259.99,
                    "feedType_": random.choice(["繁育", "育肥"]),
                    "fatherNo_": "F001",
                    "motherNo_": "M001",
                    "rfidCode_": "RF-" + str(random.randint(0, 9)),
                    "nucleusGroupStatus_": 1,
                    "insureNo_": "",
                    "purchaseOrderNo_": "",
                    "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                    "usedNo_": None,
                    "pics_": ""
                },
            "expect": "ERROR",
            "actual": ""
        }
    ]
    admin_cattle_batch_add = [
                                {
                                    "title":"批量新增-新增成功",
                                    "data":{
                                                "purchaseOrderNo_":None,
                                                "jsonStr_":[{
                                                                "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                                                                "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                                                                "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                                                                "gender_": random.choice([1001, 1003, 1002]),
                                                                "birthday_": 1579453179000,
                                                                "entryDate_": 1611075579000,
                                                                "currentChildTime_": "",
                                                                "birthWeight_": 259.99,
                                                                "feedType_": random.choice(["繁育", "育肥"]),
                                                                "fatherNo_": "F001",
                                                                "motherNo_": "M001",
                                                                "rfidCode_": "RF-" + str(random.randint(0, 9)),
                                                                "nucleusGroupStatus_": 1,
                                                                "insureNo_": "",
                                                                "purchaseOrderNo_": "",
                                                                "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                                                "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123','HD0100124']),
                                                                "pics_": ""
                                                                }]
                                            },
                                    "expect":"OK",
                                    "actual":""
                                 },
                                {
                                    "title": "批量新增-新增失败",
                                    "data": {
                                        "purchaseOrderNo_": 158,
                                        "jsonStr_": [{
                                            "cattleEarTagNo_": None,
                                            "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                                            "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                                            "gender_": random.choice([1001, 1003, 1002]),
                                            "birthday_": 1579453179000,
                                            "entryDate_": 1611075579000,
                                            "currentChildTime_": "",
                                            "birthWeight_": 259.99,
                                            "feedType_": random.choice(["繁育", "育肥"]),
                                            "fatherNo_": "F001",
                                            "motherNo_": "M001",
                                            "rfidCode_": "RF-" + str(random.randint(0, 9)),
                                            "nucleusGroupStatus_": 1,
                                            "insureNo_": "",
                                            "purchaseOrderNo_": "",
                                            "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                            "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                                            "pics_": ""
                                        },
                                            {
                                            "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                                            "cattleFenceId_": None,
                                            "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                                            "gender_": random.choice([1001, 1003, 1002]),
                                            "birthday_": 1579453179000,
                                            "entryDate_": 1611075579000,
                                            "currentChildTime_": "",
                                            "birthWeight_": 259.99,
                                            "feedType_": random.choice(["繁育", "育肥"]),
                                            "fatherNo_": "F001",
                                            "motherNo_": "M001",
                                            "rfidCode_": "RF-" + str(random.randint(0, 9)),
                                            "nucleusGroupStatus_": 1,
                                            "insureNo_": "",
                                            "purchaseOrderNo_": "",
                                            "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                            "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                                            "pics_": ""}]
                                    },
                                    "expect": "OK",
                                    "actual": ""
                                },
                                {"title": "批量新增-失败入参和成功入参混合",
                                    "data": {
                                        "purchaseOrderNo_": None,
                                        "jsonStr_": [{
                                            "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                                            "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                                            "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                                            "gender_": random.choice([1001, 1003, 1002]),
                                            "birthday_": 1579453179000,
                                            "entryDate_": 1611075579000,
                                            "currentChildTime_": "",
                                            "birthWeight_": 259.99,
                                            "feedType_": random.choice(["繁育", "育肥"]),
                                            "fatherNo_": "F001",
                                            "motherNo_": "M001",
                                            "rfidCode_": "RF-" + str(random.randint(0, 9)),
                                            "nucleusGroupStatus_": 1,
                                            "insureNo_": "",
                                            "purchaseOrderNo_": "",
                                            "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                            "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                                            "pics_": ""
                                        },
                                            {
                                            "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                                            "cattleFenceId_": None,
                                            "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                                            "gender_": random.choice([1001, 1003, 1002]),
                                            "birthday_": 1579453179000,
                                            "entryDate_": 1611075579000,
                                            "currentChildTime_": "",
                                            "birthWeight_": 259.99,
                                            "feedType_": random.choice(["繁育", "育肥"]),
                                            "fatherNo_": "F001",
                                            "motherNo_": "M001",
                                            "rfidCode_": "RF-" + str(random.randint(0, 9)),
                                            "nucleusGroupStatus_": 1,
                                            "insureNo_": "",
                                            "purchaseOrderNo_": "",
                                            "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                            "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                                            "pics_": ""}]
                                    },
                                    "expect": "OK",
                                    "actual": ""},
                                {
                                    "title": "批量新增-RFID值相同",
                                    "data": {
                                        "purchaseOrderNo_": None,
                                        "jsonStr_": [{
                                            "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                                            "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                                            "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                                            "gender_": random.choice([1001, 1003, 1002]),
                                            "birthday_": 1579453179000,
                                            "entryDate_": 1611075579000,
                                            "currentChildTime_": "",
                                            "birthWeight_": 259.99,
                                            "feedType_": random.choice(["繁育", "育肥"]),
                                            "fatherNo_": "F001",
                                            "motherNo_": "M001",
                                            "rfidCode_": "RF-" + str(999),
                                            "nucleusGroupStatus_": 1,
                                            "insureNo_": "",
                                            "purchaseOrderNo_": "",
                                            "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                            "usedNo_": random.choice(
                                                ['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                                            "pics_": ""
                                        },
                                            {
                                                "cattleEarTagNo_": "EB" + str(1616402101000 + random.randint(0, 99)),
                                                "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                                                "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                                                "gender_": random.choice([1001, 1003, 1002]),
                                                "birthday_": 1579453179000,
                                                "entryDate_": 1611075579000,
                                                "currentChildTime_": "",
                                                "birthWeight_": 259.99,
                                                "feedType_": random.choice(["繁育", "育肥"]),
                                                "fatherNo_": "F001",
                                                "motherNo_": "M001",
                                                "rfidCode_": "RF-" + str(999),
                                                "nucleusGroupStatus_": 1,
                                                "insureNo_": "",
                                                "purchaseOrderNo_": "",
                                                "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                                "usedNo_": random.choice(['HD0100120', 'HD0100121', 'HD0100122', 'HD0100123', 'HD0100124']),
                                                "pics_": ""}]
                                    },
                                    "expect": "ERROR",
                                    "actual": ""

                                }
                              ]
    admin_cattle_edit = [
                            {
                                "title":"牛只编辑-正常编辑",
                                "data":
                                        {
                                        "cattleFenceId_":1,
                                        "variety_":random.choice([1000,1001,1002,1003,1004,1005,1006,1007]),
                                        "gender_":random.choice([1001,1003]),
                                        "birthday_":1579453179000,
                                        "entryDate_":1611075579000,
                                        "currentChildTime_":"",
                                        "birthWeight_":259.99,
                                        "feedType_":10004,
                                        "fatherNo_":"F001",
                                        "motherNo_":"M001",
                                        "nucleusGroupStatus_":1,
                                        "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                        "usedNo_": random.choice(['HD0100120','HD0100121','HD0100122','HD0100123','HD0100124']),
                                        "insureNo_":"",
                                        "pics_":json.dumps([{"bizType":1,"url":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2013274768,216829781&fm=26&gp=0.jpg"}])
                                        },
                                "expect":"OK",
                                "actual":""
                            },
                            {
                                "title": "牛只编辑-修改不可编辑项(时间)",
                                "data":
                                    {
                                        "cattleFenceId_": Bullpen().get_cattle_fence()[0]['id'],
                                        "variety_": random.choice([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]),
                                        "gender_": random.choice([1001, 1003]),
                                        "birthday_": 916765179000,
                                        "entryDate_": 948301179000,
                                        "currentChildTime_": "",
                                        "birthWeight_": 259.99,
                                        "feedType_": 10004,
                                        "fatherNo_": "F001",
                                        "motherNo_": "M001",
                                        "nucleusGroupStatus_": 1,
                                        "skuCode_": Bullpen().get_product_category_mapping()[0]['sku_code'],
                                        "usedNo_":random.choice(['HD0100120','HD0100121','HD0100122','HD0100123','HD0100124']),
                                        "insureNo_": None ,
                                        "pics_": json.dumps([{"bizType":1,"url":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2013274768,216829781&fm=26&gp=0.jpg"}])
                                    },
                                "expect": "ERROR",
                                "actual": ""
                            }
    ]
    admin_cattle_list = [
                            {
                                "title":"默认查询所有",
                                "data":{
                                    "pn_":None,
                                    "ps_":None,
                                    "cattleEarTagNo_": None,
                                    "cowshedId_" : None,
                                    "cattleFenceId_" : None,
                                    "nucleusGroupStatus_" : None,
                                    "gender_" : None,
                                    "inGroupStatus_" : None,
                                    "variety_" : None,
                                    "currentChildTime_" : None,
                                    "startEntryDate_" : None,
                                    "endEntryDate_" : None,
                                    "startDepartureDate_" : None,
                                    "endDepartureDate_" : None

                                },
                                "expect":"OK",
                                "actual":""
                            },
                            {"title":"条件查询",
                                "data":{
                                    "pn_":None,
                                    "ps_":None,
                                    "cattleEarTagNo_": None,
                                    "cowshedId_" : None,
                                    "cattleFenceId_" : None,
                                    "nucleusGroupStatus_" : None,
                                    "gender_" : None,
                                    "inGroupStatus_" : 1,
                                    "variety_" : 1003,
                                    "currentChildTime_" : None,
                                    "startEntryDate_" : None,
                                    "endEntryDate_" : None,
                                    "startDepartureDate_" : None,
                                    "endDepartureDate_" : None

                                },
                                "expect":"OK",
                                "actual":""}
                         ]



if __name__ == '__main__':
    print(bullpen_case().admin_cattle_edit)


