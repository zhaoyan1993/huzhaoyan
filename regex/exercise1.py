# exercise1.py
import re
f=open('a.txt')
# pattern=r'[A-Z]\w+'
pattern=r'-?\d+\.?/?\d*%?'
l=[]
for line in f:
    l+=re.findall(pattern,line)
print(l)