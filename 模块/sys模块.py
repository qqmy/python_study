# 用于跟python解释器进行交互

import sys
# print(sys.argv)
# 执行：python sys模块.py post download
# 结果：['sys模块.py', 'post', 'download']

def post():
    print('post')

def download():
    print('download')

# if sys.argv[1] =='post':
#     post()
# elif sys.argv[1] == 'download':
#     download()

# sys.exit(0) # 0表示正常退出
import time
print(sys.path)
print(sys.platform)  # 返回操作系统平台名称
val = sys.stdin.readline()  # 输入
sys.stdout.write(val)  # 输出

