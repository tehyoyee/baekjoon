# 11054 py

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp_des = [0 for _ in range(n)]
for i in range(n):
	for j in range(0, i):
		if arr[i] > arr[j] and dp[i] < dp[j]:
			dp[i] = dp[j]
	dp[i] += 1
	
for i in range(n - 1, -1, -1):
	for j in range(i + 1, n):
		if arr[i] > arr[j] and dp_des[i] < dp_des[j]:
			dp_des[i] = dp_des[j]
	dp_des[i] += 1
max_ = 0
for i in range(n):
	max_ = max((dp[i] + dp_des[i]) - 1, max_)

print(max_)