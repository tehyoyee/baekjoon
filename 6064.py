# 6064.py
# 23.1.12 22:31 ~ 23:00  29
# 23.1.14 04:09 ~ 05:24  75

# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
# 	m, n, x, y = map(int, input().split())
# 	if m == n:
# 		if x == y:
# 			print(x)
# 		else:
# 			print(-1)
# 		continue
# 	i = x
# 	a = x
# 	while a > n:
# 		a -= n
# 	delta = n - m
# 	lst = []
# 	f = a
# 	while True:
# 		lst.append([i, a])
# 		if a == y:
# 			print(i)
# 			i = 1
# 			break
# 		i += m
# 		a -= delta
# 		if a < 1:
# 			a += n
# 		elif a > n:
# 			a -= n
# 		if f == a:
# 			print(-1)
# 			break
# 	print(lst)
	# while a != m or b != n and i < 100:
	# 	a = a % m + 1
	# 	b = b % n + 1
	# 	i += 1
	# 	if a == x:
	# 		print(i, a, b)
	# 	if a == x and b == y:
	# 		break
# a b 

# 1m  

# 1n	m-n차
# 2n 	2n차



# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
# 	m, n, x, y = map(int, input().split())
# 	if m == n:
# 		if x == y:
# 			print(x)
# 		else:
# 			print(-1)
# 		continue
# 	i = x
# 	a = x
# 	delta = n - m
# 	for _ in range(4 * n // abs(min(m, n))):
# 		if a == y:
# 			print(i)
# 			i = 1
# 			break
# 		i += m
# 		a -= delta
# 		if a < 1:
# 			a += n
# 		elif a > n:
# 			a -= n
# 	if i != 1:
# 		print("-1")

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