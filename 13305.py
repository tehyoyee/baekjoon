# 13305py

import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
price.append(0)
pivot = 0
result = 0

for i in range(len(price)):
	if price[pivot] > price[i]:
		result += price[pivot] * sum(dis[pivot:i])
		pivot = i
print(result)