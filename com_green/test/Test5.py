# -*- coding:utf-8 -*-
# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('www.sina.com.cn', 80)) # 参数是一个tuple, 包含地址和端口号

# 发送数据
str_http = """
GET / HTTP/1.1 
Host: www.sina.com.cn 
Connection: close   
"""

s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)


# 关闭连接:
s.close()

print(data)