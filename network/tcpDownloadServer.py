# -*- coding:utf-8 -*-
import socket

def send_file_2_client(new_client_socket, client_addr):
    file_name = new_client_socket.recv(1024).decode('utf-8')
    # print '客户端(%s)需要下载的文件是: %s' % (str(client_addr), file_name)
    print 'download file name: ' + file_name

    # 打开这个文件,读取数据
    file_content = None
    try:
        f = open('/Users/saicao/Desktop/'+file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print 'no this file: ' + file_name

    # 将文件数据发送给客户端,如果内容不为空,则将数据发送给客户端
    if file_content:
        new_client_socket.send(file_content)

    # 关闭客户端
    new_client_socket.close()

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('127.0.0.1', 7788))
    tcp_server_socket.listen(128)

    while True:
        new_client_socket,client_addr = tcp_server_socket.accept()

        # 调用文件发送函数
        send_file_2_client(new_client_socket, client_addr)
        # 关闭套接字
        new_client_socket.close()

    # 关闭套接字
    tcp_server_socket.close()

if __name__ == '__main__':
    main()