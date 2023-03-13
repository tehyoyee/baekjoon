# 1041.py
# 23.03.13. 16:18 ~

import sys
input = sys.stdin.readline
from itertools import combinations

def dfs(i, depth, end):
	result = 100000000
	if depth == end:
		return visit[i]
	for ni in adjacent[i]:
		if not visit[ni]:
			visit[ni] += (visit[i] + graph[ni])
			result = min(result, dfs(ni, depth + 1, end))
			visit[ni] = 0
	return result

N = int(input())
graph = list(map(int, input().split()))
lst = [[] for _ in range(3)]
adjacent = [[1, 2, 3, 4], [0, 2, 3, 5], [0, 1, 4, 5], [0, 1, 4, 5], [0, 2, 3, 5], [1, 2, 3, 4]]
one = min(graph)
if N == 1:
	print(sum(graph) - max(graph))
else:
	two = 1000000000
	three = 1000000000
	result = 0
	for i in range(6):
		visit = [0] * 6
		visit[i] = graph[i]
		two = min(two, dfs(i, 1, 2))
		visit = [0] * 6
		visit[i] = graph[i]
		three = min(three, dfs(i, 1, 3))
	result += ((5 * N**2 - 16 * N + 12) * one)
	result += ((8 * N - 12) * two)
	result += (4 * three)
	print(result)

# for i in range(6):
	
# two = 
	# n - 2 * n - 1 * 4 + n - 2 * n - 2   1면 5n2 -16n -8
	# (n-1)*4 (n-2)*4  2면
	# 4   3면
	# 4n2 -12n + 8 + n2 -4n + 4 + 4n -4 + 4n - 8 + 4
	# 5n2 -8n + 4
	# A BCDE F
	# B ACDF E
	# C ABEF D
	# D ABEF C
	# E ACDF B
	# F BCDE A
	
	# A BCDE
	# B CDF
	# C EF
	# D EF
	# E F

	