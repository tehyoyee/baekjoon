# 4948 py

def check_sosu(x):
	if x <= 1:
		return False
	if x == 2:
		return True
	for i in range(2, round(x ** 0.5) + 1):
		if x % i == 0:
			return False
	return True

arr = []

for x in range (1, 123456 * 2 + 1):
	if check_sosu(x):
		arr.append(x)

while(1):
	result = 0
	n = int(input())
	if n == 0:
		break
	for i in arr:
		if n < i <= 2 * n:
			result += 1
	print(result)