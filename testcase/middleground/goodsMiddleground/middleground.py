from utils.log import log
import time
import random
import warnings
import json
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import mp_label as goods_mp
from testcase.middleground.sql.brandMP import mp_label as brand_mp
from testcase.middleground.sql.shopMP import mp_label as shop_mp
from testcase.middleground.sql.sku_inventoryMP import mp_label as sku_mp
from testcase.middleground.caseData.case_data import middleground_data
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest


class Context:
    bizId = ''
    brandId = ''
    skuId = ''
    skuCode = ''




@ddt
class Flow_Path(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expect = sku_mp().git_sku_add(2)

    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.goods_db = goods_mp()
        self.brand_db = brand_mp()
        self.shop_db = shop_mp()
        self.faker = Faker('zh_CN')
        self.expect = sku_mp().git_sku_add(2)  # 先查出sku表中所有的数据条数
    # 新增一个品牌
    @data(*middleground_data().test_brand_add)
    def test_4_brand_add(self,case):
        name_ = case['name']
        logo_ = case['logo']
        res = self.api._admin_brand_add(name_=name_,logo_=logo_)
        self.assertEqual('OK',res.get('status'))
        if res.get('status') == 'OK':
            # 将新增的品牌id存起来，新增商品SKU 的时候使用
            setattr(Context,'brandId',self.brand_db.git_admin_brand_add()[0]['id'])

    # 新增一个业务类型
    @data(*middleground_data().test_biz_add)
    def test_1_biz_add(self,case):
        ruleName_ = case['ruleName']
        res = self.api._admin_biz_add(ruleName_=ruleName_)
        self.assertEqual('OK',res.get('status'))
        if res.get('status') == 'OK':
            self.assertEqual(self.brand_db.git_admin_biz_add()[0]['name'],case['ruleName'])
            setattr(Context,'bizId',self.brand_db.git_admin_biz_add()[0]['id'])
        else:
            self.assertEqual(res.get('status'), 'ERROR')
    # 新增类目,类目需要用到 业务类型接口返回的id
    @data(*middleground_data().test_category_add)
    def test_3_category_add(self,case):
        bizId_ = getattr(Context,'bizId')
        pcode_ = case['pcode']
        name_ = case['name']
        isSale_ = case['isSale']
        remark_ = case['remark']
        res = self.api._admin_category_add(bizId_=bizId_,pcode_=pcode_,name_=name_,isSale_=isSale_,remark_=remark_)
        self.assertEqual('OK',res.get('status'))
        if res.get('status') == 'OK':
            self.assertEqual(self.goods_db.query_mp_product_category()[0]['biz_id'],bizId_)
            self.assertEqual(self.goods_db.query_mp_product_category()[0]['name'],name_)
        else:
            self.assertEqual('ERROR', res.get('status'))

    #新增号段，号段需要用到 业务类型接口返回的id
    @data(*middleground_data().test_section_add)
    def test_2_section_add(self,case):
        prefix_ = case['prefix_'] # 号段是写死的，最大只能用99次，如果出现了"业务线无可用号段，就去修改case数据中的F为其他字母"
        bizId_ = getattr(Context,'bizId')
        num = case['num_']
        res = self.api._admin_section_add(prefix_=prefix_,bizId_=bizId_,num_=num)
        self.assertEqual('OK',res.get('status'))
        if res.get('status') == 'OK':
            self.assertEqual(self.brand_db.git_admin_section_add()[0]['biz_id'],bizId_)
            self.assertEqual(self.brand_db.git_admin_section_add()[0]['prefix'],prefix_)
        else:
            self.assertEqual('ERROR', res.get('status'))

    #新增商品规格/属性
    @data(*middleground_data().test_admin_attr_add)
    def test_5_admin_attr_add(self,case):
        attrName_ = case['attrName']
        isSale_ = case['isSale']
        res = self.api._admin_attr_add(attrName_=attrName_,isSale_=isSale_)
        self.assertEqual('OK',res.get('status'))
        if res.get('status') == 'OK':
            self.assertEqual(self.brand_db.git_admin_attr_name()[0]['name'],attrName_)
            self.assertEqual(self.brand_db.git_admin_attr_name()[0]['is_sale'],isSale_)
        else:
            self.assertEqual('ERROR', res.get('status'))
            self.assertNotEqual(self.brand_db.git_admin_attr_name()[0]['name'],attrName_)
    # 新增商品标签
    @data(*middleground_data().test_label_add)
    def test_6_label_add(self,case):
        name_ = case['name']
        type_ = case['type']
        res = self.api._admin_label_add(name_=name_,type_=type_)
        self.assertEqual('OK',res.get('status'))
        if res.get('status') == 'OK':
            self.assertEqual(self.brand_db.git_admin_label()[0]['name'],name_)
            self.assertEqual(self.brand_db.git_admin_label()[0]['type'],type_)
        else:
            self.assertNotEqual(self.brand_db.git_admin_label()[0]['name'],name_)


    # # 新增商品SKU
    @data(*middleground_data().test_sku_add)
    def test_admin_sku_add(self, case):
        name = case['name']
        alias = case['alias']
        class1 = case['class1']
        class2 = case['class2']
        class3 = case['class3']
        brandId = case['brandId']
        basicCost = case['basicCost']
        minimumPrice = case['minimumPrice']
        marketPrice = case['marketPrice']
        validity = case['validity']
        validityUnit = case['validityUnit']
        netWeight = case['netWeight']
        grossWeight = case['grossWeight']
        weightUnit = case['weightUnit']
        baseUnit = case['baseUnit']
        isSale = case['isSale']
        basicAttr = case['basicAttr']
        saleAttr = case['saleAttr']

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
        self.assertEqual('OK',resp.get('status'))
        if resp.get('status') == 'OK':
            for i in self.expect:
                for value in i.values():
                    self.expect  = value

            self.assertEqual(self.expect + 1 ,sku_mp().git_sku_add(2)[0]['count(*)'])
    # 新增库存，新增库存需要用到商品skuID
    # @data(*middleground_data().test_inventory_add)
    # def test_inventory_add(self):
    #     res = self.api._admin_inventory_add(skuId_=None,skuCode_=None,quantity_=None)


if __name__ == '__main__':
    unittest.main()