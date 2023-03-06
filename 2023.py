# 2023.py
# 23.03.06. 10:07 ~ 10:29

def isSosu(x):
	if x <= 1:
		return False
	elif x == 2:
		return True
	for i in range(2, x // 2 + 1):
		if x % i == 0:
			return False
	return True

def dfs(num, n):
	if len(str(num)) == n:
		result.append(num)
	else:
		for k in range(0, 10):
			if isSosu(num * 10 + k):
				dfs(num * 10 + k, n)

result = []
n = int(input())
for k in range(2, 10):
	if isSosu(k):
		dfs(k, n)
for x in result:
	print(x)
