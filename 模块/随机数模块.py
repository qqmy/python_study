import random
print(random.random())  # 获得一个0到1之间的随机数
print(random.randint(0, 10)) # 获得0到10之间的整数，包括0和10
print(random.choice('hello')) # 随机获取一个序列中的一个值
print(random.choice(['12',[1,2,3],(12,13,45)]))
# print(random.shuffle(('1',2,3)))
print(random.sample([1,2,3,4,5],2)) # 在一个序列里随机选多个值
print(random.randrange(1,3)) # 获取1到3之间的整数，包括1，不包括10

# def v_code():
#     code = ''
#     for i in range(5):
#         if i == random.randint(0,2):
#             add = random.randrange(10)
#         else:
#             add = chr(random.randrange(65,91))
#         code += str(add)
#         # add_num = random.randrange(0, 10)
#         # add_al = chr(random.randrange(65, 91))
#         # if i == random.randint(0,5):
#         #     code += str(add_num)
#         # else:
#         #     code += str(add_al)
#
#     print(code)

def v_code():
    code = ''
    for i in range(5):
        add = random.choice([random.randrange(0,10),chr(random.randrange(65,91))])
        code +=str(add)
    print(code)
v_code()

# print(chr(65))