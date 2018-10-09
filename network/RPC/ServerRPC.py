# -*- coding:utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer

'''RPC Server'''
def add(x, y):
    print "调用了"
    return x +y

if __name__ == '__main__':

    # s 是一个绑定了本地 8081 端口的服务器对象
    s = SimpleXMLRPCServer(('127.0.0.1', 8881))

    # register_function()方法将函数add注册到s中
    s.register_function(add)

    # serve_forever() 启动服务器
    s.serve_forever()