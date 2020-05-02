# 从明文转换成密文

import hashlib
'''
'abc' 》》》》》md5》》》》》'pkjjlkhjgyugygyog'
'''
# m = hashlib.md5()
# print(m)
# m.update('hello'.encode('utf-8'))
# print(m.hexdigest())  # 取出加密后的结果十六进制表达方式：5d41402abc4b2a76b9719d911017c592
# m.update('alex'.encode('utf-8'))
# print(m.hexdigest())
#
# # python3中存的是Unicode类型 byte类型
# # python3默认用utf-8编码
#
# m2 = hashlib.md5()
# m2.update('hello wordalex'.encode('utf-8'))  # 相当于上面的两步
# print(m.hexdigest())

# sha加密
s = hashlib.sha256()
s.update('hello word'.encode('utf-8'))
print(s.hexdigest())  # f0da559ea59ced68b4d657496bee9753c0447d70702af1a351c7577226d97723