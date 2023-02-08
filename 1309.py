# 1309.py
# 23.02.08. 18:05 ~

from collections import deque
n = int(input())
num = deque([1, 3, 7])
for n in range(2, 100):
	if n == 1:
		print(3)
	elif n == 2:
		print(7)
	else:
		for _ in range(n - 2):
			num[0] = (num[1] + ((num[2] * 2) % 9901)) % 9901
			num.rotate(-1)
		print(num[-1] % 9901)

num = [0, 3, 1]
if n == 1:
	print(1)
elif n == 2:
	print(3)
else:
	for _ in range(n - 2):
		


# import sys
# input = sys.stdin.readline
# n = int(input())
# dp = [0]*(n+1)
# for i in range(n+1) :
#     dp[i] = [0,0,0]
# dp[1][0] = 1
# dp[1][1] = 1
# dp[1][2] = 1


# for i in range(2, n + 1):
#     dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
#     dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
#     dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

# print(sum(dp[n]) % 9901)

# def bfs(i, limit, n):
# 	result = 0
# 	q = [[i, 1]]
# 	while q:
# 		cur, l = q.pop(0)
# 		if l == limit:
# 			result += 1
# 		else:
# 			if cur + 1 < n:
# 				q.append([cur + 1, l + 1])
# 			if cur + 2 < n:
# 				for k in range(cur + 2, n):
# 					q.append([k, l + 1])
# 					q.append([k, l + 1])
# 	return result

# for n in range(10):
# 	result = 1
# 	for limit in range(1, n + 1):
# 		for i in range(n):
# 			result += (bfs(i, limit, n) * 2)
# 	print(n, result)