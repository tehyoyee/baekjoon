# 6064.py
# 23.1.12 22:31 ~ 23:00  29
# 23.1.14 04:09 ~ 05:24  75

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	m, n, x, y = map(int, input().split())
	i = x
	a = x % n
	if a == 0:
		a = n
	delta = n - m
	f = a
	while True:
		# print(i, a)
		if a == y:
			print(i)
			break
		i += m
		a -= delta
		a %= n
		if a == 0:
			a = n
		if f == a:
			print(-1)
			break