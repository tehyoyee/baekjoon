# 12015.py

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [0]

for x in lst:
	if dp[-1] < x:
		dp.append(x)
	else:
		start = 0
		end = len(dp)
		while start <= end:
			pivot = (start + end) // 2
			if pivot


# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = [0] + list(map(int, input().split()))
# dp = [0] * (n + 1)

# for i in range(1, n + 1):
# 	if lst[i] > lst[i - 1]:
# 		dp[i] += dp[i - 1] + 1
# 	else:
# 		for j in range(i):
# 			if lst[i] >= lst[j]:
# 				dp[i] = max(dp[i], dp[j])
# 		dp[i] += 1
# print(dp[n])