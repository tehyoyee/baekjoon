# 16139 py

import sys
input = sys.stdin.readline

arr = input()
ret = ['']
n = int(input())
for i in range(len(arr) - 1):
	ret.append(arr[:i + 1])
for _ in range(n):
	a, l, r= input().split()
	l = int(l)
	r = int(r)
	result = ret[r + 1].count(a) - ret[l].count(a)
	print(result)
