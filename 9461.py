# 9461 py

import sys

input = sys.stdin.readline

dp = [0, 1, 1, 1, 2]

for i in range(5, 101):
	dp.append(dp[i - 1] + dp[i - 5])
t = int(input())
for _ in range(t):
	n = int(input())
	print(dp[n])