# 1697.py

n, k = map(int, input().split())

if n > k:
	print(n - k)
	exit()
dp = [0 for _ in range(100002)]
for i in range(n, 100002):
	dp[i] = i - n
for i in range(n, -1, -1):
	dp[i] = n - i
for i in range(1, 100001):
	dp[i - 1] = min(dp[i] + 1, dp[i - 1])
	dp[i + 1] = min(dp[i] + 1, dp[i + 1])
	while i < 50001:
		dp[i * 2] = min(dp[i] + 1, dp[i * 2])
		dp[i - 1] = min(dp[i] + 1, dp[i - 1])
		dp[i + 1] = min(dp[i] + 1, dp[i + 1])
		i *= 2
print(dp[k])