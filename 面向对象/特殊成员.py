# class Foo:
#     def __init__(self):
#         print('hahah')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#
# foo = Foo()  # 执行init方法
# foo()   # 执行call  python特殊方法，实例加()自动执行call方法

#
# class Foo:
#     def __init__(self):
#         pass
#     def __int__(self):
#         return 111
#     def __str__(self):
#         return 'qmy'
#
# obj = Foo()
# print(obj)  # print默认掉用对象的str方法  print(str(obj))
# print(obj,type(obj))
#
#
# # int，对象，自动执行对象的__int__方法
# r = int(obj)
# print(r)
#
# s = str(obj)  # str对象，自动执行对象的__str__方法
# print(s)
# print(obj)
#
# class F:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         # return "123"
#         # self = obj1(alex,19)
#         # other = obj2(erio,66)
#         # return self.name+other.name,self.age + other.age
#         return F(self.age,other.age)  # <__main__.F object at 0x104ab80f0>
#
#     def __del__(self):  # 析构方法 对象被销毁时自动执行，由python内部触发
#         print('对象被销毁')
#
#
# obj1 = F('qmy',123)
# obj2 = F('lyx',456)
# obj3 = F('zhangsan',123)
# # 两个对象相加时，自动执行第一个对象的__add__方法，并且将第二个对象作为参数传递进入
# a = obj1 + obj2
# print(a,type(a))   # ('qmylyx', 579) <class 'tuple'>

# class Foo():
#     '''
#     注释
#     '''
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.gender = 'nv'
#
# print(Foo.__dict__)
# obj = Foo('qmy',18)
# d = obj.__dict__
# print(d)


# li = [11,22,33,44]
# r1 = li[3]
# li[3] = 666
# del li[2]
#
# class Foo:
#     def __init__(self):
#         pass
#     def __getitem__(self, item):
#         return item+10
#     def __setitem__(self, key, value):
#         print(key,value)
#     def __delitem__(self, key):
#         print(key)
#
#
# li = Foo()
# print(li[1])  # 自动执行li对象中的__getitem__方法
# li[10] = 123  # 自动执行li对象中的__setitem__方法
# del li[10]    # 自动执行li对象中的__delitem__方法

# class Foo():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(self.age)
#     def __str__(self):
#         return '111'
# a = Foo('qm',11)   # 执行Foo('qm',11)获取到的是__str__方法的返回值


# class Foo:
#     def __init__(self):
#         pass
#     def __iter__(self):
#         return iter([1,2,3,2])
# li = Foo()
#
# # 如果类中有__iter__方法，则创建的对象为可迭代对象
# # 可迭代对象.__iter__（）的返回值：迭代器
# # for循环，遇到迭代器，直接执行next方法
# # for循环，遇到可迭代对象，先执行__iter__方法，并获取返回值，然后在执行next方法
# # 1、执行li对象对应的类中的__iter__方法，并获取其返回值
# # 2、循环上一步中的返回值
# for i in li:
#     print(i)
#
# class Foo(object):
#     def func(self):
#         print('hello')

class Mytype(type):
    def __init__(self,what,bases=None,dict=None):
        super(Mytype,self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self,*args,**args)
        self.__init__(obj)

class Foo(object,metaclass=Mytype):  # 类Foo，是type类的对象，创建Foo类的时候默认就会执行type类的构造方法
    def __init__(self,name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls,*args,**args)
obj = Foo()

# class Mytype(type):
#     def __init__(self,what,bases=None,dict=None):
#         # self = Foo
#         print(123)
#     def __call__(self, *args, **kwargs):
#         # self是Mytype的对象，即Foo类
#         print(456)
#         r = self.__new__(*args, **kwargs)
# class Foo(object,metaclass=Mytype):  # 类Foo，是type类的对象，创建Foo类的时候默认就会执行type类的构造方法
#     def __init__(self):
#         pass
#     def __new__(cls, *args, **kwargs):
#         # 在new里面才是真正的创建obj，即Foo类的对象
#         return '对象'
# obj = Foo()  # 执行Mytype的call方法  对象加（），执行call方法
# 第一阶段：解释器从上到下执行代码创建Foo类   即执行type类的构造方法
# 第二阶段：通过Foo类创建obj对象

# class Foo:
#     def func(self):
#         print(111)
# Foo().func()
#
# def func():
#     print(11)
# Foo = type('Foo',(object,),{'func':func})  # Foo也是对象，是type的对象
# Foo.func()