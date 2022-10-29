# 12865.py

# 다시풀기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
goods = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
	a, b = map(int, input().split())
	goods.append([a, b])
for i in range(1, n + 1):
	for j in range(1, k + 1):
		w = goods[i][0]
		v = goods[i][1]
		if w > j:
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[n][k])
