# 11653 py

a = int(input())

for i in range (2, 10000000):
	if a == 1:
		break
	while a % i == 0:
		print(i)
		a /= i