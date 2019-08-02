#!/usr/bin/python
import re

if re.match('^\d{4}-\d{2}-\d{2}$', '2112-22-22'):
    print("匹配成功")

else:
    print("未匹配成功")