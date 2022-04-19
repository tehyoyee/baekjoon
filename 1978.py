# 1978 py

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
result = 0
numbers = list(map(int,input().split()))
for x in numbers:
	if check_sosu(x):
		result += 1
print(result)
