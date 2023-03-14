# 2240.py
# 23.03.14. 09:59 ~

# import sys
# input = sys.stdin.readline

# T, W = map(int, input().split())
# a = b = 0
# pwm = []
# global result
# result = 0

# def dfs(cur, i, w, end, total):
# 	global result
# 	if i == end:
# 		result = max(total, result)
# 		return
# 	if cur:
# 		total += pwm[i]
# 		dfs(0, i + 1, w, end, total)
# 		if w:
# 			dfs(1, i + 1, w - 1, end, total)
# 	else:
# 		dfs(1, i + 1, w, end, total)
# 	return


# if int(input()) == 1:
# 	cur = 1
# 	a += 1
# else:
# 	cur = 0
# 	b += 1
# for i in range(T - 1):
# 	tmp = int(input())
# 	if tmp == 1:
# 		if a:
# 			a += 1
# 		else:
# 			pwm.append(b)
# 			a, b = 1, 0
# 	else:
# 		if b:
# 			b += 1
# 		else:
# 			pwm.append(a)
# 			a, b = 0, 1
# if a:
# 	pwm.append(a)
# elif b:
# 	pwm.append(b)

# if cur:
# 	dfs(1, 0, W, len(pwm), 0)
# else:
# 	dfs(0, 0, W, len(pwm), 0)
# 	dfs(1, 0, W - 1, len(pwm), 0)
# print(result)


# import sys
# input = sys.stdin.readline

# T, W = map(int, input().split())
# a = b = 0
# pwm = []


# if int(input()) == 1:
# 	cur = 1
# 	a += 1
# else:
# 	cur = 0
# 	b += 1
# for i in range(T - 1):
# 	tmp = int(input())
# 	if tmp == 1:
# 		if a:
# 			a += 1
# 		else:
# 			pwm.append(b)
# 			a, b = 1, 0
# 	else:
# 		if b:
# 			b += 1
# 		else:
# 			pwm.append(a)
# 			a, b = 0, 1
# if a:
# 	pwm.append(a)
# elif b:
# 	pwm.append(b)
# if len(pwm) <= 2:
# 	print(sum(pwm))
# 	exit()
# dp = [[0] * len(pwm) for _ in range(W + 3)]
# if cur:
# 	dp[0][0] = pwm[0]
# 	dp[1][0] = 0
# 	dp[0][1] = pwm[0]
# 	dp[1][1] = pwm[0] + pwm[1]
# else:
# 	dp[0][0] = 0
# 	dp[1][0] = pwm[0]
# 	dp[0][1] = pwm[1]
# 	dp[1][1] = pwm[0]
# 	dp[2][1] = pwm[0] + pwm[1]

# for j in range(2, len(pwm)):
# 	if dp[0][j - 1] == dp[0][j - 2]:
# 		dp[0][j] += pwm[j]
# 	else:
# 		dp[0][j] = dp[0][j - 1]	
# 	for i in range(1, j + 1):
# 		if dp[i][j - 1] != 0 and dp[i][j - 1] == dp[i][j - 2]:
# 			dp[i][j] += pwm[j]
# 		else:
# 			dp[i][j] = dp[i][j - 1]
# 		if dp[i - 1][j - 1] != dp[i - 1][j - 2]:
# 			dp[i][j] = dp[i - 1][j - 1] + pwm[j]

# result = 0
# for i in range(W + 1):
# 	result = max(dp[i][len(pwm) - 1], result)
# print(result)


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
	for i in range(j + 2):
		if dp[i][j] != 0 and dp[i][j] == dp[i][j - 1]:
			dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + pwm[j + 1])
		else:
			dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
		if dp[i][j] != dp[i - 1][j - 1]:
			dp[i + 1][j + 1] = dp[i][j] + pwm[j + 1]

result = 0
for x in dp:
	print(x)
for i in range(W + 1):
	result = max(dp[i][len(pwm) - 1], result)
print(result)