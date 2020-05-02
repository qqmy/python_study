# 远程执行命令
import socket

sk = socket.socket()
address = ('127.0.0.1',8008)

sk.connect(address)

while True:
    inp = input('请输入命令：')
    sk.send(bytes(inp,'utf8'))
    length = int(str(sk.recv(1024),'utf8'))
    print(length)
    sk.send(bytes('ok','utf8'))  # 为了解决粘包问题，发送内容可以为任意值
    data = bytes()
    while length!=len(data):   # 当接收的内容超出设置的1024时，需要多次接收，此时就需要一个循环来控制接收的次数
        data += sk.recv(1024)
    print('---',str(data,'gbk'))

