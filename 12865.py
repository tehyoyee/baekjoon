# 12865.py
# 14m

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * k * 2
for _ in range(n):
	a, b = map(int, input().split())
	# w[a].append(b)
	dp[a] += b
for i in range(1, n + 1):
	for j in range(1, n + 1):
		
print(dp)