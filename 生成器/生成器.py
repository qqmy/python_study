s = (a*2 for a in range(3))
# print(s)  # <generator object <genexpr> at 0x105eada98>
# a = [i*2 for i in range(10000000)]  # 占内存
# print(a)
# print(s.__next__()) # 私有方法
# print(next(s))  # 等价于s.__next__()
# print(next(s))
# print(next(s))
# print(next(s))  # StopIteration 报错，只能迭代到第三个

# print(type(s))  # <class 'generator'>
# 生成器只能一个一个拿

# 生成器就是一个可迭代对象（iterable）
# for i in s:
#     print(i)

# 当一个对象没有被引用时，就会被回收  for遍历s时，获取第一个值0，print后，获取第二个值1，此时i指向1，0就被回收了

# 生成器一共两种创建方式：
# 1、(a*2 for a in range(3))
# 2、yield

def fool():
    print('ok')
    yield 1
    print('ok2')
    yield 2

g = fool()
# print(next(fool()))
# print(next(fool()))
# print(next(g))
# print(next(g))
# next(g)
# for i in g:
#     print(i)
#
# for i in fool():
#     print(i)
# print(type(fool()))  # <class 'generator'>

# 什么是可迭代对象：内部有__iter__()方法的对象(对象拥有iter方法的称为可迭代对象）

# seed
def bar():
    print('ok1')
    count = yield 1
    print(count)
    count2 = yield 2
    print(count2)
    yield 3

b = bar()
b1 = b.send(None)  # 相当于next(b)  第一次send前如果没有next，只能传一个send（None）执行顺序，先yield再赋值
print(b1)
b2 = b.send('eee')
print(b2)
# b3 = b.send('fff')
# print(b3)

