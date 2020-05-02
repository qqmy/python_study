from random import randint

# input = int(input('qingshurunidefenshu:'))
#
# if 90<=input<=100:
#     print('A')
# elif 80<=input<90:
#     print('B')
# elif 79<=input<80:
#     print('C')
# elif 60<=input<70:
#     print('D')
# elif 0<=input<60 :
#     print('E')
# else :
#     print('qingshuruzhengqededenfenshu')

# 猜拳游戏
'''
1、用户输入的石头（0）、剪刀（1）、布（2）
2、电脑产生一个石头（0）、剪刀（1）、布（2）
3、判断胜负
'''
def caiquan():
    while True:
        # 获取用户输入的拳头
        user_quan = int(input('请出拳：石头（0）、剪刀（1）、布（2）'))
        # 获取电脑的拳头
        computer_quan = randint(0, 2)
        print('电脑的拳头是%d' % computer_quan)
        if user_quan in [0, 1, 2]:
            if user_quan == computer_quan:
                print('平')

            elif user_quan < computer_quan:
                print('赢')

            elif user_quan > computer_quan:
                print('输')
            break
        else:
            print('请输入正确的数')
            continue

'''
一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序完成随机分配
'''
def fenpei():
    school = [[],[],[]]
    teachers = ['A','B','C','D','E','F','G','H']
    for teacher in teachers:
        rand = randint(0, 2)
        # print(school[rand])
        school[rand].append(teacher)

    return school


# print(fenpei())

# 定义一个列表用来存储八位老师的名字
# teach_list = []
# i = 0
# while i<8:
#     teach_name = '老师' + str(i+1)
#     teach_list.append(teach_name)
#     i +=1
#
# # 定义学校，并包含3个办公室
# school = [[],[],[]]
# # 获取每个老师并随机分配办公室
# for teacher in teach_list:
#     office_number = randint(0,2)
#     school[office_number].append(teacher)
# # 打印各个办公室的老师列表
# for office in school:
#     for teacher in office:
#         print('%s' %teacher,end='')
#     print('\n'+'*'*20)

shenfen = [{1:{'姓名':'奥巴马','年龄':'50','性别':'男','身份证':'1088'}},
 {2:{'姓名':'希拉里','年龄':'56','性别':'女','身份证':'2782'}},
 {3:{'姓名':'特朗普','年龄':'60','性别':'男','身份证':'3368'}},]
for i in shenfen:
    keys = i.keys()
    for key in keys:
        print(key,i.get(key))




def bubblesort(arr):
    le = len(arr)
    for i in range(le):
        for j in range(le-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print(bubblesort([10,9,32,90,21]))

# n的阶乘
# def jiecheng(n):
#     sum = 1
#     for i in range(1,n):
#         sum = sum*i
#     return sum
# print(jiecheng(10000))

# 斐波那契数列
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
print(fib(10))

def fb(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fb(10))
