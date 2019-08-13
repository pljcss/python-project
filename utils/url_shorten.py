#-*- coding: utf-8 -*-

import requests
import json

url = 'https://dwz.cn/admin/v2/create'
method = 'POST'
content_type = 'application/json'

token = '566dd8c99091d125adb3ed479953a864'

# TODO：设置待创建的长网址
bodys = {'url':'https://m.gtdreamlife.com/#/activityDetail?id=d7d1f7f60f0244daafd9930c0f3b3cc5&activity=dx_act1_188'}

# 配置headers
headers = {'Content-Type':content_type, 'Token':token}

# 发起请求
response = requests.post(url=url, data=json.dumps(bodys), headers=headers)

# 读取响应
print(response.text)