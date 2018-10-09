# -*- coding:utf-8 -*-
import json
import sys
import logging
import pymysql
import os
import datetime
reload(sys)
sys.setdefaultencoding("utf-8")

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("LvchengPlusLog")
# 指定logger输出格式
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
logger.setLevel(logging.ERROR)
# 文件日志
file_handler = logging.FileHandler("/data/log/logdeal_script/LvchengPlus.log")
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

################ 初始连接到MySQL ######################
def connect_db():
    db = pymysql.connect(host="10.0.0.184",user="root",password="gt123",db="greentown_lvchengplus",port=3306,charset="utf8")
    return db

# 获取时间
date_input = sys.argv[1]
################### insert #####################################
def insert_db(db):
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    # 日志文件路径
    path_str_log = "/data/log/ideallife/log.log." + date_input

    # path_str_register = "/app/log/sso/" +  "register.log." + date_input
    # path_str_log = "/app/log/sso/" +  "register.log." + date_input
    # path_str_log = "/app/log/sso/" +  "register.log." + date_input
    # path_str_log = "/app/log/sso/" +  "register.log." + date_input


    # 判断文件是否存在
    if os.path.exists(path_str_log):
        with open(path_str_log, "r") as file_lvchengplus:
            for file_lines in file_lvchengplus.readlines():
                lines_file_lv = file_lines.strip()
                ###################### 1.处理 注册 日志 #################################
                if "register" in lines_file_lv:
                    sql_insert ="""insert into lvchengplus_register (`user_id`,`imei`,`logtype`,`record_time`,`os_type`,`app_version`,`channel_source`) values('%s','%s','%s','%s','%s','%s','%s')"""
                    try:
                        # 判断是否为完整记录
                        if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                            # 截取message
                            lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                            # 字符串转json
                            lines_message_dict = json.loads(lines_message)
                            # 插入数据库
                            cur.execute(sql_insert % (if_contain_key(lines_message_dict,"user_id"),
                                                      if_contain_key(lines_message_dict,"imei"),
                                                      if_contain_key(lines_message_dict,"logtype"),
                                                      format_time(if_contain_key(lines_message_dict,"record_time")),
                                                      if_contain_key(lines_message_dict,"os_type"),
                                                      if_contain_key(lines_message_dict,"app_version"),

                                                      if_contain_key(lines_message_dict,"channel_source")))
                            db.commit()
                    except ValueError as err:
                        logger.error(err)
                ###################### 2.处理 打开App 日志 #################################
                elif "open" in lines_file_lv:
                    sql_insert ="""insert into lvchengplus_open (`user_id`,`imei`,`logtype`,`record_time`,`os_type`,`app_version`,`channel_source`) values('%s','%s','%s','%s','%s','%s','%s')"""
                    try:
                        # 判断是否为完成记录
                        if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                            # 截取message
                            lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                            # 字符串转json
                            lines_message_dict = json.loads(lines_message)
                            # 插入数据库
                            cur.execute(sql_insert % (if_contain_key(lines_message_dict,"user_id"),
                                                      if_contain_key(lines_message_dict,"imei"),
                                                      if_contain_key(lines_message_dict,"logtype"),
                                                      format_time(if_contain_key(lines_message_dict,"record_time")),
                                                      if_contain_key(lines_message_dict,"os_type"),
                                                      if_contain_key(lines_message_dict,"app_version"),

                                                      if_contain_key(lines_message_dict,"channel_source")))
                            db.commit()
                    except ValueError as err:
                        logger.error(err)

                ###################### 3.处理 首页tab 日志 #################################
                elif "homepage_tab" in lines_file_lv:
                    sql_insert ="""insert into lvchengplus_homepage_tab (`user_id`,`imei`,`logtype`,`record_time`,`os_type`,`app_version`,`type`) values('%s','%s','%s','%s','%s','%s','%s')"""
                    try:
                        # 判断是否为完成记录
                        if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                            # 截取message
                            lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                            # 字符串转json
                            lines_message_dict = json.loads(lines_message)
                            # 插入数据库
                            cur.execute(sql_insert % (if_contain_key(lines_message_dict,"user_id"),
                                                      if_contain_key(lines_message_dict,"imei"),
                                                      if_contain_key(lines_message_dict,"logtype"),
                                                      format_time(if_contain_key(lines_message_dict,"record_time")),
                                                      if_contain_key(lines_message_dict,"os_type"),
                                                      if_contain_key(lines_message_dict,"app_version"),

                                                      if_contain_key(lines_message_dict,"type")))
                            db.commit()
                    except ValueError as err:
                        logger.error(err)

                ###################### 4.处理 首页button 日志 #################################
                if "homepage_button" in lines_file_lv:
                    sql_insert ="""insert into lvchengplus_homepage_button (`user_id`,`imei`,`logtype`,`record_time`,`os_type`,`app_version`,`type`) values('%s','%s','%s','%s','%s','%s','%s')"""
                    try:
                        # 判断是否为完成记录
                        if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                            # 截取message
                            lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                            # 字符串转json
                            lines_message_dict = json.loads(lines_message)
                            # 插入数据库
                            cur.execute(sql_insert % (if_contain_key(lines_message_dict,"user_id"),
                                                      if_contain_key(lines_message_dict,"imei"),
                                                      if_contain_key(lines_message_dict,"logtype"),
                                                      format_time(if_contain_key(lines_message_dict,"record_time")),
                                                      if_contain_key(lines_message_dict,"os_type"),
                                                      if_contain_key(lines_message_dict,"app_version"),

                                                      if_contain_key(lines_message_dict,"type")))
                            db.commit()
                    except ValueError as err:
                        logger.error(err)

############################ 判断是否存在key ##############
def if_contain_key(dict_lines={}, str_key=str):
    # if dict_lines.has_key(str_key):
    #     return str(dict_lines[str_key])
    # else:
    #     return "null"
    return str(dict_lines[str_key]) if dict_lines.has_key(str_key) else "null"

############################ unix时间戳转时间 ##############
def format_time(time_org):
    if str(time_org).isdigit():
        time_org = float(time_org)
        try:
            dt =  datetime.datetime.utcfromtimestamp(time_org/1000)
            dt = dt + datetime.timedelta(hours=8)
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError as err:
            print err.message

insert_db(connect_db())