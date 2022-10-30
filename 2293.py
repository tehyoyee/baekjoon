# 2293.py

n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]
dp[0] = 1
token = []
for _ in range(n):
	token.append(int(input()))
for t in token:
	for i in range(1, k + 1):
		if i - t >= 0:
			dp[i] += dp[i - t]
print(dp[k])