# import unittest
# from ddt import ddt, data, unpack
#
#
# @ddt
# class FooTestCase(unittest.TestCase):
#
#     @data((3, 2), (4, 3), (5, 3))
#     @unpack
#     def test_tuples_extracted_into_arguments(self, first_value, second_value):
#         self.assertTrue(first_value > second_value)
#
#     @data([3, 2], [4, 3], [5, 3])
#     @unpack
#     def test_list_extracted_into_arguments(self, first_value, second_value):
#         self.assertTrue(first_value > second_value)
#
#     @unpack
#     @data({'first': 1, 'second': 3, 'third': 2},
#           {'first': 4, 'second': 6, 'third': 5})
#     def test_dicts_extracted_into_kwargs(self, first, second, third):
#         self.assertTrue(first < third < second)
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

#
# import ddt
# import unittest
# t_dict = {'a':'a','b':'b','c':'c'}
#
# class Test(unittest.TestCase):
#     def setUp(self):
#         print(self)
#
#     @ddt.data(t_dict)
#     @ddt.unpack
#     def test_a(self,a,b,c):
#         print(a)
#         print(b)
#         print(c)
#
#     if __name__ == '__main__':
#         unittest.main()


# def name(price,color='red',brand='carmy',is_second_hand='True'):
#     print(price,price)
#     print(color,color)
#     print(brand,brand)
#     print(is_second_hand,is_second_hand)

# def get_formed_name(first,last):
#     full_name = first+''+last
#     return full_name.title()

# def funciton():
#     print('This is a funciton')
#     a = 1+2
#     print(a)
#
# import ddt
# import unittest
# ## 定义任意的参数，list,dict,str,tuple等等
# t_list = [1,2]
# t_dict = {"a":"a","b":"b"}
# t_str = 'test_string'
# t_tuple = (1,2)
#
# @ddt.ddt
# class Test(unittest.TestCase):
#
#     def setUp(self):
#         print('start')
#     ##这个仅有一个参数,将t_list赋值给data，打印
#     @ddt.data(t_list)
#     def test_a(self,data):
#         print(data)
#
#     ## 这个有多个参数传入时,有一个函数接受
#     @ddt.data(t_list,t_dict,t_str,t_tuple)
#     def test_b(self,data):
#         print(data)
#
#     ## 这个有多个参数传入，有多个函数接收
#     @ddt.data(t_list,t_dict,t_str,t_tuple)
#     def test_c(self,a,b,c,d):
#         print(a)
#         print(b)
#         print(c)
#         print(d)
# if __name__ == '__main__':
#     unittest.main()

class test_classmethod(object):
    @classmethod
    def printd(self,a,b):
        c = a+b
        print(c)
if __name__ == '__main__':
    c =test_classmethod()
    c.printd(3,5)

class test_classmethod(object):
    @classmethod
    def print(cls,a,b):
        c =a+b
        print(c)
if __name__ == '__main__':
    test_classmethod.print(3,5)
#
# class A(object):
#     a =1
#     def def1(self):
#         print('foo')
#
#     @classmethod
#     def def2(cls):
#         print('def2')
#         print(cls.a)
#         cls().def1()

# class test_classmethod(object):
#     @classmethod
#     def printd(a,b):
#         c =a+b
#         print(c)
# if __name__ == '__main__':
#     test_classmethod.printd(3,5)

def f1(a):
    a.append(9)
li=[11,22,33,44]
f1(li)
print(li)

def f1(name,age):
    print(name)
    print(age)
f1("Guido",27)

def f1(name,age,who='you'):
    print(name,age,who)
f1("guido",27)
f1("guido",27,'she')

def i(kargs,*args,**kwargs):
    print(kargs,type(kargs))
    print(args,type(args))
    print(kwargs,type(kwargs))
i("kwk",'111','ppp',a=1,b=2,c=3)


#format格式化
s1 ="I am {0},age{1}".format("Guido",27)
print(s1)
#通过位置填充
print('hello {0} i am{1}'.format('ken','Tom'))
print('hello {} i am{}'.format('ken','Tom'))
print('hello {0} i am{1}.my name is {0}'.format('ken','Tom'))
#通过Key填充
print('hello {name1} i am {name2}'.format(name1='ken',name2='Tom'))
#通过下标填充
names=['ken','Tom']
print('hello {names[0]} i am {names[1]}'.format(names=names))
print('hello {0[0]} i am {0[1]}'.format(names))
#通过字典key
names ={'name1':'ken','name2':'Tom'}
print('hello {names[name1]}' 'i am {names[name2]}'.format(names=names))
#通过对象的属性
# class Names():
#     name1='ken'
#     name2='Tom'
# print('hello {names.name1} i am{names.name2}'.format(names=names))

#全局变量
name ='Guido'
def f1():
    global name
    name=1
    print(name)
f1()
print(name)

global val
val =10
def test1():
    global val
    val = 5
    print('test1 global val:',val)

def test2():
    val = 8
    print('test2 global val:',val)
class Test():
    def __init__(self):
        val=5
    def connect(self):
        print("class in global val:",val)
        if 5 ==val:
            print('global val is:',val)

if __name__ == '__main__':
    Test().connect()

def changeme(mylist):
    mylist.append([1,2,3,4])
    print('函数外取值：',mylist)
    return

    mylist =[10,20,30]
    changeme(mylist)
    print('函数外取值:',mylist)

def sum(total):
    total = 30
    print('函数内是局部变量:',total)
    return
total=0
sum(total)
print('函数外是全局变量:',total)
