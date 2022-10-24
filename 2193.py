# 2193.py

import sys
input = sys.stdin.readline

n = int(input())
if n == 1 or n == 2:
	print(1)
else:
	q = []
	q.append(1)
	q.append(1)
	for i in range(1, n - 1):
		q.append(q[1] + q.pop(0))
	print(q[1])