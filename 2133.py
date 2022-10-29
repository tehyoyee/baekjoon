# 2133.py

n = int(input())

if n % 2:
	print('0')
else:
	n //= 2
	dp = [0, 3]
	for i in range(2, n + 1):
		dp.append(dp[-1] * 3 + sum(dp[:i - 1]) * 2 + 2)
	print(dp[n])