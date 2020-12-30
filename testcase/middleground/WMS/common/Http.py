import requests
import json



class Request():

    def __init__(self, method, url, data, headers, cookie=None,verify=False):

        if method == 'get':
            self.result = requests.get(url=url,params=data,headers=headers,cookies=cookie)

        elif method == 'post':
            self.result = requests.post(url=url, data=data, headers=headers,cookies=cookie)

        elif method == 'put':
            self.result =requests.put(url=url,data=data,headers=headers,cookies=cookie)


    def get_code(self):
        return  self.result.status_code
    def get_text(self):
        return self.result.text
    def get_json(self):
        return self.result.json()
    def get_cookie(self):
        return self.result.cookies
    def get_header(self):
        return self.result.headers


if __name__ == '__main__':
    data = {"appId": "FLOWER_CHASERS", "mobile": "15198034727", "verifyCode": "8888", "deviceType": "WEB",
            "deviceId": ""}
    res = Request('post',url="http://dev-gateway.worldfarm.com/world-passport/admin/sso/sms-login",data=data,headers=None,cookie=None)
    result = res.get_json()
    print(result)
    header = {"_Device-Id_":result['content']['deviceId'],
              "_Token_":result['content']['token'],
              "region":"online"
              }
    data1 = {"status":1}
    resp = Request('post',url="http://dev-gateway.worldfarm.com/mp-wms/admin/warehouse/list",data=data1,headers=header,cookie=None)
    print(header)
    print(resp.get_json())

