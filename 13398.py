# 13398.py
# 23.03.09. 10:30 ~ x

n = int(input())
lst = list(map(int, input().split()))
dp = [[0] * n for _ in range(2)]
dp[0][0] = lst[0]
dp[1][0] = -1000
for i in range(1, n):
	dp[0][i] = max(dp[0][i - 1] + lst[i], lst[i])
	dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + lst[i])
print(max(max(dp[1]), max(dp[0])))
