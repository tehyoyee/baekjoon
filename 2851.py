# 2581 py

def check_sosu(x):
	if x <= 1:
		return False
	if x == 2:
		return True
	for i in range(2, round(x ** 0.5) + 1):
		if x % i == 0:
			return False
	return True

sum = 0
min_sosu = 0
min_range = int(input())
max_range = int(input())

for x in range(min_range, max_range + 1):
	if check_sosu(x):
		if min_sosu == 0:
			min_sosu = x
		sum += x
if sum != 0:
	print(sum)
	print(min_sosu)
else:
	print("-1")
