# try:
#     int('11')
#     int('hahha')  # 上面如果有异常，则执行不到这里，没有异常才会执行到这
# except IndexError as e:  # 从上到下依次判断，执行了其中的一个exception，则后面的exception都不执行
#     print("IndexError")
# except ValueError as e:
#     print("ValueError")
# except Exception as e:
#     print('Exception')
# else:
#     print('else')  # 如果没有异常，则执行else
# finally:
#     print('finally') # 无论如何都会执行
#
# try:
#     # 主动触发异常
#     raise  Exception('主动触发异常')
# except Exception as e:
#     print(e)

# 自定义异常
class OldBoyError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    raise OldBoyError('我错了...')
except OldBoyError as e:
    print(e)   # e对象的str方法，获取返回

# 断言 assert 条件
# 如果条件成立则继续执行，如果条件不成立，则报错
# 用于强制用户服从，不服从就报错，可以捕获，但是一般不捕获
print(1)
assert 1==2
print(2)  # assert不满足，该语句不执行
