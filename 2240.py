# 2240.py
# 23.03.14. 09:59 ~ 11:39

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
a = b = 0
pwm = []


if int(input()) == 1:
	cur = 1
	a += 1
else:
	cur = 0
	b += 1
for i in range(T - 1):
	tmp = int(input())
	if tmp == 1:
		if a:
			a += 1
		else:
			pwm.append(b)
			a, b = 1, 0
	else:
		if b:
			b += 1
		else:
			pwm.append(a)
			a, b = 0, 1
if a:
	pwm.append(a)
elif b:
	pwm.append(b)
if len(pwm) <= 2:
	print(sum(pwm))
	exit()
dp = [[0] * len(pwm) for _ in range(W + 4)]

if cur:
	dp[0][0] = pwm[0]
	dp[1][0] = 0
	dp[0][1] = pwm[0]
	dp[1][1] = pwm[0] + pwm[1]
else:
	dp[0][0] = 0
	dp[1][0] = pwm[0]
	dp[0][1] = pwm[1]
	dp[1][1] = pwm[0]
	dp[2][1] = pwm[0] + pwm[1]

for j in range(1, len(pwm) - 1):
	for i in range(W + 1):
		if dp[i][j] != 0 and dp[i][j] == dp[i][j - 1]:
			dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + pwm[j + 1])
		else:
			dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
		if dp[i][j] != dp[i - 1][j - 1]:
			dp[i + 1][j + 1] = dp[i][j] + pwm[j + 1]

result = 0
for i in range(W + 1):
	result = max(dp[i][len(pwm) - 1], result)
print(result)