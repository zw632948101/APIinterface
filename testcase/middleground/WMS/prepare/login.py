import requests
import json
import unittest
import configparser
from testcase.middleground.WMS.common.config import read_config
from testcase.middleground.WMS.common.Pash import Header_mkdir # 存放header值得配置文件
from testcase.middleground.WMS.common.Pash import Public_mkdir # 调用登录接口需要的参数值，直接放在了公共配置文件


class login:
    def __init__(self,url):
        self.url = read_config(Public_mkdir).get("test_url","login_url") + url
        self.data = {"appId":read_config(Public_mkdir).get("login_data","appId"),
                     "mobile":read_config(Public_mkdir).int("login_data","mobile"),
                     "verifyCode":read_config(Public_mkdir).int("login_data","verifyCode"),
                     "deviceType":read_config(Public_mkdir).get("login_data","deviceType")
                     }

    def test_login(self):
        # 调登录接口
        try:
            req = requests.post(url=self.url, data=self.data)
        except Exception as e:
            raise e
        # 登录接口响应结果
        result = req.json()

        # 如果登录接口调用成功，写入header参数至配置文件，便于后续接口调用
        if result != "ERROR":
            set_conf = configparser.ConfigParser()
            set_conf.add_section('header')
            set_conf.set('header', '_Token_', result['content']['token'])
            set_conf.set('header', '_Device-Id_', result['content']['deviceId'])
            try:
                with open(Header_mkdir, 'w+') as fw:
                    set_conf.write(fw)
            except Exception as e:
                raise e

        else:
            print("登录报错")

        return result


if __name__ == '__main__':
    url = r"/world-passport/admin/sso/sms-login"
    data = {"appId":"FLOWER_CHASERS","mobile":"15198034727","verifyCode":"8888","deviceType":"WEB"}
    t = login(url=url).test_login()
    print(t)
