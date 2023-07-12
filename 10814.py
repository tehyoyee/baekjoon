# 10814.py
# 23.07.08. 01:57 ~

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
	a, b = input().split()
	lst.append([i, int(a), b])
lst.sort(key=lambda x:(x[1], x[0]))
for x in lst:
	print(x[1], x[2])