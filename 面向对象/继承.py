# class GrandFather():
#     def 喝花酒(self):
#         pass
# class Father(GrandFather):  # 父类，基类
#     def 篮球(self):
#         pass
#     def 足球(self):
#         pass
#     def 抽烟(self):
#         pass
#     def 喝酒(self):
#         pass
#
# class Son(Father):  # 子类，派生类
#     def 保健(self):
#         pass
# son = Son()
# son.保健()
# son.喝酒()
# son.喝花酒()

# class F:
#     def f1(self):
#         print('F.f1')
#
#     def f2(self):
#         print('F.f2')
# class S(F):
#     def s1(self):
#         print('S.s1')
#
#     def f1(self):   # 方法重写
#         # super(S,self).f1()  # 执行父类（基类）中的f1方法
#         # F.f1(self)  # 执行父类（基类）中的f1方法
#         print('S.f1')
#
# s = S()
# # s.s1() # s1中的self是形参，此时代指s
# # s.f2() # self永远指调用方法的调用者，此时指代s
#
# s.f1()

class RequestHandler():

    def get(self,arg):
        print('为所欲为')


re = RequestHandler()
re.get(1)


# 开放封闭原则，可以增加功能，不能修改源码

#
# def outer(get):
#     def inner(arg):
#         print('hahah')
#         get(arg)
#
#     return inner
#
#
# @outer
# def get(arg):
#     print('为所欲为')
#
# get(1)