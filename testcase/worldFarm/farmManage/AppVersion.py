"""
__author__ = 'Xiujuan Chen'
__date__ = '2019/8/19'

测试集中包括  版本管理
"""
from testcase.worldFarm import testCase, OtherQuery


class AppVersion(testCase):
    fq = OtherQuery()

    def test_mobile_app_version_add(self):
        """
        移动端-版本管理-新增APP版本管理 1.2.4
        :return:
        """
        register = self.ka.mobile_app_version_add(appId='01', updateType=1,
                                                  downloadUrl='ftp://192.168.62.244/%E6%B5%8B%E8%AF%95%E5%8C%85/%E4%B8%96%E7%95%8C%E5%86%9C%E5%9C%BA/Android/1.2.3/QA/app-qa-debug_build%2826%29.apk',
                                                  appCode=None, appName='世界农场', versionMilepost=0, versionNum='1.2.4',
                                                  versionCode=30, versionNumBefore='1.2.3', versionBig=None,
                                                  updateTitle='版本更新', updateTitleEn='version uptate',
                                                  updateMessage='接口测试', updateMessageEn='api test', status=1)
        version = self.fq.query_get_app_version()
        self.assertEqual(register['status'], "OK")
        self.assertEqual(version.get('version_num'), '1.2.4')
        self.assertEqual(version.get('version_num_before'), '1.2.3')
        self.assertEqual(version.get('version_code'), '30')
        self.assertEqual(version.get('status'), 1)

    def test_mobile_app_version_get(self):
        """
        移动端-版本管理-获取PP版本信息
        :return:
        """
        register = self.ka.mobile_app_version_get(appId='02')
        self.assertEqual(register['status'], "OK")

    # def test_mobile_app_version_upload_app(self):
    #     """
    #     移动端-版本管理-上传APP包
    #     :return:
    #     """
    #     file = 'E://FTP//IFWorldFarm_Release_1.2.4_build(21).ipa'
    #     register = self.ko.mobile_app_version_upload_app(file=file)
    #     self.assertEqual(register['status'], "OK")


if __name__ == '__main__':
    m = AppVersion()
