from testcase.middleground.WMS.prepare.login import login
from testcase.middleground.WMS.common.config import read_config
from testcase.middleground.WMS.common.Pash import Header_mkdir,Public_mkdir


class assembleHeader:

    def __init__(self,url):
        self.url = url
        self.login = login(self.url).test_login()

    def add_header(self):

        headers = {"_Device-Id_":read_config(Header_mkdir).get("header", "_device-id_"),
                   "_Token_":read_config(Header_mkdir).get("header", "_token_"),
                   "region": "online"}

        return headers


if __name__ == '__main__':

    t = assembleHeader(url="/world-passport/admin/sso/sms-login").add_header()
    print(t)