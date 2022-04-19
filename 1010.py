# 1010 py

import sys
from math import factorial

input = sys.stdin.readline
n = int(input())
for _ in range(n):
	a, b = map(int, input().split())
	if b > a:
		a, b = b, a
	print(factorial(a) // (factorial(b) * factorial(a - b)))
