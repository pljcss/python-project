# -*- coding:utf-8 -*-
import json

class Student(object):
    # 定义属性
    def __init__(self, name, score):
        self.name = name
        self.score = score

stu1 = Student('Lisa', 98) # 类实例化

# 定义student 转 dict方法
def student2dict(std):
    return {
        'name':std.name,
        'score':std.score
    }

# 成功序列化 Student类
print json.dumps(stu1, default=student2dict)

