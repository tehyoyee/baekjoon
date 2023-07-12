# 9095.py
# 23.07.06. 20:08 ~ 20:23

import sys
input = sys.stdin.readline
T = int(input())

dp = [0, 1, 2, 4] + [0] * 7

for i in range(4, 11):
	dp[i] = sum(dp[i-3:i])

for _ in range(T):
	print(dp[int(input())])