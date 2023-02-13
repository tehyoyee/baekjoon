# 16194.py
# 23.02.13. 16:51 ~ 17:01

import copy

n = int(input())
cards = [0] + list(map(int, input().split()))
dp = copy.deepcopy(cards)
for i in range(1, n + 1):
	for j in range(1, n + 1):
		if i + j < n + 1:
			dp[i + j] = min(dp[i] + cards[j], dp[i + j])
print(dp)
