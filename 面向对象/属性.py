class A:
    def __init__(self):
        self.name = 'name'

    def fool(self):
        print(self.name)

    # 用于执行obj.per
    @ property   # 属性，添加property装饰器后，就可以像调用字段一样调用方法
    def per(self):
        print('p')
        return 1

    # obj.per = 123  用于给obj.per传值
    @ per.setter
    def per(self,var):
        print(var)

    @ per.deleter
    def per(self):
        print('deleter')
obj = A()

p = obj.per   # 正常调用p方法应该是a.p()，但是添加property装饰器后，就可以像调用字段一样调用方法 结果：p
print(p)  # 结果 1
obj.per = 123 # 结果：123    相当于执行@ per.setter
del obj.per   # 结果deleter 相当于执行@ per.deleter


