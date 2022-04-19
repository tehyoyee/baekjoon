# 1929 py

def check_sosu(x):
	if x <= 1:
		return False
	if x == 2:
		return True
	for i in range(2, round(x ** 0.5) + 1):
		if x % i == 0:
			return False
	return True


a, b = map(int, input().split())

for i in range(a, b + 1):
    if check_sosu(i):
        print(i)