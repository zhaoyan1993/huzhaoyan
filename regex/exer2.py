# exer2.py
import re
import sys

def getAddr(port):
    f=open('./1.txt')
    while True:
        data=''
        for line in f:
            if line!='\n':
                data+=line
            else:
                break
        if not data:
            return 'have not such a message'
        try:
            PORT=re.match(r'\S+',data).group()
        except Exception as e:
            raise e
            continue
        if port==PORT:
            # addr=re.search(r'\w+\.\w+\.\w+',data).group()
            addr=re.search(r'(\d{1,3}\.){3}\d{1,3}/?\d+|Unknow',data).group()
            return addr
        
        

if __name__=='__main__':
    port=sys.argv[1]
    print(getAddr(port))