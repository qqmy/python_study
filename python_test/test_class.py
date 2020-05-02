#
# class ClassA():
#     def test(self,x):
#         print(11111,x)
#
# classa = ClassA()
# classa.test(10)

# classa.x = 1
# classa.y = 2
# print(classa.x+classa.y)
class AddrBookEntry():
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def update(self,nphone):
        self.phone = nphone
        print(self.phone)
        print(self.name)

# add = AddrBookEntry(1,2)
# add.update(1)

# # 创建子类
# class EmplAddrBookEntry(AddrBookEntry):
#     # '类定义'   # 类的文档字符串，必须紧随头行的字符串，文档字符串不能被派生类继承，派生类必须有自己的文档字符串，可以通过print(EmplAddrBookEntry.__doc__)查看
#     class1 = 1   # 类的数据属性
#     def __init__(self,name,phone,email):
#         AddrBookEntry.__init__(self,name,phone)
#         self.phone = 1
#         self.email = email
#         # print(self.name)
#         # print(self.phone)
#         # print(self.email)
#     def updateEmail(self,email):
#         self.email = email
#         print(self.email)
#
#
# # print(EmplAddrBookEntry.class1)  # 类数据属性，不依赖于任何类实例可以直接通过类名.类数据属性调用
#
# emp = EmplAddrBookEntry('zhangsan','12342222','qq@qq.com')
# EmplAddrBookEntry.class1 =2
# print(EmplAddrBookEntry.class1)   # 2
# print(emp.class1)    # 2
# emp.class1 = 3
# print(emp.class1)   # 3
# print(EmplAddrBookEntry.class1)   # 2
# EmplAddrBookEntry.class1 = 4
# print(emp.class1)    # 3
# print(EmplAddrBookEntry.class1)  # 4
# # emp.a = 'a'
# # emp.updateEmail('12@qq.com')
# # emp.update(88888)
#
# # 查看类属性
# # print(dir(EmplAddrBookEntry))
# print(emp.__dict__)
# # print(vars(EmplAddrBookEntry))



# class Test():
#     a = [1,2]
#     def test(self):
#         print(11111)
#
# test = Test()
# print(test.a)
# for i in range(10):
#     if i > 1:
#         test.a.append(2)
# print(Test.a)


# # 静态方法
# class TestStaticMethod:
#     @staticmethod
#     def fool():
#         print('calling static method fool()')
#
# tests = TestStaticMethod
# tests.fool()
# TestStaticMethod.fool()
#
# # 类方法
class TestClassMethod:
    @classmethod
    def fool(cls):
        print('calling class method fool()')
        print(cls.__name__)  # 打印当前类名字符串
TestClassMethod.fool()
testc = TestClassMethod
testc.fool()

# print(dir(TestClassMethod))
# print('*'*20)
# print(dir(testc))
# print(testc.__dict__)
# print(vars(testc))
print(dir())

# class RoundFloatManual():
#     def __init__(self,var):
#         assert isinstance(var,float),'values must be a float'
#
#         self.var = round(var,2)
#
#     def __str__(self):
#         return str(self.var)
# rf = RoundFloatManual(100.009)
# print(rf)


