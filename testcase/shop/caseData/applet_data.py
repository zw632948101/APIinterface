import requests
from utils.log import log
import time
import random
import warnings
from interfaces.wxshop.MallAction import MallAction
#from testcase.middleground.sql.brandMP import mp_label as
from testcase.shop.sql.webMP import mp_label

from interfaces.middleground.ProductAction import ProductAction
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import requests
class applet_api:
    admin_web_cart_add = [{"title":"加入购物车","data":{"skuNo":"T0101010001","shopId":"1","amount":"13"},"expect":"OK"},
                          {"title":"商品编码为空","data":{"skuNo":None,"shopId":"1","amount":"13"},"expect":"ERROR"},
                          {"title":"商品id为空","data":{"skuNo":"T0101010001","shopId":None,"amount":"13"},"expect":"ERROR"},
                          {"title":"购买数量","data":{"skuNo":"T0101010001","shopId":"1","amount":None},"expect":"ERROR"},
                         ]
    admin_web_cart_edit_amount = [{"title":"编辑购物车商品数量","data":{"id":"6","amount":"9"},"expect":"OK"},
                                  {"title":"编辑购物车数量为空","data":{"id":"6","amount":None},"expect":"ERROR"}
                                  ]

    admin_web_cart_balance = [{'title':'购物车结算','data':{"id":"6"},'expect':'OK'},
                        {'title':'结算id空','data':{"id":None},'expect':'ERROR'}]

    admin_web_cart_purchase = [{"title":"加入购物车","data":{"skuNo":"T0101010001","shopId":"1","amount":"13"},"expect":"OK"}]

class submit_order:
    cartId = ''
    web_order_close = []
    web_order_detail = []
    web_order_list = []
    web_order_submit_order = [{"title":"下单",
                               "data":{"shopId":"1",
                                       "product":{"cartId":"10","skuNo":"Z0101010003","skuNum":"3"},
                                       "addressId":"1",
                                       "freight":"0",
                                       "deliveryType":1,
                                       "productPrice":100,
                                       "buyerMemo":"尽快送达!"},
                               "expect":"OK"}
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

