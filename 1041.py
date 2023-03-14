# 1041.py
# 23.03.13. 16:18 ~ 17:18, 09:24 ~ 09:55

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
graph = list(map(int, input().split()))
adjacent = [[1, 2, 3, 4], [0, 2, 3, 5], [0, 1, 4, 5], [0, 1, 4, 5], [0, 2, 3, 5], [1, 2, 3, 4]]

if N == 1:
	print(sum(graph) - max(graph))
else:
	one = min(graph)
	two = 1000000000
	three = 1000000000
	for i in range(6):
		for x in adjacent[i]:
			two = min(graph[i] + graph[x], two)
		for x in list(combinations(adjacent[i], 2)):
			if x[1] in adjacent[x[0]]:
				three = min(graph[i] + graph[x[0]] + graph[x[1]], three)
	result = ((5 * N**2 - 16 * N + 12) * one) + ((8 * N - 12) * two) + (4 * three)
	print(result)
