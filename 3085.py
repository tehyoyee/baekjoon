# 3085.py

import sys
input = sys.stdin.readline

alpha = ['C', 'P', 'Z', 'Y']
n = int(input())
lst = []
for _ in range(n):
	lst.append(list(input().rstrip()))
result = 0

for i in range(n):
	for x in alpha:
		cnt = 0
		for j in range(n):
			if x == lst[i][j]:
				cnt += 1
			else:
				cnt = 0
			result = max(result, cnt)

for j in range(n):
	for x in alpha:
		cnt = 0
		for i in range(n):
			if x == lst[i][j]:
				cnt += 1
			else:
				cnt = 0
			result = max(result, cnt)

for i in range(n - 1):
	for j in range(n):
		lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
		for x in alpha:
			cnt = 0
			for k in range(n):
				if x == lst[k][j]:
					cnt += 1
				else:
					cnt = 0
				result = max(result, cnt)
			cnt = 0
			for k in range(n):
				if x == lst[i][k]:
					cnt += 1
				else:
					cnt = 0
				result = max(result, cnt)
			cnt = 0
			for k in range(n):
				if x == lst[i + 1][k]:
					cnt += 1
				else:
					cnt = 0
				result = max(result, cnt)
		lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]

for j in range(n - 1):
	for i in range(n):
		lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
		for x in alpha:
			cnt = 0
			for k in range(n):
				if x == lst[i][k]:
					cnt += 1
				else:
					cnt = 0
				result = max(result, cnt)
			cnt = 0
			for k in range(n):
				if x == lst[k][j]:
					cnt += 1
				else:
					cnt = 0
				result = max(result, cnt)
			cnt = 0
			for k in range(n):
				if x == lst[k][j + 1]:
					cnt += 1
				else:
					cnt = 0
				result = max(result, cnt)
		lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
print(result)
