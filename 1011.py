# 1011py

t = int(input())
for _ in range(t):
	x, y = map(int, input().split())
	distance = y - x
	comp = 0
	num = 1
	while distance > comp:
		num += 1
		comp += num // 2
	print(num - 1)
