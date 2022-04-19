# 2839 py

n = int(input())
result = 0
if n % 5 == 0:
	result = n // 5
	print(result)
max_5 = n // 5
if result == 0:
	for i in range(max_5, -1, -1):
		if (n - i * 5) % 3 == 0:
			j = (n - i * 5) // 3
			result += i + j
			print(result)
			break
if result == 0:
	print("-1")
##
##
## second
n = int(input())
result = 0
while n > 0:
	if n % 5 == 0:
		result += n // 5
		print(result)
		break
	n -= 3
	result += 1
else:
	print(-1)
