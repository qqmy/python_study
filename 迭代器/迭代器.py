# 生成器都是迭代器，迭代器不一定都是生成器
# 可迭代对象：list，tuple，dict，string
from collections import Iterable,Iterator,Generator

l=[1,2,3]
d = iter(l)  # <list_iterator object at 0x10be38908>
print(d)

# 什么是迭代器：
# 满足两个条件：有iter方法，有next方法
'''
凡是可作用于for循环的对象都是Iterable（可迭代对象）类型
凡是可作用域next（）函数的对象都是Iterator（迭代器）类型它表示一个惰性计算的序列
'''
print(next(d))
print(next(d))
print(next(d))
for i in l:
    print(i)
# for 循环内部三件事
    # 1、调用可迭代对象的iter方法，返回一个迭代器对象
    # 2、不断调用迭代器对象的next方法
    # 3、处理StopIteration异常

# Iterator 迭代器，Iterable可迭代对象,Generator生成器
# import Iterator,Iterable

g = (i for i in range(10))
print(isinstance(l,Iterable))
print(isinstance(d,Iterable))
print(isinstance(l,Iterator))
print(isinstance(l,list))
print(isinstance(g,Generator))

