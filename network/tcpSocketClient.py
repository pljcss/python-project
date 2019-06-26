# -*- coding:utf-8 -*-
import socket

def main():
    # 创建tcp 套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # tcp client绑定端口, 也可以不绑定端口, 如果不绑定则随机启动一个端口
    tcp_client_socket.bind(('127.0.0.1', 12345))

    # 链接服务器
    tcp_client_socket.connect(('127.0.0.1', 7788))

    # 发送数据/接收数据
    send_data = input("请输入要发送的数据:")
    tcp_client_socket.send(send_data.encode('utf-8'))

    # 关闭套接字
    tcp_client_socket.close()
if __name__ == '__main__':
    main()