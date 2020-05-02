# 字符串反序输出
str = 'strrts'
# print(str[::-1])
# 判断回文
# print(str[::-1]==str)
# 统计python源代码文件中代码行数，去除注释，空行，进行输出）
import os

if __name__ == '__main__':
    codeline = 0
    expline = 0
    blankline = 0

    filename = input('please input file name: ')
    file = open(filename,'r')
    # print(file.readlines())
    for line in file:
        if line.strip().startswith('#'):
            expline +=1
        elif line=='\n':
            blankline +=1
        elif line.strip().startswith('"""') or line.strip().startswith("'''") :
            expline +=1
            while True:
                line = file.readline()
                expline +=1
                if line.strip().endswith('"""') or line.strip().endswith("'''"):
                    break
        else:
            codeline +=1
    # while fi.tell()!=os.path.getsize(filename):
    #     temp = fi.readline()
    #     if temp.startswith('#'):
    #         expline +=1
    #     elif temp=='/n':
    #         blankline +=1
    #     elif temp.startswith('"""'):
    #         expline +=1
    #         while True:
    #             temp = fi.readline()
    #             expline +=1
    #             if temp.endswith('"""/n'):
    #                 break
    #     else:
    #         codeline +=1
    # else:
    """
    hahah
    hahah
    """
    '''  print('the codeline is:',codeline)
        print('the expline is:',expline)
        print('the blankline is:',blankline)
    '''
    file.close()
    print('the codeline is:', codeline)
    print('the expline is:',expline)
    print('the blankline is:',blankline)
