import random
import time
from random import choice
class Random:
    # 随机名字
    def create_name(self):
        xs = ["桂","龙","荔","山","荆","校","洋","紫","桉","刺","向","巢","榨","浓缩","油","苕","橡","荞","春","棉"]
        mz = ["花蜜","眼蜜","枝蜜","条蜜","树蜜","英蜜","樨蜜","槐蜜","葵蜜","菜蜜","子蜜","胶蜜","麦蜜","瓜蜜","桔蜜","刺蜜","木蜜","橘蜜","桕蜜"]
        sj = time.strftime('%S', time.localtime(time.time())) # 获取当前时间秒
        name = random.choice(xs) + random.choice(mz) + sj
        return name
    def logo_list(self):
        form = ".jpg"
        logo = ["https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1767448974,2051103783&fm=26&gp=0",
                "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3112097844,4213331226&fm=26&gp=0",
                "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2196976096,3047104416&fm=26&gp=0",
                "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2013274768,216829781&fm=26&gp=0"]
        return choice(logo) + form



class middleground_data:

    test_brand_add = [{"name":Random().create_name(),"logo":Random().logo_list()},
                      ]
    test_biz_add = [{"ruleName":"蜂蜜汁"}
                    ]
    test_category_add = [{"bizId":None,"pcode":"","name":Random().create_name(),"isSale":1,"remark":"凡酿蜜蜂普天皆有"},
                         {"bizId":None,"pcode":"","name":Random().create_name(),"isSale":0,"remark":"凡酿蜜蜂普天皆有"},
                         {"bizId":None,"pcode":"F14","name":Random().create_name(),"isSale":1,"remark":"凡酿蜜蜂普天皆有"},
                         {"bizId":None,"pcode":"F1402","name":Random().create_name(),"isSale":1,"remark":"凡酿蜜蜂普天皆有"}]
    test_section_add = [{"prefix_":"F","bizId_":"","num_":99}
                        ]
    test_admin_attr_add = [
        {"title":"新增商品规格","attrName":Random().create_name(),"isSale":1},
        {"title":"新增商品属性","attrName":Random().create_name(),"isSale":0}
    ]
    test_label_add = [{"name":Random().create_name(),"type":1}
                      ]
    test_sku_add = [{"name":Random().create_name(),
                     "alias":Random().create_name(),
                     "class1":"F14", # 分类编码
                     "class2":"F1402",
                     "class3":"F140201",
                     "brandId":31, # 品牌id
                     "basicCost":100,
                     "minimumPrice":120,
                     "marketPrice":180,
                     "validity":24,
                     "validityUnit":"MONTH",
                     "netWeight":50,
                     "grossWeight":55,
                     "weightUnit":"g",
                     "baseUnit":"桶",
                     "isSale":1,
                     "airTransport":1,
                     "basicAttr":"",
                     "saleAttr":""}]
    test_inventory_add = [{"skuId":"","skuCode":"","quantity":1000},
                          ]

    test_product_push = [{"title":"同步至ERP","data":{"skus":["T0101020001","T0101020002","T0101010001","T0101010002","T0102010001","T0102020001","T0102020002","T0101010003","T0103010001","T0102020003","T0102010002"],"subjectCode":"1"},"expect":"OK"},
                         {"title":"sku不存在","data":{"skus":["0022222222222000"],"subjectCode":"1"},"expect":"ERROR"},
                         {"title":"Code不存在","data":{"skus":["T0101020001","T0101020002","T0101010001"],"subjectCode":None},"expect":"ERROR"}]
    test_product_sync = []
    test_product_list = [{"pn":"","ps":"","name":"","skuCode":"","status":""}]
    test_product_detail = []



if __name__ == '__main__':
    t = Random().logo_list()
    print(t)