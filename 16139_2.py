# 16139.py
# 23.02.07. 09:25 ~

# import sys
# input = sys.stdin.readline

# s = input()
# t = int(input())
# case = []
# for _ in range(t):
# 	a, b, c = input().split()
# 	a = ord(a) - 97
# 	b = int(b)
# 	c = int(c)
# 	case.append([a, b, c])

# dp = [[0] * 26 for _ in range(len(s))]
# for i in range(1, len(s)):
# 	dp[i][ord(s[i - 1]) - 97] = 1
# 	for j in range(26):
# 		dp[i][j] += dp[i - 1][j]
# for x in case:
# 	print(dp[x[2] + 1][x[0]] - dp[x[1]][x[0]])

import sys
input = sys.stdin.readline

s = input()
t = int(input())
dp = [[0] * 26 for _ in range(len(s))]
for i in range(1, len(s)):
	dp[i][ord(s[i - 1]) - 97] = 1
	for j in range(26):
		dp[i][j] += dp[i - 1][j]
for _ in range(t):
	a, b, c = input().split()
	a = ord(a) - 97
	b = int(b)
	c = int(c)
	print(dp[c + 1][a] - dp[b][a])