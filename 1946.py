# 1946.py

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	result = 1
	case = []
	for _ in range(n):
		case.append(list(map(int, input().split())))
	case.sort()
	cut = case[0][1]
	for i in range(1, n):
		if case[i][1] < cut:
			result += 1
			cut = case[i][1]
	print(result)
