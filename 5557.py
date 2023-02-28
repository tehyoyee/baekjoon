# 5557.py
# 23.02.28. 13:48 ~ 14:30

n = int(input())
lst = list(map(int, input().split()))
dp = [[0] * (n - 1) for _ in range(21)]
dp[lst[0]][0] = 1
for j in range(1, n - 1):
	for i in range(0, 21):
		if 0 <= i + lst[j] <= 20:
			dp[i + lst[j]][j] += dp[i][j - 1]
		if 0 <= i - lst[j] <= 20:
			dp[i - lst[j]][j] += dp[i][j - 1]
print(dp[lst[-1]][-1])