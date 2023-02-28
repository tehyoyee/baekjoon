# 2011.py
# 23.02.25. 20:21 ~ ?


# 오랜시간
from math import factorial
import sys
sys.setrecursionlimit(10**4)

def f(x):
	a, b, c = x, x, 0
	result = 0
	for i in range(x // 2 + 1):
		result += (factorial(a) // factorial(b) // factorial(c))
		a -= 1
		b -= 2
		c += 1
	return result

def dfs(s, x):
	if x + 1 >= len(code):
		return x
	if code[x:x+2] == "10" or code[x:x+2] == "20":
		if x + 2 < len(code) and code[x+2] == '0':
			print(0)
			exit()
		return x + 2
	if code[x:x+2] == "00":
		print(0)
		exit()
	if 1 <= int(code[x:x+2]) <= 26:
		if x + 2 < len(code) and code[x+2] == '0':
			if int(code[x + 1]) > 2:
				print(0)
				exit()
			else:
				return x + 3
		dp[-1] += 1
		return dfs(s, x + 1)
	elif code[x+1] == '0':
			print(0)
			exit()
	return x + 1

code = input()
if code[0] == '0':
	print(0)
	exit()
dp = [1]
i = 0
while i + 1 < len(code):
	if dp[-1] != 1:
		dp.append(1)
	i = dfs(i, i)
	dp[-1] = f(dp[-1])
result = 1
for x in dp:
	result *= x
	result %= 1000000
print(result)