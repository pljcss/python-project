# -*- coding:utf-8 -*-
import django
num = 100
nums = [100,200]
def test1():
    global num
    num += 100
    print("888888888888")


def test2():
    global nums
    nums += [300,400]


print(django.__path__)