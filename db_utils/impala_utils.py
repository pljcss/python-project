from impala.dbapi import connect
from impala.util import as_pandas
import sys
import os

# os.environ['HADOOP_USER_NAME'] = 'impala'
conn = connect(host='BI-HD05', port=21050,)

print(conn)
cur = conn.cursor(user='bibi_data')
sql = 'SELECT 1 FROM    ods.T_USER_INFO_HIST A LIMIT 1;'


cur.execute(sql)
data = cur.fetchall()


cur.execute('select user();')

print()

print (data)