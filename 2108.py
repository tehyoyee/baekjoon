# 2108.py

import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
	lst.append(int(input()))
lst.sort()
print(round(sum(lst) / n))
print(lst[n // 2])
most = [[1, lst[0]]]
cnt = 1
for i in range(1, n):
	if lst[i - 1] == lst[i]:
		cnt += 1
	else:
		cnt = 1
	if cnt > most[-1][0]:
		most.append([cnt, lst[i]])
	elif cnt == most[-1][0]:
		most[-1].append(lst[i])
if len(most[-1]) == 2:
	print(most[-1][1])
else:
	print(most[-1][2])
print(lst[-1] - lst[0])