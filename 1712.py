# 1712 py

a, b, c = map(int, input().split())
x = 0
if b >= c:
	print(-1)
else:
	x = a // (c - b) + 1
	print(x)
