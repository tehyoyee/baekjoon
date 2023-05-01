# 2042.py
# 23.05.01. 13:03 ~ 13:54

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
num = [0]
lst = [0] * (N + 1)
lst2 = []
for i in range(1, N + 1):
	num.append(int(input()))
	lst[i] = lst[i - 1] + num[i]

for _ in range(M + K):
	order, a, b = map(int, input().split())
	if order == 1:
		lst2.append([a, b - (num[a])])
		num[a] = b
	else:
		result = lst[b] - lst[a-1]
		for key, value in lst2:
			if a <= key and key <= b:
				result += value
		print(result)
