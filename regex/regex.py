# regex.py

import re

pattern=r'(ab)cd(ef)'
s='abcdefghojklabcdef'
regex=re.compile(pattern)
l=regex.findall(s)
# print(l)

l=re.split(r'\s+','hello world 你好　bye')
print(l)
l2=re.sub(r'\s+','$','hello world 你好　bye   hahah')
print('sub--',l2)