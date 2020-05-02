# class Bar():
#     def foo(self,arg):
#         print(self,self.name,self.age,self.gender,arg)  # self指代调用方法的对象
# obj = Bar()  # bar: 中间人
# obj.name = 'xiaoming'
# obj.age = 10
# obj.gender = 'nan'
# obj.foo('上山去砍柴')
#
# bar = Bar('hah')  # bar: 中间人
# # bar.name = 'alex' # 可以直接往中间人里存信息
# print(bar.name)
# bar.age = '19'
# bar.foo('666')
#
# bar2 = Bar('haha')
# # bar2.name = 'alex1'
# bar2.age = '29'
# bar2.foo('8888')

# 构造方法
# class Bar():
#     def __init__(self,name,age):
#         self.n = name
#         self.a = age
#     def foo(self,arg):
#         # self.gender = self.name
#         print(self,self.n,self.a,arg)  # self指代调用方法的对象
# obj = Bar('xiao',10)
# obj.n ='lisi'
# print(obj.n)
# # obj.name = 'xiaoming'
# # # obj.age = 10
# # obj.gender = 'nan'
# obj.foo('上山去砍柴')

class Person():
    def __init__(self,name,age):  # 构造方法：构造方法的特性，类名（）会自动执行构造方法
        self.name = name
        self.age = age
        self.x = 'AB'
    def show(self):
        print(f"{self.name}:{self.age} {self.x}型血")

lihuan = Person('李欢',18)
xiaoming = Person('小明',89)
lihuan.show()
xiaoming.show()
