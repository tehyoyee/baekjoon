# 2436.py
# 23.03.24. 00:00 ~ x

def gcd(num1, num2):
    if num2 % num1==0:
        return num1
    else:
        return gcd(num2%num1,num1)
    
a, b=map(int,input().split())
b //= a
res=[]
for i in range(1,b+1):
    if b % i==0:
        if i < b // i:
            if gcd(i, b//i)==1:
                res.append([i*a+(b//i)*a,i*a,(b//i)*a])
        else:
            if gcd(b//i,i)==1:
                res.append([i*a+(b//i)*a,(b//i)*a,i*a])
if len(res)>0:
    res.sort(key=lambda x:x[0])
    print(res[0][1],res[0][2])
