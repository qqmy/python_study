# class Foo():
#     def __init__(self,name,age):
#
#         self.name = name
#         # self.age = age
#         self.__age = age   # 私有变量，外部无法直接访问
#
#     def show(self):
#         return self.__age  # 可以间接访问
# obj = Foo('qmy',1)
#
# print(obj.name)
# # print(obj.__age)
# print(obj.show())

# class Foo:
#     # c = 123
#     __c = 123
#     def __init__(self):
#         pass
#
#     def show(self):
#         return self.__c
# print(Foo.c)
# print(Foo.__c)   无法直接访问
# print(Foo().show())

# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     @ classmethod
#     def __f1(cls):
#         print('f1')
#
#     @ classmethod
#     def f2(cls):
#         cls.__f1

# Foo._f1  无法直接访问
# Foo.f2    # 可以间接访问

#
# class F():
#     def __init__(self,name):
#         self.__name = name
#         self.age = 10
#         self.__gender = 'nan'
#         self.a ='a'
#
# class A(F):
#     def __init__(self,name,age):
#         self.__age = age
#         self.name = name
#         super(A,self).__init__(name)
#     def show(self):
#         print(self.age)
#         print(self.name)
#         print(self.a)
#         # print(self.__gender)  无法访问父类的私有字段
#
#
# a = A('qmy',123)
# # print(a.name)
# a.show()

class F:
    def __init__(self):
        self.ge = 123
        self.__gene = 123

class S(F):
    def __init__(self,name):
        self.name = name
        self.__age = 14
        super(S,self).__init__()

    def show(self):
        print(self.name)
        # print(self.__gene)   无法访问父类的私有字段
        print(self.ge)
        print(self.__age)

s = S('qmy')
s.show()