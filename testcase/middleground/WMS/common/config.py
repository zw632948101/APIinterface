import configparser


# conf_dir =Pash.conf
# token_dir = Pash.token_dir


class read_config():

    def __init__(self,mkdir):
        self.conf = configparser.ConfigParser()
        self.conf.read(mkdir,encoding='utf-8')


    def get(self,section,option):
        return self.conf.get( section, option)

    def boolen(self,section,option):
        return self.conf.getboolean( section, option)

    def float(self,section,option):
        return self.conf.getfloat( section, option)

    def int(self,section,option):
        return self.conf.getint( section, option)




if __name__ == '__main__':
    t = read_config(Public_mkdir).get("header","_deviceid_")
    print(t)