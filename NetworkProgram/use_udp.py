
import socket

# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，
# 而是直接接收来自任何客户端的数据
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    # 接受数据
    data, addr = s.recvfrom(1024)
    print('Received from %s: %s' % (addr, data))
    s.sendto(b'Hello, %s' % data, addr)
