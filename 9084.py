# 9084.py
# 23.03.01. 90분

# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
# 	n = int(input())
# 	tokens = list(map(int, input().split()))
# 	target = int(input())
# 	dp = [0] * (target + 1)
# 	dp[0] = 1
# 	for token in tokens:
# 		tmp = [0] * (target + 1)
# 		for i in range(target):
# 			cnt = 1
# 			while i + token * cnt <= target:
# 				tmp[i + token * cnt] += dp[i]
# 				cnt += 1
# 		for i in range(target + 1):
# 			dp[i] += tmp[i]
# 	print(dp[-1])


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n = int(input())
	tokens = list(map(int, input().split()))
	target = int(input())
	dp = [0] * (target + 1)
	dp[0] = 1
	for token in tokens:
		print(dp)
		for i in range(1, target + 1):
			if i - token >= 0:
				dp[i] += dp[i - token]
	print(dp)
	print(dp[-1])