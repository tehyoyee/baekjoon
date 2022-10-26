# 12865.py

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
goods = []

for _ in range(n):
	a, b = map(int, input().split())
	# w[a].append(b)
	dp[a] += b
	goods.append([a, b])
for i in range(1, k + 1):
	if dp[i] < 
print(goods)
print(dp)