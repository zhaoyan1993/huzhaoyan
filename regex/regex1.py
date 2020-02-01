# regex1.py

import re

it=re.finditer(r'\d+','2008-2020,10年\
    时间啊')
for i in it:
    print(i.group())