# 1946.py

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	cut = 0
	n = int(input())
	check = [1] * (n)
	case = []
	for _ in range(n):
		case.append(list(map(int, input().split())))
	case.sort()
	print(case)
	for i in range(n - 1):
		cut = max(case[i][1], cut)
		for j in range(i + 1, n):
			if case[j][1] > cut:
				check[j] = 0
print(check)