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

for i in range(0, n - 1):
	for j in range(n):
		lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
		for x in alpha:
			cnt = 0
			for k in range(n):
				if x == lst[i][k]:
					cnt += 1
				else:
					cnt = 0
				result = max(result, cnt)
			if i == n - 2:
				cnt = 0
				for k in range(n):
					if x == lst[n - 1][k]:
						cnt += 1
					else:
						cnt = 0
					result = max(result, cnt)
		lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]

for j in range(0, n - 1):
	for i in range(n):
		lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
		for x in alpha:
			cnt = 0
			for k in range(n):
				if x == lst[k][j]:
					cnt += 1
				else:
					cnt = 0
				result = max(result, cnt)
			if j == n - 2:
				cnt = 0
				for k in range(n):
					if x == lst[k][n - 1]:
						cnt += 1
					else:
						cnt = 0
					result = max(result, cnt)
		lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
print(result)

# for x in alpha:
# 	for i in range(1, n + 1):
# 		flag = 1
# 		cnt = 0
# 		for j in range(1, n + 1):
# 			if lst[i][j] == x:
# 				cnt += 1
# 			elif flag == 1:
# 				if (lst[i + 1][j] == x) or (lst[i - 1][j] == x):
# 					flag = 0
# 					cnt += 1
# 					temp = j
# 			else:
# 				cnt = 0
# 				flag = 1
# 				j = temp
# 			result = max(result, cnt)
# 	for j in range(1, n + 1):
# 		flag = 1
# 		cnt = 0
# 		for i in range(1, n + 1):
# 			if lst[i][j] == x:
# 				cnt += 1
# 			elif flag == 1:
# 				if (lst[i][j - 1] == x) or (lst[i][j + 1] == x):
# 					flag = 0
# 					cnt += 1
# 					temp = i
# 			else:
# 				cnt = 0
# 				flag = 1
# 				i = temp
# 			result = max(result, cnt)	
