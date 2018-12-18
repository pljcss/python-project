# -*- coding:utf-8 -*-
import socket

'''
udp 接收数据
'''
def main():
    # 创建一个udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地相关信息, 如果一个程序不绑定, 则系统会随机分配
    # ip地址和端口, 如果ip不写, 则表示本机的任何一个ip
    local_addr = ('127.0.0.1', 7788)
    udp_socket.bind(local_addr)

    # 接收数据,等待接收对方发送的数据, 1024表示本次接收的最大字节数
    # recv_data这个变量中存储的是一个元组, (接收的信息, (发送发的IP, port))
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]  # 接收到的数据
        send_addr = recv_data[1]  # 发送放的IP地址和端口
        # 打印接收到的数据
        print recv_data
        print '%s:%s' % (str(send_addr), recv_msg.decode('utf-8'))

        # 使用 socket发送数据
        send_data = raw_input("请输入返回数据: ")
        udp_socket.sendto(send_data.encode('utf-8'), ('127.0.0.1', 7789))

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()