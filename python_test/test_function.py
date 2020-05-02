# import random
# cho = random.choice('+-')
# print(cho)
# print(random.randint(1,10))
# num = [random.randint(1,10) for i in range(2)]
# print(num)


# 算术游戏
#
# from random import randint, choice
# from operator import add, sub
#
# ops = {'+': add,"-": sub}
# MAXTERIES = 2
#
# def doprob():
#     op = choice("+-")
#     nums =[randint(1,10) for i in range(2)]
#     nums.sort(reverse=True)
#     ans = ops[op](*nums)
#     pr ='%d %s %d='%(nums[0],op,nums[1])
#     oops=0
#     while True:
#         try:
#             if int(input(pr)) == ans:
#                 print('correct')
#                 break
#             if oops==MAXTERIES:
#                 print('answer\n%s%d'%(pr,ans))
#             else:
#                 print('incorrect...try again')
#                 oops +=1
#         except(KeyboardInterrupt,EOFError,ValueError):
#             print('invalid input.. try again')
#
#
# def main():
#     while True:
#         doprob()
#         try:
#             opt = input('Again? [y]').lower()
#             if opt and opt[0] =='n':
#                 break
#         except(KeyboardInterrupt,EOFError):
#             break
# main()
#


# def fool():
#     'hhhhhh'
#
# def bar():
#     pass
#
# bar.version = 1
# bar.__doc__ = 'doc'
#
# # print(help(fool()))
# print(fool.__doc__)
# help(fool)
# fool 函数的引用，fool() 函数的调用
# print(bar.__doc__)
# print(bar.version)


# 装饰器
import logging

# def use_logging(func):
#
#     def wrapper():
#         logging.warn("%s is running" % func.__name__)
#         return func()
#     return wrapper
#
# @use_logging
# def foo():
#     print("i am foo")
#
# foo()

# 装饰器示例

# def tsfuns(func):
#     def wrappernfunc(*args):
#         "执行的操作"
#         return func(*args)
#     return wrappernfunc
#
# @tsfuns()
# def func():
#     pass
#
# func()

# 参数组 关键字参数，非关键字参数
# def fun(one,two = 1, *tup, **dict):   # *tup：元组，*dict：字典
#     print(one)
#     print(two)
#     print(tup)
#     print(dict)
#
# fun(1,2,3,a=1,b=2,c=3)
# '''
# 结果 (1, 2)
# {'a': 1, 'b': 2, 'c': 3}'''

# 测试函数
# def testit(func,*nkwargs):
#
#     try:
#         retval = func(*nkwargs)
#         result = (True,retval)
#     except Exception as diag:
#         result = (False,str(diag))
#     return result
#
# def test():
#     funcs = (int,float)
#     vals = (1234,12.34,'1234','12.34')
#
#     for eachFunc in funcs:
#         print('_'*20)
#         for eachVal in vals:
#             retval = testit(eachFunc,eachVal)
#             if retval[0]:
#                 print("%s(%s)=" %(eachFunc.__doc__,'eachVal'),retval[1])
#             else:
#                 print('%s(%s)= FALLED' %(eachFunc.__doc__,'eachVal'),retval[1])
#
# test()


# 函数式编程
# a = lambda *x : x
# print(a(3, 4, 5))
#
# print(filter(lambda x: x % 2, [1, 2, 3, 4, 5]))

# from random import randint
# def odd(n):
#     return n%2
#
# allnums = []
# for eachnum in range(9):
#     allnums.append(randint(1,99))
#
# print(filter(odd,allnums))

# from random import randint
# allNums = []
# for eachnum in range(9):
#     allNums.append(randint(1,99))
# print([n for n in allNums if n%2])
# 等价于
# print([n for n in [randint(1,99) for i in range(9)] if n%2])

# 函数式编程的内建函数
# 1. fillter(func,seq)调用一个布尔函数func来迭代遍历没个seq中的元素；返回一个使func返回值为true的迭代器对象
# 2. map(func,seq1[,seq2...)将函数func作用于给定序列s的每个元素，并用一个列表来提供返回值，如果func为None，func表现为一个身份函数
# 返回一个含有每个序列中元素集合的n个元组的列表
# 2. reduce(func,seq[,init)将二元函数作用于seq序列的元素，每次携带一对（先前的结果以及下一个序列元素），连续的将现有的结果和下一个值
# 作用在获得的随后的结果上，最后减少我们的序列为一个单一的返回值，如果初始值init给定，第一个比较回事init和第一个序列元素而不是序列的头两个元素

# eg fillter

# print(list(filter(lambda x: x % 2, range(10))))

# # eg map
# print(list(map(lambda x, y, z: z , [1, 2, 3,1], [4, 5, 6,1], [7, 8, 9,])))
# print(list(map(lambda x,y:1,[1,2,3],[2,3,4,5])))
# print(list(map(lambda x,y:(x,y),[1,4],[2,3])))
# print(list(zip([1, 2, 3], [4, 5, 6])))  # 返回一个含有每个序列中元素集合的n个元组的列表
import functools

# print(functools.reduce(lambda x, y: x , [9, 2, 3],1))
it = functools.reduce(lambda x,y:x,[12,3,2])

a = 1
