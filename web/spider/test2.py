import requests
from urllib import request
from http import cookiejar
import random
import os
import datetime
import socket


def ex(x):
    if x > 1:
        x -= 1
        y=ex(x)
    # else:
    #     return x
    return ''

def tt():
    response = requests.get("https://www.baidu.com")

    return response

def ex1(x):
    res = tt()
    print(res.text)
    if x > 1:
        x -= 1
        return ex1(x)
    else:
        return "11111"


if __name__ == '__main__':
    # url = 'http://www.dianping.com/'
    #
    # t = ex1(2)
    #
    # print(t)
    #
    # t = ex(5)
    # print(t)

    with open("url_all.txt") as f:
        for i in f.readlines():
            print(i.strip().split('^')[3])