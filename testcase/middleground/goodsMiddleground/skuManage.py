from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.brandMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest



class tagMdata(object):
    def __init__(self):
        super(tagMdata, self).__init__()
        self.faker = Faker('zh_CN')

    def add_label_data(self):
        """
        添加标签数据
        :return:
        """
        ldata = [None, self.faker.text(21), self.faker.text(20), self.faker.text(20), self.faker.text(20)]
        ltype = [1, 1, '1', None, self.faker.text(10)]
        label_data = [list(i) for i in zip(ldata, ltype)]
        return label_data

class Random:
    # 随机名字
    def create_name(self):
        xs = ["yexin_",
              "Tom_",
              "Mary_",
              "Crazy_",
              "Python_",
              "Java_",
              "PHP",
              "javascpit",
              "CSS",
              "html",
              "XLMX",
              "sql",
              "Ruby",
              "Go",
              "Swift"
              ]
        mz = ["默然",
              "旅人",
              "多余",
              "云中",
              "残雪",
              "末世",
              "桑榆",
              "扉匣",
              ]
        sj = time.strftime('%S', time.localtime(time.time())) # 获取当前时间秒

        name = random.choice(xs) + random.choice(mz) + sj
        return name


class sku_data:
    admin_sku_add = [

        {"title":"新增商品","data":
            {
                "name":Random().create_name(),
                "alias":Random().create_name(),
                "class1":"T01",
                "class2":"T0101",
                "class3":"T010101",
                "brandId":"1",
                "basicCost":"100",
                "minimumPrice":"150",
                "marketPrice":"210",
                "validity":"365",
                "validityUnit":"2021-10-30",
                "netWeight":"50",
                "grossWeight":"50",
                "weightUnit":"5",
                "baseUnit":"ge",
                "isSale":"1",
                "basicAttr":"",
                "saleAttr":""
            },
         "expect":""},
        {"title":"商品名字>30个字符","data":
            {
                "name": '是具有数据操纵和数据定义等多种功能的数据库语言是具有数据操纵和数据定义等',
                "alias": Random().create_name(),
                "class1": "T01",
                "class2": "T0101",
                "class3": "T010101",
                "brandId": "1",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "2021-10-30",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect":""},
        {"title": "商品短名>30个字符","data":
            {
                "name": Random().create_name(),
                "alias": '还可以作为子语言为其他程序设计提供有效助力该程序应用中SQL可与其他程序语言一起优化程序功能',
                "class1": "T01",
                "class2": "T0101",
                "class3": "T010101",
                "brandId": "1",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "2021-10-30",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "一级分类不填","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class1": "",
                "class2": "T0101",
                "class3": "T010101",
                "brandId": "1",
                "basicCost": "1000",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "2021-10-30",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "二级分类不填","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class1": "T01",
                "class2": "",
                "class3": "T010101",
                "brandId": "1",
                "basicCost": "1000",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "三级分类不填","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class1": "T01",
                "class2": "T0101",
                "class3": "",
                "brandId": "1",
                "basicCost": "1000",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "短名字不填","data":
            {
                "name": Random().create_name(),
                "alias": "",
                "class1": "T01",
                "class2": "T0101",
                "class3": "T010101",
                "brandId": "1",
                "basicCost": "1000",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "名字不填","data":
            {
                "name": "",
                "alias": Random().create_name(),
                "class1": "T01",
                "class2": "T0101",
                "class3": "T010101",
                "brandId": "1",
                "basicCost": "1000",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "分类不存在","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "99999999999999",
                "class1": "88888888888888",
                "class3": "77777777777777",
                "brandId": "1",
                "basicCost": "1000",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "价格＜0","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": -1,
                "minimumPrice": -1,
                "marketPrice": -1,
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "价个＞1亿","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": 1000000000.00,
                "minimumPrice": 1000000000.00,
                "marketPrice": 1000000000.00,
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "价格为空","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": None,
                "minimumPrice": None,
                "marketPrice": None,
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "市场价＜最低销售价","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": 100,
                "minimumPrice": 150,#最低售价
                "marketPrice": 110,#市场价
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "最低售价＜成本价","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": 100,#成本价
                "minimumPrice": 50,#最低售价
                "marketPrice": 110,#市场价
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "市场价＜成本价","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": 100,#成本价
                "minimumPrice": 150,#最低售价
                "marketPrice": 50,#市场价
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "重量单位＜0","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": 100,#成本价
                "minimumPrice": 150,#最低售价
                "marketPrice": 200,#市场价
                "validity": "365",
                "validityUnit": "1949-10-1",
                "netWeight": -1,
                "grossWeight": -2,
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "保质期＜0","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": 100,#成本价
                "minimumPrice": 150,#最低售价
                "marketPrice": 200,#市场价
                "validity": -1,
                "validityUnit": "1949-10-1",
                "netWeight": 100,
                "grossWeight": 300,
                "weightUnit": "5",
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""},
        {"title": "重量单位传入厘米","data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '1',
                "basicCost": 100,#成本价
                "minimumPrice": 150,#最低售价
                "marketPrice": 200,#市场价
                "validity": -1,
                "validityUnit": "1949-10-1",
                "netWeight": 100,
                "grossWeight": 300,
                "weightUnit": '5cm',
                "baseUnit": "ge",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": ""}
    ]
    admin_sku_page_list = [
        # {"title": "查商品SKU分页",
        #  "data": {"pn": 1, "ps": 50,"skuCode":"T0101010061","name":"CSS末世29"},
        #  "expected": "OK"},
        # {"title": "SKU编码为空",
        #  "data": {"pn": 1, "ps": 50,"skuCode":"T0101010062","name":"CSS末世29"},
        #  "expected": "OK"},
        {"title": "传入负值",
         "data": {"pn": -1, "ps": -50,"skuCode":"T0101010062","name":"CSS末世29"},
         "expected": "OK"}
    ]


@ddt
class skuManage(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')


    @data(*sku_data().admin_sku_add)
    def test_admin_sku_add(self,case):
        name = case['data']['name']
        alias = case['data']['alias']
        class1 = case['data']['class1']
        class2 = case['data']['class2']
        class3 = case['data']['class3']
        brandId = case['data']['brandId']
        basicCost = case['data']['basicCost']
        minimumPrice = case['data']['minimumPrice']
        marketPrice = case['data']['marketPrice']
        validity = case['data']['validity']
        validityUnit = case['data']['validityUnit']
        netWeight = case['data']['netWeight']
        grossWeight = case['data']['grossWeight']
        weightUnit = case['data']['weightUnit']
        baseUnit = case['data']['baseUnit']
        isSale = case['data']['isSale']
        basicAttr = case['data']['basicAttr']
        saleAttr = case['data']['saleAttr']

        resp = self.api._admin_sku_add(name_=name,
                                       alias_=alias,
                                       class1_=class1,
                                       class2_=class2,
                                       class3_=class3,
                                       brandId_=brandId,
                                       basicCost_=basicCost,
                                       minimumPrice_=minimumPrice,
                                       marketPrice_=marketPrice,
                                       validity_=validity,
                                       validityUnit_=validityUnit,
                                       netWeight_=netWeight,
                                       grossWeight_=grossWeight,
                                       weightUnit_=weightUnit,
                                       baseUnit_=baseUnit,
                                       isSale_=isSale,
                                       basicAttr_=basicAttr,
                                       saleAttr_=saleAttr)

    @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    @data(*sku_data().admin_sku_page_list)
    def test_admin_sku_page_list(self,case):
        pn = case['data']['pn']
        ps = case['data']['ps']
        skuCode = case['data']['skuCode']
        name = case['data']['name']
        resp = self.api._admin_sku_page_list(pn_=pn, ps_=ps, skuCode_=skuCode, name_=name)


if __name__ == '__main__':
    unittest.main()