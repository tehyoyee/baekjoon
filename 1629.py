# 1629.py
# 23.07.10. 00:16 ~ x

a, b, c = map(int, input().split())

def dac(a, b):
	if b == 1:
		return a % c
	div = dac(a, b//2)
	if b % 2 == 0:
		return div * div % c
	else:
		return div * div * a % c

print(dac(a, b))
