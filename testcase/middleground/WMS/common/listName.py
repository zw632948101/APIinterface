import random
import time


class Random:
    # 只能传list
    def __init__(self,city=None,name=None,now=None):
        if city == None:
            self.city = ["铜仁","郫县","溶洞","音乐空间"]
        else:
            self.city = city
        if name == None:
            self.name = ["行政仓","车间仓","项目仓"]
        else:
            self.name = name
        if now == None:
            self.now = time.strftime('%S', time.localtime(time.time()))
        else:
            self.now = now

        self.img_url = ["https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1767448974,2051103783&fm=26&gp=0",
                        "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3112097844,4213331226&fm=26&gp=0",
                        "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2196976096,3047104416&fm=26&gp=0",
                        "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2013274768,216829781&fm=26&gp=0"]

    def create_name(self,create=None):
        if create == None:
            new_name = random.choice(self.city) \
                       + random.choice(self.name)

            return new_name

        elif create != None:
            new_img = random.choice(self.img_url) + ".jpg"
            return new_img

if __name__ == '__main__':
    t = Random().create_name(1)
    print(t)


