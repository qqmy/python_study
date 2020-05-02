from functools import reduce

def jiecheng(n):
    if n <= 1:
        return n
    return reduce(lambda x,y:x*y,range(1,n+1))
print(jiecheng(5))