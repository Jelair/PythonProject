
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 9999))
    # 接受数据
    # 从服务器接收数据仍然调用recv()方法
    print(s.recv(1024).decode('utf-8'))

s.close()