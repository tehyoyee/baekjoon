import sys
input = sys.stdin.readline

num = []
n = int(input())
for _ in range(n):
	a = int(input())
	if a == 0:
		num.pop()
	else:
		num.append(a)
print(sum(num))