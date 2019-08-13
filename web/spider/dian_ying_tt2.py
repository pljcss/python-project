# -*- coding:utf-8 -*-
from lxml import etree
from bs4 import BeautifulSoup
import sys
import re
from web.spider.dian_ying_tt import download

# reload(sys)
# sys.setdefaultencoding('utf-8')

def parse_movie_url(url):
    # html = download("http://www.ygdy8.net/html/gndy/dyzz/20181025/57658.html")
    html = download(url)
    htmlEmt = etree.HTML(html)
    # result = htmlEmt.xpath('//div[@id="Zoom"]')[0].xpath('string(.)')

    soup = BeautifulSoup(html, 'html.parser')
    fixed_html = soup.prettify()

    page_res = soup.find('div', attrs={'id':'Zoom'}).find('p')

    movie_type = ""

    for page_line in page_res:
        # print page_line
        page_line_str = str(page_line)

        if "译　　名" in page_line_str:
            label = page_line_str[18:].strip()
            movie_type = movie_type + label + ","
        elif "年　　代" in page_line_str:
            label = ""
            try:
                label = re.findall(r"(\d\d\d\d)", page_line_str)[0]
            except BaseException as e:
                print(e.message)
            movie_type = movie_type + label + ","
        elif "产　　地" in page_line_str:
            label = page_line_str[18:].strip()
            movie_type = movie_type + label + ","
        elif "类　　别" in page_line_str:
            label = page_line_str[18:].strip()
            movie_type = movie_type + label + ","
        elif "上映日期" in page_line_str:
            label = page_line_str[18:].strip()
            movie_type = movie_type + label + ","
        elif "IMDb评分" in page_line_str:
            label = ""
            try:
                label = re.findall(r"(\d\.\d)", page_line_str)[0]
            except BaseException as e:
                print(e.message)
            movie_type = movie_type + label + ","
        elif "豆瓣评分" in page_line_str:
            label = ""
            try:
                label = re.findall(r"(\d\.\d)", page_line_str)[0]
            except BaseException as e:
                print(e.message)
            movie_type = movie_type + label

    print(movie_type,url)
    return movie_type + ',' + url

with open('/Users/saicao/Desktop/movie_file1.txt', 'r') as f:
    for line in f.readlines():
        url =  line.split(',')[1]
        page_res = parse_movie_url(url)
        with open('/Users/saicao/Desktop/movie_res.txt', 'a+') as f1:
            f1.write(page_res.encode('utf-8'))


# parse_movie_url('http://www.ygdy8.net/html/gndy/dyzz/20181016/57613.html')
# parse_movie_url('http://www.ygdy8.net/html/gndy/jddy/20181024/57651.html')

# parse_movie_url('http://www.ygdy8.net/html/gndy/dyzz/20181025/57658.html')