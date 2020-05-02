# 通过yield实现
def fib(n):
    i = 1
    before,after = 0,1
    while i<= n:

        before,after=after,before+after
        yield after
        i +=1
# print(type(fib(8)))
# for i in fib(8):
#     print(i)
# g = fib(8)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
