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
logger = logging.getLogger("zhiyeLogdeal")
# 指定logger输出格式
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
logger.setLevel(logging.INFO)
# 文件日志
file_handler = logging.FileHandler("/data/log/logdeal/zhiyeLogdeal.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# 指定日志的最低输出级别，默认为WARN级别
file_handler.setLevel(logging.INFO)
console_handler.setLevel(logging.ERROR)
# 移除一些日志处理器
# logger.removeHandler(file_handler)

################ 初始连接到MySQL ######################
def connect_db():
    db = pymysql.connect(host="10.0.0.184",user="root",password="gt123",db="greentown_zhiye",port=3306,charset="utf8")
    return db

# 输入时间[时间格式 2018-02-07]
date_input = sys.argv[1]

################### insert #####################################
def insert_db(db):
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    # PC端 浏览日志
    path_str_visit = "/data/log/onsale/pc/visit/visit." + date_input + ".log"
    # PC端 访问时长日志
    path_str_visit_time = "/data/log/onsale/pc/visit/visit_time." + date_input + ".log"
    # PC端 首页模块点击日志
    path_str_homepage_module_click = "/data/log/onsale/pc/visit/homepage_module_click." + date_input + ".log"
    # PC端 首页广告模块点击日志
    path_str_homepage_ad_module_click = "/data/log/onsale/pc/visit/homepage_ad_module_click." + date_input + ".log"

    ###################### 1.处理 PC端 浏览日志 #################################
    path_visit = unicode(path_str_visit)
    # 判断文件是否存在
    if os.path.exists(path_visit):
        sql_insert ="""insert into pc_visit (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`present_url`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_visit,"r") as file_lv:
            logger.info("开始读取PC端浏览日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
                        # 插入数据库
                        cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                  if_contain_key(lines_message_dict,"user_id"),
                                                  if_contain_key(lines_message_dict,"user_agent"),
                                                  if_contain_key(lines_message_dict,"cookie"),
                                                  if_contain_key(lines_message_dict,"ip_addr"),
                                                  if_contain_key(lines_message_dict,"present_url"),
                                                  if_contain_key(lines_message_dict,"record_time"),
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")

    ###################### 2.处理 PC端访问时长 日志 #################################
    path_visit_time = unicode(path_str_visit_time)
    # 判断文件是否存在
    if os.path.exists(path_visit_time):
        sql_insert ="""insert into pc_visit_time (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`enter_url`,`leave_url`,`enter_time`,`leave_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_visit_time,"r") as file_lv:
            logger.info("开始读取PC端访问时长日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
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
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")

    ###################### 3.处理 PC端首页模块点击日志 #################################
    path_homepage_module_click = unicode(path_str_homepage_module_click)
    # 判断文件是否存在
    if os.path.exists(path_homepage_module_click):
        sql_insert ="""insert into pc_homepage_module_click (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`type`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_homepage_module_click,"r") as file_lv:
            logger.info("开始PC端首页模块点击日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
                        # 插入数据库
                        cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                  if_contain_key(lines_message_dict,"user_id"),
                                                  if_contain_key(lines_message_dict,"user_agent"),
                                                  if_contain_key(lines_message_dict,"cookie"),
                                                  if_contain_key(lines_message_dict,"ip_addr"),
                                                  if_contain_key(lines_message_dict,"type"),
                                                  if_contain_key(lines_message_dict,"record_time"),
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")

    ###################### 4.处理 PC端首页广告模块点击日志 #################################
    path_homepage_ad_module_click = unicode(path_str_homepage_ad_module_click)
    # 判断文件是否存在
    if os.path.exists(path_homepage_ad_module_click):
        sql_insert ="""insert into pc_homepage_ad_module_click (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`type`,`project_id`,`project_name`,`position`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_homepage_ad_module_click,"r") as file_lv:
            logger.info("开始PC端首页广告模块点击日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
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
                                                  if_contain_key(lines_message_dict,"record_time"),
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")


    # Mobile端
    path_str_visit_m = "/data/log/onsale/mobile/mobile_visit/mobile_visit." + date_input + ".log"
    ###################### 1.处理 Mobile端 浏览日志 #################################
    path_visit_m = unicode(path_str_visit_m)
    # 判断文件是否存在
    if os.path.exists(path_visit_m):
        sql_insert ="""insert into mobile_visit (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`present_url`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_visit_m,"r") as file_lv:
            logger.info("开始读取移动端浏览日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
                        # 插入数据库
                        cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                  if_contain_key(lines_message_dict,"user_id"),
                                                  if_contain_key(lines_message_dict,"user_agent"),
                                                  if_contain_key(lines_message_dict,"cookie"),
                                                  if_contain_key(lines_message_dict,"ip_addr"),
                                                  if_contain_key(lines_message_dict,"os_type"),
                                                  if_contain_key(lines_message_dict,"present_url"),
                                                  if_contain_key(lines_message_dict,"record_time"),
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")


    ###################### 2.处理 Mobile端 访问时长日志 #################################
    path_str_visit_time_m = "/data/log/onsale/mobile/mobile_visit/mobile_visit_time." + date_input + ".log"
    path_visit_time_m = unicode(path_str_visit_time_m)
    # 判断文件是否存在
    if os.path.exists(path_visit_time_m):
        sql_insert ="""insert into mobile_visit_time (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`enter_url`,`leave_url`,`enter_time`,`leave_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_visit_time_m,"r") as file_lv:
            logger.info("开始读取移动端访问时长日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
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
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")


    ###################### 3.处理 移动端首页模块点击 日志 #################################
    path_str_homepage_module_click_m = "/data/log/onsale/mobile/mobile_visit/mobile_homepage_module_click." + date_input + ".log"
    path_homepage_module_click_m = unicode(path_str_homepage_module_click_m)
    # 判断文件是否存在
    if os.path.exists(path_homepage_module_click_m):
        sql_insert ="""insert into mobile_homepage_module_click (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`type`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_homepage_module_click_m,"r") as file_lv:
            logger.info("开始移动端首页模块点击日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
                        # 插入数据库
                        cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                  if_contain_key(lines_message_dict,"user_id"),
                                                  if_contain_key(lines_message_dict,"user_agent"),
                                                  if_contain_key(lines_message_dict,"cookie"),
                                                  if_contain_key(lines_message_dict,"ip_addr"),
                                                  if_contain_key(lines_message_dict,"os_type"),
                                                  if_contain_key(lines_message_dict,"type"),
                                                  if_contain_key(lines_message_dict,"record_time"),
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")

    ###################### 4.处理 移动端首页广告模块点击日志 #################################
    path_str_mobile_homepage_ad_module_click_m = "/data/log/onsale/mobile/mobile_visit/mobile_homepage_ad_module_click." + date_input + ".log"
    path_mobile_homepage_ad_module_click_m = unicode(path_str_mobile_homepage_ad_module_click_m)
    # 判断文件是否存在
    if os.path.exists(path_mobile_homepage_ad_module_click_m):
        sql_insert ="""insert into mobile_homepage_ad_module_click (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`type`,`project_id`,`project_name`,`position`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_mobile_homepage_ad_module_click_m,"r") as file_lv:
            logger.info("开始移动端首页广告模块点击日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
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
                                                  if_contain_key(lines_message_dict,"record_time"),
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")

    ###################### 5.处理 移动端首页底部Tab点击 日志 #################################
    path_str_mobile_homepage_tab_m = "/data/log/onsale/mobile/mobile_visit/mobile_homepage_tab." + date_input + ".log"
    path_mobile_homepage_tab_m = unicode(path_str_mobile_homepage_tab_m)
    # 判断文件是否存在
    if os.path.exists(path_mobile_homepage_tab_m):
        sql_insert ="""insert into mobile_homepage_tab (`logtype`,`user_id`,`user_agent`,`cookie`,`ip_addr`,`os_type`,`type`,`record_time`,`version`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        # 读取文件
        with open(path_mobile_homepage_tab_m,"r") as file_lv:
            logger.info("开始移动端首页底部Tab点击日志")
            # 遍历文件的每一行记录
            for lines_file_lv in file_lv.readlines():
                try:
                    # 判断是否为完成记录
                    if lines_file_lv.find("{") and lines_file_lv.find("}") != -1:
                        # 截取message
                        lines_message = lines_file_lv[lines_file_lv.index("{"):].strip()
                        # 字符串转json
                        lines_message_dict = json.loads(lines_message)
                        # 插入数据库
                        cur.execute(sql_insert % (if_contain_key(lines_message_dict,"logtype"),
                                                  if_contain_key(lines_message_dict,"user_id"),
                                                  if_contain_key(lines_message_dict,"user_agent"),
                                                  if_contain_key(lines_message_dict,"cookie"),
                                                  if_contain_key(lines_message_dict,"ip_addr"),
                                                  if_contain_key(lines_message_dict,"os_type"),
                                                  if_contain_key(lines_message_dict,"type"),
                                                  if_contain_key(lines_message_dict,"record_time"),
                                                  if_contain_key(lines_message_dict,"version")))
                        db.commit()
                except ValueError as err:
                    logger.error(err)
    else:
        logger.info("没有该文件")



############################ 判断是否存在key ##############
def if_contain_key(dict_lines={}, str_key=str):
    # if dict_lines.has_key(str_key):
    #     return str(dict_lines[str_key])
    # else:
    #     return "null"
    return str(dict_lines[str_key]) if dict_lines.has_key(str_key) else "null"


insert_db(connect_db())