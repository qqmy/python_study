import time
import sys
# file = open('flush.txt','w')
# file.write('a')
# # file.flush()
# time.sleep(20)
# file.close()
#
# for i in range(20):
#     # sys.stdout.write('#')
#     # sys.stdout.flush()
#     print('#',end='')
#     time.sleep(0.2)

# file = open('flush.txt','a')
# # file.write('a')
# file.truncate(1)   # 截断，不加参数默认从起始位置开始截断
# file.fileno()  # 返回一个文件操作符，是一个非负整形的数，唯一的代表
# file.close()

'''
昨夜寒蛰不住鸣。
惊回千里梦，已三更。
起来独自绕阶行。
人悄悄，帘外月胧明。
白首为功名，旧山松竹老，阻归程。
欲将心事付瑶琴。
知音少，弦断有谁听。
'''

# r+ 读写模式，w+ 写读模式，a+ 追加读模式
# file = open('小重山.txt','r+')
# print(file.readline())
# print('###')
# # file.seek(10)
# file.write('1111')
# print(file.readline())
# file.close()

# file = open('小重山.txt','w+')
# print(file.readline())
# file.write('111111')
# # file.seek(0)
# print(file.readline())
# file.close()


# 终极问题
# 在第六行末尾添加alex
# 只能复制一份
file = open('小重山.txt','r+')
file2 = open('小重山2.txt','w+')
number = 1
for line in file:
    if number == 6:
        line = ''.join([line.strip(),'alex\n'])
    file2.write(line)
    file2.flush()
    number +=1
file.close()
# file2.flush()
for f in file2:
    print(f)
file2.close()


with open('log','r') as f:
    f.readlines()
    f.read()
# 退出with代码块后，会自动关闭文件
print('hello')

# with 同时管理多个文件对象
with open('file1','r') as file1,open('file2','w') as file2:
    file1.read()
