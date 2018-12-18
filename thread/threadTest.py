# -*- coding:utf-8 -*-
import time
import threading

def sing():
    for i in range(50000):
        print "sing a song"
        time.sleep(1)


def dance():
    for i in range(50000):
        print "dance"
        time.sleep(1)


def main():
    """非多任务环境下,唱歌跳舞只能依次执行"""
    # sing()
    # dance()

    # 注意,target后的方法名不需要加括号,写括号代表调用函数;不写代表告诉target函数在哪
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    # enumerate可以显示当前运行的所以线程
    # 共三个线程,主线程和两个子线程(但是不一定,因为线程的执行是部分先后顺序的)
    print threading.enumerate()

if __name__ == '__main__':
    main()