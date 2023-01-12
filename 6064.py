# 6064.py
# 23.1.12 22:31 ~

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	m, n, x, y = map(int, input().split())
	i = 0
	a = 0
	b = 0
	while a != m or b != n and i < 100:
		a = a % m + 1
		b = b % n + 1
		i += 1
		print(i, a, b)
		if a == x and b == y:
			break
	
	if a == m and b == n and a != x and b != y:
		print(-1)
	else:
		print(i)
