# 在函数内部调用函数本身

# 求n的阶乘
# 普通实现
# def test(n):
#     sum = 1
#     if n >= 1:
#         for i in range(1, n+1):
#             # print(i)
#             sum *= i
#         return sum
#     else:
#         return n

# 递归实现
def jiecheng(n):
    if n<=1:
        return n
    return n*jiecheng(n-1)

print(jiecheng(7))

'''
关于递归的特性
1、调用函数自身
2、有一个结束条件
3、但凡递归能解决的事情，循环都可以解决
4、递归的效率在很多时候会很低

'''
# 斐波那契数列,从起始值为0，1
# 1，2，3，5，8，13，21，34，55
def fei(n):
    a = 0
    b = 1
    for i in range(n+1):
        a, b = b, a + b
    return a
print(fei(8))

def feibo(n):
    if n <= 2:
        return n
    return feibo(n-1) + feibo(n-2)
print(feibo(1))