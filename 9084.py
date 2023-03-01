# 9084.py
# 23.03.01. 21:11 ~

import sys
input = sys.stdin.readline

result = []
t = int(input())
for _ in range(t):
	n = int(input())
	tokens = list(map(int, input().split()))
	target = int(input())
	dp = [0] * (target + 1)
	for token in tokens:
		i = 1
		while i * token <  target:
			dp[i * token] += 1
			i += 1
	tmp = 0
	for i in range(0, target // 2 + 1):
		# if dp[i] * dp[target - i] != 0:
			# tmp += 1
		tmp += (dp[i] * dp[target - i])
	result.append(tmp)
	print(dp)
for r in result:
	print(r)