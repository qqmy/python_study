# 计算机函数 == subroutine 子程序，procedures 过程
'''作用：
1. 减少重复代码
2. 方便修改，更易扩展
3. 保持代码的一致性
'''
# import time
# time_format = '%Y-%m-%d %X'
# time_current = time.strftime(time_format)
# print(time_current)
#
# def print_info(name,age):
#     print(name,":",age)
# print_info('张三',10) # 必需参数
# print_info(age='10',name = '李四') # 关键字参数
#
# def print_info2(name,age,sex='男'):
#     print(name,":",age, sex)
# print_info2('李四',10)  # 默认参数
# print_info2(name='王五',age=1)


# 不定长参数 无命名参数 元组
# def add(*args):
#     sum = 0
#     for i in args:   # args = (1,2,3,4)
#         sum = sum+i
#     print(sum)
#
# add(1,2,3,4)

# 不定长参数 有命名参数 字典（键值对）
# def print_info(name,age,**kwargs):
#     for i in kwargs:  # kwargs = {'sex': '男', 'phone': '12345566'}
#         print("name:",name,'age:',age,i,":",kwargs[i])
# print_info('张三',10,job='it',sex='男')

# 元组+字典
def print_info(*args,**kwargs):
    print(args)
    print(kwargs)
# print_info('zhangsan',10,'it',sex='男',phone='12345566')
# ('zhangsan', 10, 'it')
# {'sex': '男', 'phone': '12345566'}

# 位置关系：从左到右：位置>关键字>默认>*args>**kwargs
print_info(*'111',**{'name':'张三','phone':'123400000'})
