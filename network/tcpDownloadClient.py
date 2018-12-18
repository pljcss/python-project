# -*- coding:utf-8 -*-
import socket

def main():
    # 链接服务器
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('127.0.0.1', 7788))

    # 将要下载的文件名传给服务器
    download_filename = raw_input("请输入要下载的文件名")
    tcp_client_socket.send(download_filename.encode('utf-8'))

    # 接收数据,1024->1k; 1024*1024->1024*1k->1m;
    recv_data = tcp_client_socket.recv(1024)

    # 如果接收到数据,则创建文件
    if recv_data:
        # 将接收到的数据写入到新文件中
        with open("/Users/saicao/Desktop/new_" +  download_filename, 'wb') as f:
            f.write(recv_data)

    tcp_client_socket.close()

if __name__ == '__main__':
    main()