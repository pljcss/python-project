# -*- coding:utf-8 -*-
import multiprocessing
import time


class MultiProcessDemo(multiprocessing.Process):

    def __init__(self, args):
        super(MultiProcessDemo, self).__init__()
        self.args = args


    def run(self):
        while True:
            time.sleep(1)
            print(self.args)
    # def run1(self):
    #     while True:
    #         time.sleep(1)
    #         print('1')
    #
    # def run2(self):
    #     print('2')


if __name__ == '__main__':
    c1 = MultiProcessDemo('1')
    c1.start()

    c2 = MultiProcessDemo('2')
    c2.start()