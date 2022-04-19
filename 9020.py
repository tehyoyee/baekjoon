# 9020 py

def check_sosu(x):
	if x <= 1:
		return False
	if x == 2:
		return True
	for i in range(2, round(x ** 0.5) + 1):
		if x % i == 0:
			return False
	return True

t = int(input())
for _ in range(t):
	n = int(input())

	a = n // 2
	b = a
	while a > 0:
		if check_sosu(a) and check_sosu(b):	
			print(a, b)
			break
		else:
			a -= 1
			b += 1