# 1850.py
# 23.02.14. 15:39 ~ x

def gcd(a, b) :
    if b == 0 :
        return a
    else :
        return gcd(b, a % b)

a, b = map(int,input().split())

print('1' * gcd(a, b))