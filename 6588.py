# 6588.py
# 23.02.20. 14:02 ~ 14:47

import sys
input = sys.stdin.readline
import math

dp = [False] * 1000000
cur_range = 3
def search(last_range, cur_range):
	for i in range(last_range, cur_range):
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
	if cur_range < n:
		last_range = cur_range
		cur_range = n
		search(last_range, cur_range)
	flag = 0
	for i in range(3, n // 2 + 1):
		if dp[i] == True and dp[n - i] == True:
			print(n, "=", i, "+", n - i)
			flag = 1
			break
	if not flag:
		print("Goldbach's conjecture is wrong.")