# -*- coding:utf8 -*-
import logging
import sys

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("Logtest")
# 指定logger输出格式
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
logger.setLevel(logging.ERROR)
# 文件日志
file_handler = logging.FileHandler("/Users/saicao/Desktop/pythonLogTest/Logtest.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# 指定日志的最低输出级别，默认为WARN级别
file_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.ERROR)
# 移除一些日志处理器
# logger.removeHandler(file_handler)


def use_logging(func):
    logging.warn("%s is running" % func.__name__)
    func()

def foo():
    print('i am foo')

use_logging(foo)
