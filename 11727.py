# 11727.py

import sys
input = sys.stdin.readline

n = int(input())
arr = []
arr.append(0)
arr.append(1)
if n >= 2:
	arr.append(3)
while (n >= 3):
	arr.append(2 * arr[-2] + arr[-1])
	n -= 1
print(arr[-1] % 10007)
