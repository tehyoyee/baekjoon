# 11052.py

n = int(input())
arr = [0]
arr += list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
	dp[i] = arr[i]
	for j in range(1, (i + 2) // 2):
		dp[i] = max(dp[i], dp[j] + dp[i - j])
print(dp[n])
