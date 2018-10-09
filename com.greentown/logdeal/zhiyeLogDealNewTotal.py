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
logger = logging.getLogger("zhiyeLog")
# 指定logger输出格式
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
logger.setLevel(logging.ERROR)
# 文件日志
file_handler = logging.FileHandler("/data/log/logdeal_script/zhiyeLog.log")
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

'''
python脚本处理置业绿城每日的埋点数据
'''
################ 初始连接到MySQL ######################
def connect_db():
    db = pymysql.connect(host="10.0.0.184",user="root",password="gt123",db="greentown_zhiye_new",port=3306,charset="utf8")
    return db

# 获取时间
# date_input = sys.argv[1]
################### insert #####################################
def insert_db(db):
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    ss = ['2018-04-17', '2018-04-18', '2018-04-19', '2018-04-20', '2018-04-21', '2018-04-22', '2018-04-23',
          '2018-04-24', '2018-04-25', '2018-04-26', '2018-04-27', '2018-04-28', '2018-04-29', '2018-04-30',
          '2018-05-01', '2018-05-02', '2018-05-03', '2018-05-04', '2018-05-05', '2018-05-06', '2018-05-07',
          '2018-05-08', '2018-05-09', '2018-05-10', '2018-05-11', '2018-05-12', '2018-05-13', '2018-05-14',
          '2018-05-15', '2018-05-16', '2018-05-17', '2018-05-18', '2018-05-19', '2018-05-20', '2018-05-21',
          '2018-05-22', '2018-05-23', '2018-05-24', '2018-05-25', '2018-05-26', '2018-05-27', '2018-05-28',
          '2018-05-29', '2018-05-30', '2018-05-31', '2018-06-01', '2018-06-02', '2018-06-03', '2018-06-04',
          '2018-06-05', '2018-06-06', '2018-06-07', '2018-06-08', '2018-06-09', '2018-06-10', '2018-06-11',
          '2018-06-12', '2018-06-13', '2018-06-14', '2018-06-15', '2018-06-16', '2018-06-17', '2018-06-18',
          '2018-06-19', '2018-06-20', '2018-06-21', '2018-06-22', '2018-06-23', '2018-06-24', '2018-06-25',
          '2018-06-26', '2018-06-27', '2018-06-28', '2018-06-29', '2018-06-30', '2018-07-01', '2018-07-02',
          '2018-07-03', '2018-07-04', '2018-07-05', '2018-07-06', '2018-07-07', '2018-07-08', '2018-07-09',
          '2018-07-10', '2018-07-11', '2018-07-12', '2018-07-13', '2018-07-14', '2018-07-15', '2018-07-16',
          '2018-07-17', '2018-07-18', '2018-07-19', '2018-07-20', '2018-07-21', '2018-07-22', '2018-07-23',
          '2018-07-24', '2018-07-25', '2018-07-26', '2018-07-27', '2018-07-28', '2018-07-29', '2018-07-30',
          '2018-07-31']

    for dateLog in ss:
        # 日志文件路径
        path_str_log = "/data/log/onlinesale/log.log." + dateLog

        # 判断文件是否存在
        if os.path.exists(path_str_log):
            with open(path_str_log, "r") as file_zhiye:
                for file_lines in file_zhiye.readlines():
                    lines_file_lv = file_lines.strip()
                    # 判断是否为完整日志
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取日志
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
                        ######################## PC端 #######################
                        ### PC visit
                        if lines_message_dict["logtype"] == "visit":
                            sql_insert ="""insert into pc_visit (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`present_url`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"present_url"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
                                db.commit()
                            except ValueError as err:
                                logger.error(err)
                        ### PC visit_time
                        elif lines_message_dict["logtype"] == "visit_time":
                            sql_insert ="""insert into pc_visit_time (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`enter_url`,`leave_url`,`enter_time`,`leave_time`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"enter_url"),
                                                          if_contain_key(lines_message_dict,"leave_url"),
                                                          if_contain_key(lines_message_dict,"enter_time"),
                                                          if_contain_key(lines_message_dict,"leave_time"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
                                db.commit()
                            except ValueError as err:
                                logger.error(err)
                        ### PC homepage_module_click
                        elif lines_message_dict["logtype"] == "homepage_module_click":
                            sql_insert ="""insert into pc_homepage_module_click (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`type`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"type"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
                                db.commit()
                            except ValueError as err:
                                logger.error(err)
                        ### PC homepage_ad_module_click
                        elif lines_message_dict["logtype"] == "homepage_ad_module_click":
                            sql_insert ="""insert into pc_homepage_ad_module_click (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`type`,`project_id`,`project_name`,`position`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"type"),
                                                          if_contain_key(lines_message_dict,"project_id"),
                                                          if_contain_key(lines_message_dict,"project_name"),
                                                          if_contain_key(lines_message_dict,"position"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
                                db.commit()
                            except ValueError as err:
                                logger.error(err)
                        ######################## 移动端 #######################
                        ### Mobile mobile_visit
                        elif lines_message_dict["logtype"] == "mobile_visit":
                            sql_insert ="""insert into mobile_visit (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`present_url`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"os_type"),
                                                          if_contain_key(lines_message_dict,"present_url"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
                                db.commit()
                            except ValueError as err:
                                logger.error(err)
                        ### Mobile mobile_visit_time
                        elif lines_message_dict["logtype"] == "mobile_visit_time":
                            sql_insert ="""insert into mobile_visit_time (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`enter_url`,`leave_url`,`enter_time`,`leave_time`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"os_type"),
                                                          if_contain_key(lines_message_dict,"enter_url"),
                                                          if_contain_key(lines_message_dict,"leave_url"),
                                                          if_contain_key(lines_message_dict,"enter_time"),
                                                          if_contain_key(lines_message_dict,"leave_time"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
                                db.commit()
                            except ValueError as err:
                                logger.error(err)
                        ### Mobile mobile_homepage_module_click
                        elif lines_message_dict["logtype"] == "mobile_homepage_module_click":
                            sql_insert ="""insert into mobile_homepage_module_click (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`type`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"os_type"),
                                                          if_contain_key(lines_message_dict,"type"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
                                db.commit()
                            except ValueError as err:
                                logger.error(err)
                        ### Mobile mobile_homepage_ad_module_click
                        elif lines_message_dict["logtype"] == "mobile_homepage_ad_module_click":
                            sql_insert ="""insert into mobile_homepage_ad_module_click (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`type`,`project_id`,`project_name`,`position`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"os_type"),
                                                          if_contain_key(lines_message_dict,"type"),
                                                          if_contain_key(lines_message_dict,"project_id"),
                                                          if_contain_key(lines_message_dict,"project_name"),
                                                          if_contain_key(lines_message_dict,"position"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
                                db.commit()
                            except ValueError as err:
                                logger.error(err)
                        ### Mobile mobile_homepage_tab
                        elif lines_message_dict["logtype"] == "mobile_homepage_tab":
                            sql_insert ="""insert into mobile_homepage_tab (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`type`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                            try:
                                # 插入数据库
                                cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                          if_contain_key(lines_message_dict,"user_id"),
                                                          if_contain_key(lines_message_dict,"user_agent"),
                                                          if_contain_key(lines_message_dict,"cookie"),
                                                          if_contain_key(lines_message_dict,"ip_addr"),
                                                          if_contain_key(lines_message_dict,"os_type"),
                                                          if_contain_key(lines_message_dict,"type"),
                                                          format_time(if_contain_key(lines_message_dict,"record_time")),
                                                          if_contain_key(lines_message_dict,"version")))
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