# test01.py
s=0
while True:
    n=int(input("请继续输入数字："))
    if n>=0:
        s=s+n
    else:
        
        print("所有数字的和是：",s)
        break
        