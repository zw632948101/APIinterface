import random
import time

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
        return random.choice(logo) + form


class member_data:


    tag_add = [
               {"title": "添加标签",
                "data": {"name":Random().create_name(),"remark":"通过正式手续加入某个会社或专业组织的人"},
                "expect":"OK"},
               {"title": "标签名字＞20字符",
                "data": {"name":"精英一族小众群体的称谓投其所好研发产品完善服务","remark":"通过正式手续加入某个会社或专业组织的人"},
                "expect": "ERROR"},
               {"title": "标签说明＞400字符",
                "data": {"name":Random().create_name(),"remark":"成长真好儿时bai有喜有忧有笑有泪就像"
                                                                "一个五味瓶但还是苦多甜少儿时不懂事情总办杂记得一次我和妈妈到乡"
                                                                "下看老爷到了乡下我便和那里的伙伴们玩了起来我们到回收废品的阿姨家旁"
                                                                "边玩我在一辆三轮车里发现了一台收音机我们明知这是阿姨回收来的但在伙"
                                                                "伴的催促下我举起收音机向一块石头砸去结果可想而知我被妈妈严厉地批评了"
                                                                "慢慢地长大了懂得了一些事理做的错事变少了当然挨打挨骂次数减少了又一"
                                                                "次我和妈妈又到乡下看老爷到了乡下我又和那里的伙伴们玩了起来老爷家的"
                                                                "房子后有一片青草非常绿原来那里立着一块写着禁止进入的木牌如今已经倒下"
                                                                "了如果是小时侯会对那木头“招牌”视而不见跨进去玩事后是免不了一通骂现在"
                                                                "大了就走过去把木牌立起用绳子绑在木桩上再给一部分草浇上水回到家后我将"
                                                                "事说了一遍大家都夸我长大了我自豪地走出门成长真是好啊做的错事愈来愈少"
                                                                "受到的表扬愈来愈多愿永远成长成长真好"},
                "expect": "ERROR"},
               {"title": "标签名为空",
                "data": {"name":None,"remark":"协会会员，以某专业人士自发组织，提供专业学术交流、教育"},
                "expect": "ERROR"},
               {"title": "标签说明为空",
                "data": {"name":"铂金会员","remark":None},
                "expect": "ERROR"}
               ]

    tag_del = []
    tag_detail = []
    tag_edit = []
    tag_list = []
    tag_tagged_by_tag = []