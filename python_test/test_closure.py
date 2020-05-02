# 闭包
# def cunter(start_at = 0):
#     count = [start_at]
#     def incr():
#         count[0] +=2
#         return count[0]
#     return incr
# count = cunter()
# for i in range(10):
#     print(count())

# 定义一个函数
# def test(number):
#     # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
#     def test_in(number_in):
#         print("in test_in 函数, number_in is %d" % number_in)
#         return number + number_in
#
#     # 其实这里返回的就是闭包的结果
#     return test_in


# # 给test函数赋值，这个20就是给参数number
# ret = test(20)
#
# # 注意这里的100其实给参数number_in
# print(ret(100))


# 生成器
def simpleGen():
    yield 1
    yield '2---》punch'

for eachitem in simpleGen():
    print(eachitem)