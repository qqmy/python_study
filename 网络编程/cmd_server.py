import subprocess
import socket

sk = socket.socket()
address = ('127.0.0.1',8008)
sk.bind(address)
sk.listen(3)

conn,addr = sk.accept()

while True:
    data = str(conn.recv(1024),'utf8')
    print(data)
    obj = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE)
    result = obj.stdout.read()   # 字节形式，可以通过str方法转换为字符串  Windows下默认是gbk编码。mac是utf8
    print(result)
    # 将命令的返回值大小传递给客户端
    result_len = len(result)
    conn.sendall(bytes(str(result_len),'utf8'))   # 当一次发送的内容较少时，连续发送可能和下一次的发送一起发过去，这个现象为粘包现象

    # 解决粘包问题  在两次连续发送之前添加一次接收
    conn.recv(1024)

    conn.sendall(result)
