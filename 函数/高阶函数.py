
# def out():
#     def inner():
#         return 8
#     return inner  # 返回的是inner函数对象的地址
# print(out())   # <function out.<locals>.inner at 0x1104232f0>
# out = out()
# print(out())   # 要想获得inner的结果，要调用它
#
# def out():
#     def inner():
#         return 10
#     return inner() # 返回的是inner函数的调用结果，8
# print(out())   # 10
# # print(out)

# 高阶函数：1、函数名可以作为一个参数输入
        #  2、函数名可以作为返回值

def fu(n):
    return n*n

def test(a,b,f):
    return f(a) + f(b)

print(test(1, 2, fu))

# 函数名可以进行赋值
foo = fu
print(foo(10))
# 函数名可以作为参数，还可以作为函数的返回值，代表该函数对象的引用，要想获得该函数对象的值需要调用它