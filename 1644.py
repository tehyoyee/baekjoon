# 1644.py
# 23.04.04. 13:27 ~ 13:48

#21분
def set_dp():
	dp[0] = 0
	dp[1] = 0
	for i in range(2, (N//2)+1):
		for j in range(2, N//i+1):
			dp[i*j] = 0

result = 0
N = int(input())
dp = [i for i in range(N+1)]
set_dp()
sets = set(dp)
dp = sorted(list(sets))
for i in range(1, len(dp)):
	dp[i] += dp[i - 1]
key1, key2 = 0, 1

while key1 < len(dp) and key2 < len(dp):
	if dp[key2] - dp[key1] == N:
		key1 += 1
		key2 += 1
		result += 1
	elif dp[key2] - dp[key1] > N:
		key1 += 1
	else:
		key2 += 1

print(result)