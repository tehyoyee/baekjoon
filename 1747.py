# 1747.py
# 23.02.21. 13:22 ~ 14:30

from math import sqrt

def isPrime(x):
	if x < 2:
		return False
	for i in range(2, int(sqrt(x) + 1)):
		if x % i == 0:
			return False
	return True

def isPelin(x):
	x = str(x)
	for i in range(len(x) // 2):
		if x[i] != x[len(x) - 1 - i]:
			return False
	return True

n = int(input())
while True:
	if isPrime(n) and isPelin(n):
		print(n)
		break
	n += 1