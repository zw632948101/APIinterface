from testcase.beefcattle.sql.Bullpen_sql import Bullpen
import random


class bullpen_case:
    admin_cattle_add = [
        {
            "title":"牛只信息-正常新增",
            "data":
                    {
                        "cattleEarTagNo_":int(Bullpen().get_cattle()[0]['cattle_ear_tag_no']) + 1,
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
        }
    ]