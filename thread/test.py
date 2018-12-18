# -*- coding:utf-8 -*-

num = 100
nums = [100,200]
def test1():
    global num
    num += 100

def test2():
    global nums
    nums += [300,400]

print num
test1()
print num

print nums
test2()
print nums