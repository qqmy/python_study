# import socket
#
# # 创建socket
# sk = socket.socket()
# address = ('127.0.0.1',8006)  # 127.0.0.1 特殊的地址 可以代指本机地址
# sk.connect(address)
#
# data = sk.recv(1024) # 一次最大收1024字节   阻塞
# print(str(data,'utf-8'))
# sk.close()


# 小虎
import socket
sk = socket.socket()
address = ('127.0.0.1',8006)

sk.connect(address)
while True:
    inp = input('>>>')
    if inp == 'exit':   # 当客户端退出时或者主动断开连接时，服务端默认会接收到一个空内容，通过判断内容是否为空可以判定客户端是否断开连接
        break
    sk.send(bytes(inp,'utf8'))
    data = sk.recv(1024)
    print('-----',str(data,'utf8'))
sk.close()