# -*- coding:utf-8 -*-
import json
import sys
import logging
import pymysql
import os
import datetime

################ 初始连接到MySQL ######################
def connect_db():
    db = pymysql.connect(host="95.163.206.236",user="root",password="cs6255",db="moviedb",port=3306,charset="utf8")
    return db

def insert_db(db):
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql_insert ="""insert into movie (`name`,`time`,`area`,`category`,`time2`,`imdb`,`douban`,`url`) values('%s','%s','%s','%s','%s','%s','%s','%s')"""

    with open('/Users/saicao/Desktop/movie_res.txt') as f:
            for line in f.readlines():
                line_list = line.split(',')
                if len(line_list) == 8:
                    print line
                    try:
                        cur.execute(sql_insert % (line_list[0],line_list[1],line_list[2],line_list[3],line_list[4],line_list[5],line_list[6],line_list[7]))
                    except BaseException as e:
                        print e.message

                    db.commit()

insert_db(connect_db())

