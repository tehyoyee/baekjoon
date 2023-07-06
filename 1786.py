# 1786.py
# 23.07.06. 9:48 ~ x

import sys
input = sys.stdin.readline
from collections import deque

T = input().rstrip()
P = input().rstrip()

pi = [0] * len(P)
result = [0, []]
j = 0
for i in range(1, len(P)):
	while j > 0 and P[i] != P[j]:
		j = pi[j - 1]
	if P[i] == P[j]:
		j += 1
		pi[i] = j

j = 0
for i in range(len(T)):
	while j > 0 and T[i] != P[j]:
		j = pi[j - 1]
	if T[i] == P[j]:
		if j == len(P) - 1:
			result[0] += 1
			result[1].append(i - j + 1)
			j = pi[j]
		else:
			j += 1

print(result[0])
print(*result[1])