# 1806.py
# 23.07.10. 00:37 ~ 02:01

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

s, e = 0, 0
total = 0
l = 0
while total < M:
	total += lst[e]
	l += 1
	e += 1
	if e == N:
		if total >= M:
			while total - lst[s] >= M:
				total -= lst[s]
				l -= 1
				s += 1
			print(l)
		else:
			print(0)
		exit()
	result = l

while s <= e < N:
	total += lst[e]
	l += 1
	e += 1
	while s <= e and total - lst[s] >= M:
		total -= lst[s]
		l -= 1
		s += 1
	result = min(result, l)
print(result)