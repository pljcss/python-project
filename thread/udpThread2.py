# -*- coding:utf-8 -*-
import threading
import socket

'''多线程版udp聊天器'''
def recv_msg(udp_socket):
    """接收数据并显示"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print recv_data


def send_msg(udp_socket):
    """发送数据"""
    while True:
        send_data = raw_input('请输入要发送的数据')
        udp_socket.sendto(send_data.encode('utf-8'), ('127.0.0.1', 7788))

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('127.0.0.1', 7789))

    # 创建2个线程去,去执行相应的功能
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket,))

    t_recv.start()
    t_send.start()

if __name__ == '__main__':
    main()