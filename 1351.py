# 1351.py
# 23.06.29. 12:42 ~

N, P, Q = map(int, input().split())

dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
	dp[i] = dp[i//P] + dp[i//Q]
print(dp[N])
# for i in range(1, N + 1):
# 	if dp[i] != dp[i - 1]:
# 		print(i, dp[i])
# 		# print("Y", end = "")
# 	# print()

# 	# 32 64 128