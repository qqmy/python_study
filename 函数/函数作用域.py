# count = 10
# def test():
#     # pass
#     # count = 5
#     # print(count)  # 全局变量不可被修改，相当于重新创建了一个count，可以
#
#     # count +=1  # 报错  #全局变量被调用后，再修改报错  count +=1 相当于count = count +1
#
#     # print(count)
#     # count = 5  # 报错  # 全局变量被调用后，再修改报错
                            # 原因是，在局部变量中有count变量，但是在count被定义之前就使用了count，所以报错
                            # 因为python首先会在局部作用域中找count，找到后，就不在去全局里面找了
#
#     global count
#     print(count)
#     count = 5
#     print(count)
#
# test()

'''
变量查找顺序 LEGB原则：局部>外层>当前模块中的全局>python内置作用域
只有模块，类，函数，才能引入新的作用域
对于一个变量，内部作用域先声明，就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量，且不能修改该变量
内部作用域变量要修改外部作用域的变量值时，全局变量要使用global 关键字，嵌套作用域变量要使用nonlocal关键字
'''

# 练习
# 全局变量和局部变量
# a = 10
# def test():
#     # a = 11
#     # print(a)
#     # a = 12
#     # print(a)
#
#     # print(a)
#     # a = 11
#
#     global a
#     a = 0
#     print(a)
# print(a)
# test()

# 外部变量和局部变量
count = 10

def outer():
    outer = 0
    global count
    count = 11
    print(count)
    print(outer)
    def inner():
        nonlocal outer
        count = 100
        outer ='111'
        print(count)
        print(outer)

    inner()

outer()
