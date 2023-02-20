# 6588.py
# 23.02.20. 14:02 ~ 14:47

import sys
input = sys.stdin.readline
print = sys.stdout.write
import math

dp = [False] * 1000000
cur_range = 3

for i in range(3, 1000000, 2):
	flag = 0
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			flag = 1
			break
	if flag == 0:
		dp[i] = True

while True:
	n = int(input())
	if n == 0:
		break
	flag = 0
	for i in range(3, n // 2 + 1, 2):
		if dp[i] == True and dp[n - i] == True:
			print(f"{n} = {i} + {n - i}\n")
			flag = 1
			break
	if not flag:
		print("Goldbach's conjecture is wrong.\n")