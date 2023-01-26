# 13549.py
# 23.01.22 16:01 ~

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
r = max(n, k)
dp = [j for j in range(n, -1, -1)] + [i for i in range(1, 2 * r + 1)]

if n >= k:
	print(n - k)
else:
	for i in range(n, 2* r):
		j = 1
		while i * j < r + r:
			dp[i * j] = min(dp[i * j], dp[i])
			j *= 2
	for i in range(n, 2 * r):
		dp[i] = min(dp[i - 1] + 1, dp[i], dp[i + 1] + 1)
		j = 1
		while i * j < r + r:
			dp[i * j] = min(dp[i * j], dp[i])
			j *= 2
	for i in range(1, r + r):
		dp[i] = min(dp[i - 1] + 1, dp[i], dp[i + 1] + 1)
	print(dp[k])