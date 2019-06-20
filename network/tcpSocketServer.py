# -*- coding:utf-8 -*-
import socket

def main():
    # 创建tcp 套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip、端口
    tcp_server_socket.bind(('127.0.0.1', 7788))

    # 让默认的套接字由主动变被动,128简单理解是可以同时有128个客户端链接
    # 但此种不是解决并发的方式,默认即可
    tcp_server_socket.listen(128)

    while True:
        # 等待客户端的链接 accept
        # 监听套接字负责等待有新的客户端链接, accept产生的新的套接字用来为客户端服务
        new_client_socket, client_addr = tcp_server_socket.accept()

        print(client_addr)
        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)
        print(recv_data)

        # 如果recv解堵塞, 那么有两种方式
        # 1、客户端发送过来数据
        # 2、客户端调用close
        if recv_data:

            # 给浏览器发送数据
            http_data = 'HTTP/1.1 200 OK \n' \
                        '\n' \
                        '<h1>hahaha</h1>'
            # 给客户端发送数据
            # new_client_socket.send("got it".encode('utf-8'))
            new_client_socket.send(http_data.encode('utf-8'))
        else:
            break

        # 关闭套接字
        new_client_socket.close()

    # 关闭套接字
    tcp_server_socket.close()

if __name__ == '__main__':
    main()