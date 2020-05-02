# filter(function, iterable) 将iterable中的每个元素交给function函数过滤，返回过滤后的结果，如果function不存在过滤条件，则会返回iterable本身
# def fun(s):
#     if s != 'a':
#         return s
#
#
# fil = filter(fun,[1,2,3,'a','b']) # 结果是一个迭代器对象
#
# lis = list(fil)
# print(lis)  # [1, 2, 3, 'b']

# map(function, iterable) 将iterable中的每个元素交给function函数处理，返回处理后的结果
# def fun2(n):
#     return n+'hello'
# ma = map(fun2,'word')
# list = list(ma)
# print(list)  # ['whello', 'ohello', 'rhello', 'dhello']

# filter与map的区别，map，不会修改iterable，只对其进行过滤
# map可以对iterable中的每个元素进行修改

# reduce reduce的结果就是一个值
from functools import reduce
def add(x,y):
    return x + y
print(reduce(add,range(0,1)))
#
# # reduce实现阶乘
# def jiecheng(x,y):
#     return x*y
#
# print(reduce(jiecheng, range(1,8)))

# lambda 实现阶乘
print(reduce(lambda x, y: x * y, range(1, 8)))
