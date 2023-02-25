# 2011.py
# 23.02.25. 20:21 ~

def factorial(x):
	if x >= 2:
		return factorial(x - 1) * x
	else:
		return 1

def f(x):
	a, b, c = x, x, 0
	result = 0
	for i in range(x // 2 + 1):
		result += (factorial(a) // factorial(b) // factorial(c))
		result %= 1000000
		a -= 1
		b -= 2
		c += 1
	return result

def dfs(s, x):
	if x + 1 >= len(code):
		dp[s] = f(dp[s])
		return x
	# if x + 2 < len(code) and code[x + 2] == "0":
	# 	if int(code[x + 1]) > 2:
	# 		print(0)
	# 		exit()
	if code[x:x+2] == "10" or code[x:x+2] == "20":
		return x + 2
	if x + 2 < len(code) and code[x + 2] == "0" or not 0 <= int(code[x+1:x+3]) <= 26:
		dp[s] = f(dp[s])
		return x + 3
	# if int(code[x:x+2]) != 10 and int(code[x:x+2]) != 20 and 1 <= int(code[x:x+2]) <= 26:
	if 1 <= int(code[x:x+2]) <= 26:
		dp[s] += 1
		dp[s] = f(dp[s])
		return dfs(s, x + 1)
	return x + 1

code = input()
if len(code) > 1:
	if code[0] == "0" or code[-1] == "0" and 3 <= int(code[-2]):
		print(0)
		exit()
	for i in range(len(code) - 1):
		if code[i + 1] == "0":
			if code[i] == "0" or int(code[i]) > 2:
				print(0)
				exit()
if len(code) == 1 and code[0] == '0':
	print(0)
	exit()
dp = [1] * len(code)
i = 0
while i + 1 < len(code):
	i = dfs(i, i)
result = 1
for x in dp:
	result *= x
	result %= 1000000
# print(dp)
print(result)


# 0
# 답 0

# 1
# 답 1

# 9
# 답 1

# 10
# 답 1

# 20
# 답 1

# 11
# 답 2

# 26
# 답 2

# 27
# 답 1

# 30
# 답 0

# 01
# 답 0

# 99
# 답 1

# 100
# 답 0

# 123
# 답 3

# 101
# 답 1

# 110
# 답 1

# 103
# 답 1

# 000
# 답 0

# 007
# 답 0

# 1010
# 답 1

# 2220
# 답 2

# 2626
# 답 4

# 123456789
# 답 3

# 9876543210