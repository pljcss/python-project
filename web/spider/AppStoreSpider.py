# -*- coding:utf-8 -*-
import urllib3
import json

import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# url = 'https://itunes.apple.com/rss/customerreviews/id=529092160/json'

for page in range(1,1000):
    url = 'https://itunes.apple.com/rss/customerreviews/page=' + str(page) + '/id=957323480/sortby=mostrecent/json?l=en&&cc=cn'

    response = urllib3.urlopen(url)

    html = response.read()

    json_html = json.loads(html)

    json_list = json_html['feed']['entry']
    res_str = ''
    for line in json_list:
        res_str = res_str + line['title']['label'] + "\n"

    print(res_str)

    with open('/Users/saicao/Desktop/file1.txt', 'a+') as f:
        f.write(res_str)