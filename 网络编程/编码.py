# # str：Unicode
# #bytes：十六进制
#
# s = 'hello 猪八戒'
# print(type(s))   # <class 'str'>  Unicode
#
#
# # str 》》》》》bytes：编码
# # 方式1
# b = bytes(s, 'utf8')
# print(b)    # 将str变为十六进制的数  b'hello \xe7\x8c\xaa\xe5\x85\xab\xe6\x88\x92' utf8规则下的bytes类型
# # 方式二
# # b2 = s.encode('utf8')  # 编码
# # print(b2)
#
# # gbk编码下的bytes数据
# b3 = s.encode('gbk')
# print('gbk编码下的bytes',b3) # gbk编码下的bytes b'hello \xd6\xed\xb0\xcb\xbd\xe4'
#
#
# # 解码
# # 方式一
# # s1 = b2.decode('utf8')
# # print(s1)   # 按照什么规则编码就得按照什么规则解码
# # s2 = str(b2,'gbk')
# # print(s2)  # UnicodeDecodeError: 'gbk' codec can't decode byte 0xaa in position 8: illegal multibyte sequence
#
# # 解码方式二
# # s2 = str(b2,'utf8')
# # print(s2)   # str数据类型
#
# s3 = b3.decode('gbk')
# print(s3)  # hello 猪八戒


# 输入字符串1：I have a student.；输入字符串2: aeiou；
# 处理：在字符串1中，将字符串2中的字母删掉；输出：I hv stdnt.
def deal_str(data1,data2):
    l1 = list(data1)
    l2 = []
    length = len(l1)
    for i in range(length):
        if l1[i] in data2:
            continue
        else:
            l2.append(l1[i])

    return ''.join(l2)

print(deal_str('I have a student','aeiou'))