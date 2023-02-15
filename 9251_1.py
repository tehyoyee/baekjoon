# 9251_1.py
# 23.02.15. 15:02 ~ 15:30 X

import sys
input = sys.stdin.readline

a = input()
b = input()
dp = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
	for j in range(1, len(b)):
		if a[i - 1] == b[j - 1]:
			dp[i][j] = dp[i - 1][j - 1] + 1
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
