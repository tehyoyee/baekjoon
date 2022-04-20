# 11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_ = 0
dp = [0]
for x in arr:
	sum_ += x
	dp.append(sum_)
for _ in range(m):
	a, b = map(int, input().split())
	print(dp[b] - dp[a - 1])