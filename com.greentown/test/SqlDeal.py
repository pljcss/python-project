# -*- coding:utf8 -*-


sql_str = """
"SELECT " +
"city_company_name as projectName, " +
"ifnull(sum(1),0) as totalNums, " +
"ifnull(sum(CASE " +
"WHEN form_status = '3' THEN " +
"1 ELSE 0 END),0) as doneNums, " +
"ifnull(sum(CASE " +
"WHEN form_status != '3' THEN " +
"1 ELSE 0 END),0) as nodoneNums " +
"FROM (select distinct form_id,city_company_name,form_status,receive_time from final_kefu where city_company_name IS NOT NULL and city_company_name != '' ) as t " +
" where city_company_name is not null " +
"and receive_time>=#{start_time} and receive_time<=#{end_time} " +
"GROUP BY city_company_name"
"""

sql = sql_str.replace('"', "").replace('+', "")

print sql