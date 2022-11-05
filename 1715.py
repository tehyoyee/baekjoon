# 1715.py

import sys
input = sys.stdin.readline

result = 0
n = int(input())
lst = []
for _ in range(n):
	lst.append(int(input()))
lst.sort()

while n >= 3:
	if lst[0] > lst[-2] and lst[0] > lst[-1]:
		result += lst[-1] + lst[-2]
		lst.append(lst.pop(-1) + lst.pop(-1))
	elif lst[1] > lst[-1] and lst[1] > lst[0]:
		result += lst[0] + lst[-1]
		lst.append(lst.pop(0) + lst.pop(-1))
	elif lst[-1] > lst[0] and lst[-1] > lst[1]:
		result += lst[0] + lst[1]
		lst.append(lst.pop(0) + lst.pop(0))
	n -= 1
result += sum(lst)
print(result)


1 2 3 4 100 101 102 103
3 4 100 101 102 103 3
100 101 102 103 3 7
100 101 102 103 10
101 102 103 110
103 110 103
110 206