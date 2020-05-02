# import socket
#
# sk = socket.socket()
#
# print(sk)
# # 绑定ip地址和端口
# address = ('127.0.0.1',8006)
# sk.bind(address)
#
# # server端可以容纳的最大排队数
# sk.listen(3)
#
# # 等待客户端连接
# print('等待客户端连接....')
# conn,addr = sk.accept()
# # coon 是客户端的socket对象
# # print(conn)
#
# inp = input()
# conn.send(bytes(inp,'utf-8'))
#
# conn.close()  #  关闭和conn的连接
# sk.close()  # 关闭和所有人的连接

'''
server下的方法
bind（）
listen（）
accept()

recv()    用于接收，可以设置一次最大接收的长度，如果没有接收内容的话则会一直阻塞在这里
send()   可能一次发不过去
sendall()   一次次的发，一次发不过去接着发   传送的内容必须是byte类型

close()

client下的方法
connect（）
recv()
send()   可能一次发不过去
sendall()  

close()
一发一收
只要发送必须接收
'''









# 小虎追女神
# 女神
import socket
sk = socket.socket()
address = ('127.0.0.1',8006)
sk.bind(address)
sk.listen(3)

# 方式一
# conn, addr = sk.accept()
#
# while True:
#
#     data = conn.recv(1024)
#     if not data:    # 如果data为空，说明客户端已经断开连接了，服务端可以和下一个客户端进行连接了
#         conn.close()
#         conn,addr = sk.accept()
#         print(addr)
#         continue
#     print(str(data,'utf8'))
#     inp = input('>>>')
#     conn.send(bytes(inp,'utf8'))


# 方式二

# while True:
#     conn,addr = sk.accept()
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             conn.close()
#             break
#         print(str(data,'utf8'))
#         inp = input('>>>')
#         conn.send(bytes(inp,'utf8'))


# 方式三
while 1:
    conn, addr = sk.accept()
    print(addr)
    while 1:
        try:
            data = conn.recv(1024)   # 在Windows下，如果client端异常终止了，recv会报错，需要捕捉后处理一下
        except Exception:
            break
        if not data: break
        print('.........', str(data, 'utf8'))
        inp = input('>>>')
        conn.send(bytes(inp, 'utf8'))

sk.close()


