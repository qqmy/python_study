# class Foo():
#     def __init__(self):
#         pass
# obj = Foo()  # obj对象，obj也称为Foo类的实例，（实例化）
# obj1 = Foo()
# obj2 = Foo()
# obj3 = Foo()


# 单例，用于使用同一份实例
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.name,self.age)
#
# v = None
# if v:
#     v.show()
# else:
#     v = Foo('alex',18)
#     v.show()

# python实现单例模式  单例模式，每次创建的时候用的都是同一个实例
class Foo:
    __v = None
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @ classmethod
    def get_instance(cls,name,age):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo(name,age)
            return cls.__v
# 不要使用类名加（）创建实例，通过类名.get_instance创建实例
v1 = Foo.get_instance('1my',18)
print(v1)
v2 = Foo.get_instance('qmy',18)
print(v2)
print(v1.name,v2.name)   # 结果：1my 1my






class F1():
    def __init__(self,name):
        self.name = name
class F2():
    def __init__(self,ff):
        self.ff = ff
class F3():
    def __init__(self,dd):
        self.dd = dd

f1 = F1('qmy')
print(f1.name)
f2 = F2(f1)
print(f2.ff.name)
f3 = F3(f2)
print(f3.dd.ff.name)