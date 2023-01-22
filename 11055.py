# 11055py
# 23.01.22. 10:49 ~ 11:02

import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
	for j in range(i - 1, -1, -1):
		if lst[j] < lst[i]:
			dp[i] = max(dp[i], dp[j] + lst[i])

print(max(dp))