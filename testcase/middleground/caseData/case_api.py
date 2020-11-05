
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


class api_data:
    admin_sku_add = [

        {"title": "新增商品", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class1": "F14",
                "class2": "F1402",
                "class3": "F140201",
                "brandId": "1",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "MONTH",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "kg",
                "baseUnit": "kg",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "OK"},
        {"title": "商品名字>30个字符", "data":
            {
                "name": '是具有数据操纵和数据定义等多种功能的数据库语言是具有数据操纵和数据定义等',
                "alias": Random().create_name(),
                "class1": "F14",
                "class2": "F1402",
                "class3": "F140201",
                "brandId": "31",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "MONTH",
                "netWeight": "48",
                "grossWeight": "50",
                "weightUnit": "kg",
                "baseUnit": "ge",
                "isSale": "0",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "商品短名>30个字符", "data":
            {
                "name": Random().create_name(),
                "alias": '还可以作为子语言为其他程序设计提供有效助力该程序应用中SQL可与其他程序语言一起优化程序功能',
                "class1": "F14",
                "class2": "F1402",
                "class3": "F140201",
                "brandId": "31",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "MONTH",
                "netWeight": "50",
                "grossWeight": "53",
                "weightUnit": "g",
                "baseUnit": "g",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "一级分类不填", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class1": "",
                "class2": "T0101",
                "class3": "T010101",
                "brandId": "31",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "MONTH",
                "netWeight": "50",
                "grossWeight": "52",
                "weightUnit": "kg",
                "baseUnit": "kg",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "二级分类不填", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class1": "T01",
                "class2": "",
                "class3": "T010101",
                "brandId": "1",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "5",
                "validityUnit": "YEAR",
                "netWeight": "50",
                "grossWeight": "58",
                "weightUnit": "t",
                "baseUnit": "t",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "三级分类不填", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class1": "T01",
                "class2": "T0101",
                "class3": "",
                "brandId": "31",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "DAY",
                "netWeight": "50",
                "grossWeight": "55",
                "weightUnit": "g",
                "baseUnit": "g",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "短名字不填", "data":
            {
                "name": Random().create_name(),
                "alias": None,
                "class1": "T01",
                "class2": "T0101",
                "class3": "T010101",
                "brandId": "31",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "DAY",
                "netWeight": "50",
                "grossWeight": "57",
                "weightUnit": "g",
                "baseUnit": "g",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "名字不填", "data":
            {
                "name": None,
                "alias": Random().create_name(),
                "class1": "T01",
                "class2": "T0101",
                "class3": "T010101",
                "brandId": "31",
                "basicCost": "100",
                "minimumPrice": "150",
                "marketPrice": "210",
                "validity": "365",
                "validityUnit": "DAY",
                "netWeight": "500",
                "grossWeight": "5050",
                "weightUnit": "kg",
                "baseUnit": "kg",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "分类不存在", "data":
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
         "expect": "ERROR"},
        {"title": "价格＜0", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "F1402",
                "class1": "F14",
                "class3": "F140201",
                "brandId": '31',
                "basicCost": -1,
                "minimumPrice": -1,
                "marketPrice": -1,
                "validity": "365",
                "validityUnit": "DAY",
                "netWeight": "50",
                "grossWeight": "56",
                "weightUnit": "kg",
                "baseUnit": "kg",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "价格参数非Int", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "F1402",
                "class1": "F14",
                "class3": "F140201",
                "brandId": '31',
                "basicCost": 'hello',
                "minimumPrice": 'hello',
                "marketPrice": 'hello',
                "validity": "365",
                "validityUnit": "DAY",
                "netWeight": "50",
                "grossWeight": "55",
                "weightUnit": "kg",
                "baseUnit": "kg",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "价格为空", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '31',
                "basicCost": None,
                "minimumPrice": None,
                "marketPrice": None,
                "validity": "365",
                "validityUnit": "DAY",
                "netWeight": "50",
                "grossWeight": "55",
                "weightUnit": "g",
                "baseUnit": "g",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "保质期空", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "T0101",
                "class1": "T01",
                "class3": "T010101",
                "brandId": '31',
                "basicCost": 120,
                "minimumPrice": 140,
                "marketPrice": 170,
                "validity": None,
                "validityUnit": "DAY",
                "netWeight": "50",
                "grossWeight": "55",
                "weightUnit": "g",
                "baseUnit": "g",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"},
        {"title": "品牌为空", "data":
            {
                "name": Random().create_name(),
                "alias": Random().create_name(),
                "class2": "F1402",
                "class1": "F14",
                "class3": "F140201",
                "brandId": None,
                "basicCost": 120,
                "minimumPrice": 140,
                "marketPrice": 170,
                "validity": 365,
                "validityUnit": "DAY",
                "netWeight": "50",
                "grossWeight": "55",
                "weightUnit": "g",
                "baseUnit": "g",
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            },
         "expect": "ERROR"}

    ]
    admin_sku_page_list = [
        # {"title": "查商品SKU分页",
        #  "data": {"pn": 1, "ps": 50,"skuCode":"T0101010061","name":"CSS末世29"},
        #  "expected": "OK"},
        # {"title": "SKU编码为空",
        #  "data": {"pn": 1, "ps": 50,"skuCode":"T0101010062","name":"CSS末世29"},
        #  "expected": "OK"},
        {"title": "传入负值",
         "data": {"pn": 1, "ps": 50, "skuCode": "T0101010062", "name": "CSS末世29"},
         "expected": "OK"}
    ]

    admin_label_add_data = [
        {"title": "新增type为0的标签", "data": {"name": Random().create_name(), "type": 0}, "expected": "OK"},
        {"title": "新增type为1的标签", "data": {"name": Random().create_name(), "type": 1}, "expected": "OK"},
        {"title": "新增type为2的标签", "data": {"name": Random().create_name(), "type": 2}, "expected": "OK"},
        {"title": "新增type为3的标签", "data": {"name": Random().create_name(), "type": 3}, "expected": "OK"},
        {"title": "新增type为4的标签", "data": {"name": Random().create_name(), "type": 4}, "expected": "OK"},
        {"title": "新增type为5的标签", "data": {"name": Random().create_name(), "type": 5}, "expected": "OK"},
        {"title": "新增type为-1的标签", "data": {"name": Random().create_name(), "type": -1}, "expected": "OK"},
        {"title": "新增type为0的标签", "data": {"name": "建议须谨慎看待大陆军事动态保持高度警觉并作适当反应", "type": 9}, "expected": "ERROR"},
        {"title": "新增名字为空", "data": {"name": None, "type": -1}, "expected": "ERROR"},
        {"title": "新增类型为空", "data": {"name": Random().create_name(), "type": None}, "expected": "ERROR"},
        {"title": "新增名字为空格", "data": {"name": "      ", "type": 0}, "expected": "ERROR"}
    ]
    admin_label_change_status_data = [
        {"title": "启用标签", "data": {"id_": "50", "status_": "1"}, "expected": "OK"},
        {"title": "禁用标签", "data": {"id_": "50", "status_": "2"}, "expected": "OK"}
        # {"title": "异常值0", "data": {"id_": "50","status_":"0"},"expected":"ERROR"},
        # {"title": "异常值3", "data": {"id_": "50", "status_":"3"},"expected":"ERROR"},
        # {"title": "异常值-1", "data": {"id_": "50", "status_":"-1"},"expected":"ERROR"}
    ]
    admin_label_list_by_type = [
        {"title": "查已启用", "data": {"type": "1", "status": "1"}, "expected": "OK"},
        {"title": "查已禁用", "data": {"type": "1", "status": "2"}, "expected": "OK"},
        {"title": "异常值", "data": {"type": None, "status": None}, "expected": "ERROR"},
        {"title": "异常值", "data": {"type": "#￥%", "status": "1"}, "expected": "ERROR"}

    ]

    admin_shop_add = [
        {"title": "新增店铺",
         "data":
             {"name": Random().create_name(), "remark": "本店专门营销什么什么商品，假一罚十信誉保证。本店的服务宗旨是用心服务，以诚待人!"}
            , "expected": "OK"},
        {"title": "店铺名超过20字符",
         "data": {"name": "本店所有的商品照片为专业摄影师拍摄后期精心修制及色彩调整", "remark": "本店专门营销什么什么商品，假一罚十信誉保证。"}
            , "expected": "ERROR"},
        {"title": "店铺说明超过20字符",
         "data": {"name": Random().create_name(),
                  "remark": "本店所有的商品照片为专业摄影师拍摄，后期精心修制及色彩调整，尽量与实际商品保持一致，但由于拍摄时用光、角度、显示器色彩偏差、个人对颜色的认知等方面的差异，导致实物可能会与照片存在一些色差，最终颜色以实际商品为准。请在购买前与我们客服充分沟通后做出慎重选择。色差问题将不被我们认可当退换货的理由!"}
            , "expected": "ERROR"},
        {"title": "店铺名称为空",
         "data": {"name": None, "remark": "本店专门营销什么什么商品，假一罚十信誉保证。本店的服务宗旨是用心服务，以诚待人!"}
            , "expected": "ERROR"},
        {"title": "店铺说明为空",
         "data": {"name": Random().create_name(), "remark": None}
            , "expected": "ERROR"}
    ]
    admin_shop_edit = [
        {"title": "修改店铺信息",
         "data":
             {"name": Random().create_name(), "remark": "一间芝麻大的小铺 八仙过海各抒己见", "isDelete_": 0}
            , "expected": "OK"},
        {"title": "修改名字＞20",
         "data":
             {"name": "五月终可开张经营百分热情双倍才行千挑万选献上宝贝", "remark": "一间芝麻大的小铺 八仙过海各抒己见哈哈", "isDelete_": 0}
            , "expected": "ERROR"},
        {"title": "名字为空",
         "data":
             {"name": None, "remark": "一间芝麻大的小铺 八仙过海各抒己见", "isDelete_": 0}
            , "expected": "ERROR"},
        {"title": "说明为空",
         "data":
             {"name": Random().create_name(), "remark": None, "isDelete_": 0}
            , "expected": "ERROR"}

    ]
    admin_shop_delete = [{"title": "删除店铺", "data": {"isDelete_": 1}, "expected": "OK"},
                   {"title": "删除店铺", "data": {"isDelete_": 0}, "expected": "ERROR"}
                   ]

    admin_inventory_add = [
        {"title": "新增库存", "data": {"skuId_": "143", "skuCode_": "T0101010001", "quantity_": 20000}, "expected": "OK"},
        {"title": "新增库存", "data": {"skuId_": "145", "skuCode_": "T0101010002", "quantity_": 20000}, "expected": "OK"},
        {"title": "库存为负", "data": {"skuId_": "143", "skuCode_": "T0101010001", "quantity_": -10000},
         "expected": "ERROR"},
        {"title": "库存为空", "data": {"skuId_": "143", "skuCode_": "T0101010001", "quantity_": None}, "expected": "ERROR"},
        {"title": "ID为空", "data": {"skuId_": None, "skuCode_": "T0101010001", "quantity_": 30000}, "expected": "ERROR"},
        {"title": "code为空", "data": {"skuId_": "143", "skuCode_": None, "quantity_": 30000}, "expected": "ERROR"}
    ]
    admin_inventory_update = [
        {"title": "修改库存", "data": {"skuCode": "T0101010001", "quantity": 30000}, "expected": "OK"},
        {"title": "修改库存-为负", "data": {"skuCode": "T0101010001", "quantity": -30000}, "expected": "ERROR"},
        {"title": "修改库存-为空", "data": {"skuCode": "T0101010001", "quantity": None}, "expected": "ERROR"}
    ]
    admin_inventory_list = [
        {"title": "修改库存-为空", "data": {"pn": 1, "ps": 5, "skuCode": "T0101010001", "skuName": "追"}, "expected": "OK"}
    ]

    admin_biz_add = [

        {"title": "业务新增", "data": {"ruleName_": Random().create_name()}, "expect": "OK"},
        {"title": "业务新增-为空", "data": {"ruleName_": None}, "expect": "ERROR"},
        {"title": "业务新增-为int", "data": {"ruleName_": 8888}, "expect": "ERROR"},
        {"title": "业务新增-长度>20", "data": {"ruleName_": "具有某种特征的人典型属于苹果手机山东新增本地确诊病例1例类型的具特征的"}, "expect": "ERROR"},
        # {"title":"业务新增-符号","data":{"ruleName_":'******'},"expect":"ERROR"},
        {"title": "业务新增-空格", "data": {"ruleName_": "      "}, "expect": "ERROR"}
    ]
    admin_biz_change_status = [
        {"title": "业务启用", "data": {"id": 1, "status": 1}, "expect": "OK"},
        {"title": "业务禁用", "data": {"id": 1, "status": 2}, "expect": "OK"},
        {"title": "业务ID为空", "data": {"id": None, "status": ""}, "expect": "ERROR"},
        {"title": "业务status为空", "data": {"id": '', "status": None}, "expect": "ERROR"}

    ]
    admin_biz_list_enable = [

        {"title": "业务分页", "data": {"pn": 1, "ps": 20}, "expect": "OK"},
        {"title": "业务分页-异常值", "data": {"pn": '搞笑', "ps": '小品'}, "expect": "ERROR"}

    ]

    admin_brand_add = [

        {"title": "新增品牌", "data": {"name": Random().create_name(),
                                   "logo": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1767448974,2051103783&fm=26&gp=0.jpg"},
         "expect": "OK"},
        {"title": "新增品牌", "data": {"name": Random().create_name(),
                                   "logo": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3112097844,4213331226&fm=26&gp=0.jpg"},
         "expect": "OK"},
        {"title": "新增品牌", "data": {"name": Random().create_name(),
                                   "logo": "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2196976096,3047104416&fm=26&gp=0.jpg"},
         "expect": "OK"},
        {"title": "新增品牌", "data": {"name": Random().create_name(),
                                   "logo": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2013274768,216829781&fm=26&gp=0.jpg"},
         "expect": "OK"}

    ]
    admin_brand_status = [
        {"title": "禁用品牌", "data": {"status": 2}, "expect": "OK"},
        {"title": "启用品牌", "data": {"status": 1}, "expect": "OK"},
        {"title": "状态传空", "data": {"status": None}, "expect": "ERROR"}

    ]
    admin_brand_edit = [
        {"title": "修改品牌名字", "data": {"name": Random().create_name()}, "expect": "OK"},
        {"title": "修改品牌-名字传空", "data": {"name": None}, "expect": "ERROR"},
        {"title": "修改品牌-字符>20个", "data": {"name": "意大利西西里岛的萨莱米市计划出售套房屋的售价仅相当于一个汉堡的价格"}, "expect": "ERROR"}
    ]