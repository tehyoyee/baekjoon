# 5525.py
# 23.02.02. 13:39 ~

n = int(input())
m = int(input())
s = input()

dp = [0] * m
cnt = 0
for i in range(m):
	if s[i:i+3] == "IOI":
		for j in range(2):
			dp[i + j] = dp[i - 1] + 1
	elif dp[i] == 0 and dp[i - 1] >= n:
		cnt += dp[i - 1] - n + 1

print(cnt)