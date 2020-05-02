'''
对文件操作流程：
1、打开文件得到文件句柄并赋值给一个变量
2、通过句柄对文件进行操作
3、关闭文件

r：只可读
w：只可写，open时清空文本内容
a：追加，不可读
'''
f = open('小重山.txt', 'r', encoding='utf-8')
# data = f.read(1) # 读出第一个字符
# print(data)
# for file in f :
#     print(file,end='')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# le = 1
# for i in f.readlines():
#     # 在第六行后加个字符串
#     if le == 6:
#         i = ''.join([i.strip(), 'hello', 'kk'])  # 取代万恶的加号
#     print(i.strip())
#     le += 1
#
# # print(f.readlines())
#
# f.close()

# file = open('小重山2.txt','w+')
# file.write('hello\n')
# file.write('world')
# file.close()
import time

# file = open('小重山2.txt','a')
# file.write('\nhello\n')
# file.write('world')
# # time.sleep(10)
# file.close()


# file = open('小重山.txt','r')

# tell检测当前光标位置，一个中文占3个字符，一个英文一个字符
# print(file.tell())
# print(file.read(10))  # read（）中英文均占一个字符
# print(file.tell())
# file.seek(0)      # 用于断点续传
# print(file.read(10))
# print('##########')

# for f in file:  # 这是for内部将file对象做成了一个迭代器，用一行取一行
#     print(f.strip())


# 将小重山中的第五行改成hello world
# file_read = open('小重山.txt','r')
# file_write = open('小重山2.txt','w')
# index = 1
# for f in file_read:
#     if index == 5:
#         f = 'hello world\n'
#     file_write.write(f)
#     index += 1
#
# file_write.close()
# file_read.close()



