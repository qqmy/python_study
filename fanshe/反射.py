class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        return '%s-%s' %(self.name,self.age)
obj = Foo('alex',18)
b = 'name'
# 通过b拿出 obj对象中name的值
# print(obj.__dict__[b])
#
# # 去什么东西里面获取什么内容
# print(getattr(obj, 'name'))  # 通过字符串的形式去取类的成员
#
# func = getattr(obj,'show')
# print(func)
# r = func()
# print(r)
#
# print(hasattr(obj,'name'))  # 判断obj对象中是否有name成员
# setattr(obj,'k1','v1')   # 设置k1=v1
# print(obj.k1)
# delattr(obj,'k1')   # 删除k1


# fanshe：通过字符串的形式，去操作对象中的成员，包括获取，添加，删除，查找

from fanshe import s
# name = getattr(s,'name')
# print(name)
# fun = getattr(s,'fun')
# print(fun())
# foo = getattr(s,'Foo')
# obj = foo('lyx')
# obj.fu()

url = input('请输入要查看的URL：')
if hasattr(s,url):
    result = getattr(s,url)
    print(result())
else:
    print(404)