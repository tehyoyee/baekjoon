# 14502.py
# 23.07.02.12:01 ~ 12:24

import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy
from itertools import combinations

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(wall, graph, virus):
	result = 0
	for i, j in wall:
		graph[i][j] = 1
	q = deque(virus)
	for i, j, in virus:
		graph[i][j] = 2
	while q:
		ci, cj = q.popleft()
		for k in range(4):
			ni, nj = ci + di[k], cj + dj[k]
			if 0 <= ni < N and 0 <= nj < M and not graph[ni][nj]:
				graph[ni][nj] = 2
				q.append([ni, nj])
	for i in range(N):
		for j in range(M):
			if graph[i][j] == 0:
				result += 1
	return result

N, M = map(int, input().split())
graph = []
virus = []
space = []
result = 0

for i in range(N):
	graph.append(list(map(int, input().split())))
	for j in range(M):
		if graph[i][j] == 2:
			virus.append([i, j])
		if graph[i][j] == 0:
			space.append([i, j])

candi = list(combinations(space, 3))

for wall in candi:
	result = max(result, bfs(wall, deepcopy(graph), virus))
print(result)
# print(candi)




