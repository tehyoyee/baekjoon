# 1416.py
# 23.03.20. 14:19 ~ 15:18 모르겠따 응응ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
book = list(map(int, input().split()))

left = []
right = []
for item in book:
    if item < 0:
        left.append(item)
    elif item > 0:
        right.append(item)

distance = []
left.sort()
for i in range(len(left)//m):
    distance.append(abs(left[m*i]))
if len(left) % m > 0:
    distance.append(abs(left[(len(left)//m)*m]))
    
right.sort(reverse = True)
for i in range(len(right)//m):
    distance.append(right[m*i]) 
if len(right) % m > 0:
    distance.append(right[(len(right)//m)*m])    
    
distance.sort()
result = distance.pop()
result += 2*sum(distance)
print(result)