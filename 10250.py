# 10250 py

t = int(input())

for _ in range(t):
	h, w, n = map(int, input().split())
	floor = n % h
	num = n // h
	if floor == 0:
		floor = h
		num -= 1
	print(f'{floor * 100 + num + 1}')
