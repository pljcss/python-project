# -*- coding:utf-8 -*-
import os

def gci(path):
    print(path)
    total_lines = 0
    with open(path) as files:
        for f in files:
            # print(f)
            with open(f.strip('\n')) as data:
                total_lines = total_lines + len(data.readlines())

    print(total_lines)

    return None


if __name__ == '__main__':
    path = "/Users/saicao/Desktop/readlines"
    gci(path)