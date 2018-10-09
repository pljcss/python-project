# -*- coding:utf8 -*-
import json

d = {'name':'Bob','age':20, 'score':88}

# python对象 转 json
print json.dumps(d)

# 写入json
with open("/Users/saicao/Desktop/filetest/ser.txt",'wb') as f:
    json.dump(d, f)


json_str = '{"age": 20, "score": 88, "name": "Bob"}'

# json 反序列化为 python 对象
print json.loads(json_str)

# 从文件中读取json
with open("/Users/saicao/Desktop/filetest/ser.txt",'rb') as f:
    print json.load(f)





