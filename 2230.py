# 2230.py
# 23.03.14. 15:00 ~ 15:22

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
result = 2000000000
for i in range(N):
	lst.append(int(input()))

lst.sort(reverse=True)
i = 0
j = 1
while i < N and j < N:
	if lst[i] - lst[j] >= M:
		result = min(result, lst[i] - lst[j])
		if i + 1 == j:
			i += 1
			j += 1
		else:
			i += 1
	else:
		j += 1
print(result)