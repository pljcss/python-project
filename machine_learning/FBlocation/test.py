# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt


def test():
    plt.figure(figsize=(10, 10))
    plt.scatter([60, 72, 75, 80, 83], [126, 151.1, 157.5, 168, 174.3])

    plt.show()
    return None

if __name__ == '__main__':
    test()