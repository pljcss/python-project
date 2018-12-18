# -*- coding:utf-8 -*-
import threading

global_num = 0

# 创建一个互斥锁,默认是没有上锁的
mutex = threading.Lock()

def add1(num):
    global global_num
    for i in range(0,num):
        # 上锁,如果之前没有上锁,那么此时上锁成功
        # 如果上锁之前已经被上锁了,那么此时会堵塞在这里,知道这个锁被解开
        mutex.acquire()
        global_num += 1
        # 解锁
        mutex.release()
    print global_num

def add2(num):
    global global_num
    for i in range(0,num):
        # 上锁,如果之前没有上锁,那么此时上锁成功
        # 如果上锁之前已经被上锁了,那么此时会堵塞在这里,知道这个锁被解开
        mutex.acquire()
        global_num += 1
        # 解锁
        mutex.release()
    print global_num

def main():
    t1 = threading.Thread(target=add1, args=(10000,))
    t2 = threading.Thread(target=add2, args=(10000,))

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()

