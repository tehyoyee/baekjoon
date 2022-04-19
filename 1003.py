# 1003 py

t = int(input())

for _ in range(t):
	n = int(input())
	
	zero = 1
	one = 0
	tmp = 0
	for _ in range(n):
		tmp = one
		one += zero
		zero = tmp
	print(zero, one)
