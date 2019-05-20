# -*- coding:utf-8 -*-
import configparser
import sys

def config_init():
    cf = configparser.ConfigParser()
    cf.read("fileDemo.ini")

    # sections
    secs = cf.sections()
    print(secs)

    # options
    opts = cf.options("mysql")
    print(opts)

    # kvs
    kvs = cf.items("mysql")
    print(kvs)

    str_val = cf.get("mysql", "host")
    int_val = cf.getint("mysql", "port")
    print(str_val)
    print(int_val)

    return None

if __name__ == '__main__':
    print(len(sys.argv))
    print(sys.argv[0])
    if len(sys.argv) < 2:
        exit(0)

    config_init()
