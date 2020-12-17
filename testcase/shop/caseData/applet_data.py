import requests
from utils.log import log
import time
import random
import warnings
from interfaces.wxshop.MallAction import MallAction
#from testcase.middleground.sql.brandMP import mp_label as
from testcase.shop.sql.webMP import mp_label
from testcase.shop.caseData.os_path import evaluate_001,evaluate_002
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import requests



class applet_api:
    admin_web_cart_add = [{"title":"正常数量：","data":{"amount":"2"},"expect":"OK"},
                          {"title":"数量为空：","data":{"amount":None},"expect":"ERROR"},
                          {"title":"数量为负：","data":{"amount":-500},"expect":"ERROR"},
                          {"title":"购买数量超出库存：","data":{"amount":"100000000"},"expect":"ERROR"}
                         ]
    admin_web_cart_edit_amount = [{"title":"编辑购物车商品数量","data":{"id":"6","amount":"9"},"expect":"OK"},
                                  {"title":"编辑购物车数量为空","data":{"id":"6","amount":None},"expect":"ERROR"}
                                  ]

    admin_web_cart_balance = [{'title':'购物车结算','data':{"id":"6"},'expect':'OK'},
                        {'title':'结算id空','data':{"id":None},'expect':'ERROR'}]
    admin_web_cart_buy_again = [{"title":"再次购买","data":{"product":[{"skuNo":"10201010007","amount":"10"}],"shopId":"1"},"expect":"OK"},
                                {"title":"再次购买-库存不足","data":{"product":[{"skuNo":"10201010003","amount":"10"}],"shopId":"1"},"expect":"ERROR"},
                                {"title":"再次购买-商品下架","data":{"product":[{"skuNo":"10701030003","amount":"10"}],"shopId":"1"},"expect":"ERROR"},
                                {"title":"商品sku错误","data":{"product":[{"skuNo":"111111","amount":"10"}],"shopId":"1"},"expect":"ERROR"},
                                {"title":"店铺传空","data":{"product":[{"skuNo":"10201010007","amount":"10"}],"shopId":None},"expect":"ERROR"},
                                {"title":"商品传空","data":{"product":None,"shopId":"1"},"expect":"ERROR"}
                                ]

    admin_web_cart_purchase = [{"title":"加入购物车","data":{"skuNo":"T0101010001","shopId":"1","amount":"13"},"expect":"OK"}]

file_list = ["https://thumb22.jfcdns.com/thumb/up/2017-12/15135651876688413_460_380.jpg",
                 "https://goss.veer.com/creative/vcg/veer/800water/veer-133156216.jpg",
                 "https://p3.itc.cn/images03/20200521/022e648fea5148a9b93a99eb5d50d32c.jpeg",
                 "https://pic.9ht.com/up/2017-12/15135801979119688.jpg"]
class submit_order:
    cartId = ''
    web_order_close = [{"title":"取消订单","data":{"pn":"","ps":"","reason":"不想要了"},"expect":"OK"},
                       {"title":"原因为空","data":{"pn":"","ps":"","reason":None},"expect":"ERROR"}]
    web_order_detail = []
    web_order_list = []
    web_order_submit_order = [{"title":"下单",
                               "data":{"shopId":"1",
                                       "product":[],
                                       "addressId":"1",
                                       "freight":"0",
                                       "deliveryType":1,
                                       "productPrice":100,
                                       "buyerMemo":"尽快送达!"},
                               "expect":"OK"}]
    web_mobile_evaluate_order_add = [
                                     {"title":"评价内容＞200个字",
                                      "data":{"orderNo":"", # 取数据库中，order_status = 50的订单
                                              "serviceScore":4,
                                              "logisticsScore":4,
                                              "productEvaluateJson":[{"skuNo":mp_label().git_web_order_evaluate('蜂友708528')[0]['sku_no'],
                                                                      "productScore":4,
                                                                      "comment":"网购了这么多年，这是我第一次这么认真的对待。"
                                                                                "我怀着忐忑的心情拿着手机盯着屏幕，迟迟不敢下手。"
                                                                                "我怕我一旦说出来，老板会觉得我在拍马屁，是不是想为了那几块钱的红包，"
                                                                                "又怕我的评价会误导后来的网友。为了写这次评价，我鼓起勇气喝了3瓶啤酒才有信心。"
                                                                                "记得第一次喝酒还是对初恋表白的那天，今天又是同样的心情，拼了，为了不辜负老板对我的期望，"
                                                                                "我一定会客观，公正，如实的写下自己的评价：这是我这开心的一次网购，谢谢！！！",
                                                                      "urls":["https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959198373.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959204151.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959208558.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959210374.png"]}],
                                            },
                                      "expect":"ERROR"},
                                     {"title":"评价内容≤200个字",
                                      "data":{"orderNo":"",
                                              "serviceScore":4,
                                              "logisticsScore":4,
                                              "productEvaluateJson":[{"skuNo":mp_label().git_web_order_evaluate('蜂友708528')[0]['sku_no'],
                                                                      "productScore":4,
                                                                      "comment":"真的超级喜欢，非常支持，质量非常好，"
                                                                                "与卖家描述的完全一致，非常满意,"
                                                                                "真的很喜欢，完全超出期望值，发货速度非常快，"
                                                                                "包装非常仔细、严实，物流公司服务态度很好，运送速度很快，很满意的一次购物。",
                                                                      "urls":["https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959198373.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959204151.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959208558.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959210374.png"]}],
                                              },
                                      "expect":"OK"},
                                     {"title":"评价服务传空",
                                      "data":{"orderNo":"",
                                              "serviceScore":None,
                                              "logisticsScore": 4,
                                              "productEvaluateJson": [{"skuNo": mp_label().git_web_order_evaluate('蜂友708528')[0]['sku_no'],
                                                                       "productScore": 4,
                                                                       "comment": "真的超级喜欢，非常支持，质量非常好，"
                                                                                  "与卖家描述的完全一致，非常满意,"
                                                                                  "真的很喜欢，完全超出期望值，发货速度非常快，"
                                                                                  "包装非常仔细、严实，物流公司服务态度很好，运送速度很快，很满意的一次购物。",
                                                                       "urls": ["https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959198373.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959204151.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959208558.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959210374.png"]}],
                                             },
                                      "expect":"ERROR"},
                                     {"title": "评价物流传空",
                                      "data": {"orderNo": "",
                                               "serviceScore": 4,
                                               "logisticsScore": None,
                                               "productEvaluateJson": [{"skuNo": mp_label().git_web_order_evaluate('蜂友708528')[0]['sku_no'],
                                                                        "productScore": 4,
                                                                        "comment": "真的超级喜欢，非常支持，质量非常好，"
                                                                                   "与卖家描述的完全一致，非常满意,"
                                                                                   "真的很喜欢，完全超出期望值，发货速度非常快，"
                                                                                   "包装非常仔细、严实，物流公司服务态度很好，运送速度很快，很满意的一次购物。",
                                                                        "urls":["https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959198373.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959204151.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959208558.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959210374.png"]}],
                                               },
                                      "expect": "ERROR"},
                                     {"title": "评价商品传空",
                                      "data": {"orderNo": "",
                                               "serviceScore": 4,
                                               "logisticsScore": 4,
                                               "productEvaluateJson": [{"skuNo": mp_label().git_web_order_evaluate('蜂友708528')[0]['sku_no'],
                                                                        "productScore":None,
                                                                        "comment": "真的超级喜欢，非常支持，质量非常好，"
                                                                                   "与卖家描述的完全一致，非常满意,"
                                                                                   "真的很喜欢，完全超出期望值，发货速度非常快，"
                                                                                   "包装非常仔细、严实，物流公司服务态度很好，运送速度很快，很满意的一次购物。",
                                                                        "urls":["https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959198373.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959204151.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959208558.png",
                                                                              "https://dnkj-mp-oms-prod.oss-accelerate.aliyuncs.com/data/wx-mall/dev/1/1606959210374.png"]}],
                                               },
                                      "expect": "ERROR"}
                                     ]
    web_mobile_evaluate_order_audit = [{"title":"审核拒绝",
                                        "data":{"evaluateNo":"","status":3},
                                        "expect":"OK"},{"title":"审核通过",
                                        "data":{"evaluateNo":"","status":2},
                                        "expect":"OK"},{"title":"审核值-传负",
                                        "data":{"evaluateNo":"","status":-1},
                                        "expect":"ERROR"},{"title":"审核值-传空",
                                        "data":{"evaluateNo":"","status":None},
                                        "expect":"ERROR"}]
    web_mobile_evaluate_order_reply = [{"title":"","data":{"comment":"'感谢你的光顾，欢迎下次再来！"},"expect":"OK"},
                                       {"title":"","data":{"comment":None},"expect":"OK"}]
    web_favorite_add = [{"title":"商品收藏-加入收藏",
                         "data":{"skuNo":"T0101010001",
                                "shopId":"1"},
                         "expect":"OK"},
                        {"title":"商品收藏-商品ID传空",
                         "data":{"skuNo":None,
                                "shopId":"1"},
                         "expect":"ERROR"},
                        {"title":"商品收藏-店铺id传空",
                         "data":{"skuNo":"T0101010003",
                                "shopId":None},
                         "expect":"ERROR"},
                        {"title":"商品收藏-重复收藏",
                         "data":{"skuNo":"T0101010001",
                                "shopId":"1"},
                         "expect":"ERROR"},
                        {"title":"商品收藏-商品不存在",
                         "data":{"skuNo":"T0101018888",
                                "shopId":"1"},
                         "expect":"ERROR"}]

    web_attach_upload = [{"title":"上传图片-gif图片","data":{"file":evaluate_001,"type":1},"expect":"OK"},
                         {"title":"上传图片-jpg图片","data":{"file":evaluate_002,"type":1},"expect":"OK"}
                        ]


#
# class re():
#     url = "http://dev-gateway.worldfarm.com/wx-mall/web/cart/add"
#     data = {"skuNo": "Z0101010003", "shopId": "1", "amount": "2"}
#     url2 = "http://dev-gateway.worldfarm.com/wx-mall/web/cart/list"
#     data2 = {}
#     headers2 = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Accept": "application/json, text/plain, */*",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)"
#                       " AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/86.0.4240.111 Safari/537.36",
#         "_Device-Type_": "web",
#         "region": "online",
#         "Accept_Language": "zh",
#         "_Device-Id_":"cc4feebe419791332bbcff5e0fdf084a",
#         "_Token_": "39_mfUVHncpbmDgyhTJmFwv97G5oQAx76iR8xDyXk-iMdk4ypcFIJB3DfSmVRU1puwg0a2wbn4qQc_Ovj6N1cropzcFo3VpvuYFZLBkPJa9xiArxK2SsanMndkwcT1yLilWvSuiVSLwn8aqT_fxZWOfADAGDV"
#
# }
#     result = requests.post(url=url, data=data, headers=headers2)
#     print(result.json())
#     res_ = requests.post(url=url2,headers=headers2)
#     print(res_.json())

if __name__ == '__main__':
    a= submit_order().file_list