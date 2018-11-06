# -*- coding:utf-8 -*-
import urllib2
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
tt = sys.getfilesystemencoding()

# 读取 url
def download(url, user_agent='wswp', num_retries=3):
    # print 'Downloading:', url
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read().decode('gbk').encode('utf-8')
        # 下载链接时, 不编码
        # html = urllib2.urlopen(request).read().decode('gbk').encode('utf-8')
    except urllib2.URLError as e:
        print 'Download Error: ', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 如果是 5xx http error 则重试
                return download(url, user_agent, num_retries-1)
    return html

# 解析url
def download_url(url):
    movie_url = ""
    html = download(url)
    htmlEmt = etree.HTML(html)
    result = htmlEmt.xpath('//a[2][@class="ulink"]')

    for line in result:
        mm =  line.xpath('text()')[0] + "," + "http://www.ygdy8.net" + line.xpath('@href')[0]
        movie_url = movie_url + mm + "\n"

    return movie_url


# with open('/Users/saicao/Desktop/movie_file1.txt', 'a+') as f:
#     for nums in range(2,203):
#         print 'page ',nums
#         url  = 'http://www.ygdy8.net/html/gndy/oumei/list_7_' + str(nums) + '.html'
#         f.write(download_url(url))


# print download("http://www.ygdy8.net/html/gndy/dyzz/20181025/57658.html")
# print download('http://www.ygdy8.net/html/gndy/jddy/20181019/57630.html')