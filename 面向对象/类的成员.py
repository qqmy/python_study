'''
游戏人生程序
1、创建三个游戏人物，分别是：
仓井井，女，18，初始战斗力1000
东尼木木，男，20，初始战斗力1800
波多多，女，19，初始战斗力2500

2、游戏场景，分别：
草丛战斗，消耗200战斗力
自我修炼，增长100战斗力
多人游戏，消耗500战斗力
'''
# class Person:
#     def __init__(self,name,age,gender,fight):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.fight = fight
#
# role_list = []
# y_n = input('是否创建角色')
# if y_n == 'y':
#     name = input('请输入名称')
#     age = input('请输入年龄')
#     gender = input('请输入性别')
#     fight = input('请输入初始战斗力')
#
#     role_list.append(Person(name,age,gender,fight))
#     # role_list[]


# class Province:
#     #静态字段，属于类，在内存中只保存一份 ，可以通过类访问，也可以通过对象访问，如果静态字段被修改了，那么之后创建的对象中的该字段均会被修改
#     country = '中国'
#
#     def __init__(self,name):
#         # 普通字段 属于对象，只有创建对象的时候才创建
#         self.name = name


# 静态字段通过类名.字段名调用
# Province.country='韩国'
# print(Province.country)
# 普通字段通过对象.字段名调用
# pro = Province('河南')
# 通过对象访问静态字段
# pro.country='北京'
# pro1= Province('河北')
# print(pro.country)
# print(pro.name)


class Foo:


    def bar(self):
        print('bar')

    @staticmethod  # 静态方法不用创建对象，可以直接访问，相当于模块级函数的封装
    def sta():      # 静态方法不用传self
        print('123')

    @staticmethod
    def sta1(a1,a2):
        print(a1,a2)

    @classmethod
    def clas(cls):  # 类方法，cls是类名
        print(cls)
        print('classmethod')
obj = Foo()
obj.bar()
Foo.sta()
Foo.sta1(1,2)
Foo.clas()

# 通过类来调用方法
# obj = Foo()
# Foo.bar(obj)


# class A:
#     def f1(self):
#         print('A.f1')
#         self.f2()
#     def f2(self):
#         print('A.f2')
#
#
# class S(A):
#     def f2(self):
#         print('S.f2')
# s = S()
# s.f1()



