# -*- coding:utf-8 -*-
import socket

'''
udp 发送数据
套接字可以同时收发数据
'''
def send_msg(udp_socket):
    """发送消息"""
    # 从键盘获取数据
    dest_ip = input("请输入对方ip:")
    dest_port = input("请输入对方port:")
    send_data = input("请输入要发送的数据:")

    # 使用套接字收发数据
    dest_addr = ('127.0.0.1', 7788)

    # dest_addr = ('192.168.32.166', 9000)
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

def recv_msg(udp_socket):
    """接收消息"""
    # 可以使用同一个socket接收数据
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)

def main():
    # 创建一个udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp发送数据可以不绑定端口, 此时会随机绑定一个端口
    udp_socket.bind(('127.0.0.1', 7789))
    while True:
        print('----xxx聊天室----')
        print('1: 发送消息')
        print('2: 接收消息')
        print('0: 退出系统')
        op = input("请输入选项")
        if op == '1':
            send_msg(udp_socket)
        elif op == '2':
            recv_msg(udp_socket)
        elif op == '0':
            break
        else:
            print('输入有误, 请重新输入')

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()