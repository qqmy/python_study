
# 闭包
# def outer():
#     x = 10
#     def inner():  # inner就是内部函数
#         print(x)   # 外部环境的一个变量
#
#     return inner   # 结论：内部函数inner就是一个闭包
# # inner() 不能直接调用inner inner是局部变量
# a = outer()
# a()

# 闭包定义：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）
# 关于闭包：闭包=内部函数+定义函数时的变量

# 开放封闭原则
# 对修改封闭，对扩展开放 即：不允许修改源代码，在不修改源代码的基础上可以扩展功能



# 装饰器  装饰器仅仅是用来装饰或者修饰函数的包装，返回一个修改后的函数对象，将其重新赋值原来的标识符，并永久失去对原始函数对象的访问
import time


# def fool():
#     print('fool')
#     time.sleep(2)

# 计算fool函数执行时间

# def show_time(f):
#     start = time.time()
#     f()
#     end = time.time()
#     print(end-start)
# show_time(fool)

# def show_time2(f):   # 装饰器，实现计算函数f的执行时间
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print(end - start)
#     return inner

# @show_time2 #  等价于fool = show_time2(fool)
# def fool():
#     print('fool')
#     time.sleep(2)
# fool()   # 此时调用fool，执行的是inner函数，其中包含了原始的fool函数

# fool = show_time2(fool)
# fool()

# @show_time2  # 等价于 bar = shouw_time2(bar)
# def bar():
#     print('bar')
#     time.sleep(3)
# bar()


# 功能函数的参数
# 被装饰函数的参数-定长参数
def show_time3(f):
    def inner(a,b):
        start = time.time()
        f(a,b)
        end = time.time()
        print(end - start)
    return inner

@show_time3
def ad(a,b):
    print(a+b)
    time.sleep(1)
# ad(1,2)


# 被装饰函数的参数-不定长参数
def show_time3(f):
    def inner(*args):
        start = time.time()
        f(*args)
        end = time.time()
        print(end - start)
    return inner

# 功能函数加参数
@show_time3
def ad(*args):
    sum = 0
    for i in args:
        sum +=i
    print(sum)
    time.sleep(1)
# ad(1,2,3)


# 装饰器的参数
def show_time4(log):
    def out(f):
        def inner(*args):
            if log == True:
                start = time.time()
                f(*args)
                end = time.time()
                print(end - start)
            else:
                f(*args)
        return inner
    return out

@ show_time4(True)
def ad(a,b):
    print(a+b)
    time.sleep(1)
ad(1,2)
