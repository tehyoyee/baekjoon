# 2294.py
# 23.02.14. 16:19 ~ 16:33

n, k = map(int, input().split())
tokens = []
dp = [10001] * (k + 1)

for _ in range(n):
	tokens.append(int(input()))
for token in tokens:
	if token <= k:
		dp[token] = 1
for i in range(1, k + 1):
	if dp[i] != 10001:
		for token in tokens:
			if i + token <= k:
				dp[i + token] = min(dp[i] + 1, dp[i + token])
if dp[-1] == 10001:
	print(-1)
else:
	print(dp[-1])