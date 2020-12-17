import os




# os.path.realpath(__file__) 获取当前操作的文件路径
import os
moke_path =os.path.realpath(__file__)


# 整个项目路径
Wms_Path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
Config_mkdir = os.path.join(Wms_Path + r"\configs")
Header_mkdir = os.path.join(Config_mkdir + r"\header_wms.conf")
Public_mkdir = os.path.join(Config_mkdir + r"\public_wms.conf")
if __name__ == '__main__':

    print(moke_path)
    print(Config_mkdir)
    print(Header_mkdir)

# conf = os.path.join(moke_path + r'\configs\test.conf') # 测试环境不变的数据，配置文件存放路径
# token_dir = os.path.join(moke_path + r'\configs\token.conf') # 会变动的token，配置文件存放路径
# case_dir = os.path.join(moke_path + r'\datas')
# reports_dir = os.path.join(moke_path + r'\reports')
#
#
# reports = os.path.join(moke_path + r'\reports')
# result = os.path.join(moke_path , r'D:\WeFun Smoke\reports')
# html = os.path.join(result , 'test_runner.html')