# 5582.py
# 23.03.02.17:58 ~ 18:28 03.03. 08:30 ~

import sys
input = sys.stdin.readline

s1 = input()
s2 = input()
dp = [[0] * (len(s2)) for _ in range(len(s1))]
result = 0
for i in range(len(s1) - 1):
	for j in range(len(s2) - 1):
		if s1[i] == s2[j]:
			dp[i][j] += (dp[i - 1][j - 1] + 1)
			result = max(dp[i][j], result)
print(result)