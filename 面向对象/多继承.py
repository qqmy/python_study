# class F():
#     def a(self):
#         print('f.a')
# class F1(F):
#     # def a(self):
#     #     print('f1.a')
#     pass
# class F2():
#     def a(self):
#         print('f2.a')
#
# class S(F1,F2):
#     pass
#
# obj = S()
# obj.a()

'''
class Obj():
    def a(self):
        print('Obj.a')
class F1(Obj):
    pass
class F2(Obj):
    def a(self):
        print('F2.a')
class S(F1,F2):
    pass
s = S()
s.a()   # 执行的是F2中的a方法
'''

'''
class BaseRequest():
    def __init__(self):
        print('BaseRequest.init')

class RequestHandler(BaseRequest):
    def __init__(self):
        # super(RequestHandler,self).__init__()  # 执行父类的构造方法
        # BaseRequest.__init__(self)
        print('RequestHandler.init')
    def server_forever(self):
        print('RequestHandler.server_forever')
        self.process_request()

    def process_request(self):
        print('RequestHandler.process_request')

class Minx:
    def process_request(self):
        print('Minx.process_request')

class Son(Minx,RequestHandler):
    pass

# son = Son()    # Minx.process_request
# son.process_request()  # RequestHandler.server_forever
# son.server_forever()   # Minx.process_request   此时self指的是son，
# 先去Minx中找server_forever没找到后去RequestHandler中找，
# 在RequestHandler中找到server_forever
# server_forever中调用self.process_request() 方法，此时的self指的是son对象，所以要从Son中重新找
# Son中没找到就去他的父类中找，父类有时从左到右找的，所以找到的是Minx中的process_request方法

'''

class BaseRequest():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('BaseRequest.init')

class RequestHandler(BaseRequest):

    def __init__(self,name,age,gender):
        self.name = name
        self.age=age
        self.gender = gender
        print(self.gender,self.name,self.age)
        BaseRequest.__init__(self,'zhangsan',12)
        # self.name = name
        print(self.gender,self.name,self.age)
        # super(RequestHandler,self).__init__()  # 执行父类的构造方法
        # BaseRequest.__init__(self)
        print('RequestHandler.init')

    def server_forever(self):
        print('RequestHandler.server_forever')
        self.process_request()

    def process_request(self):
        print('RequestHandler.process_request')

class Minx:
    def process_request(self):
        print('Minx.process_request')

class Son(Minx,RequestHandler):
    pass

son = Son('liuyuxing',90,'zhongxing')
son.server_forever()
# 执行顺序
# 1、RequestHandler.init
# 2、BaseRequest.init
# 3、RequestHandler.server_forever
# 4、Minx.process_request


# import socketserver
# obj = socketserver.ThreadingTCPServer(1,2)
# obj.serve_forever()