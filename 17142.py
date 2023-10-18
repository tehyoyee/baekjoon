# 17142.py
# 23.10.18. 10:37 ~ 11:22

import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
from copy import deepcopy

di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)

def bfs(q, graphCopy):
	result = 1
	for i, j in q:
		graphCopy[i][j] = 1
	while q:
		ci, cj = q.popleft()
		if not graph[ci][cj] == -2:
			result = max(result, graphCopy[ci][cj])
		for k in range(4):
			ni, nj = ci + di[k], cj + dj[k]
			if 0 <= ni < N and 0 <= nj < N:
				if graphCopy[ni][nj] == 0 or graphCopy[ni][nj] == -2:
					graphCopy[ni][nj] = graphCopy[ci][cj] + 1
					q.append((ni, nj))
	for i in range(N):
		for j in range(N):
			if graphCopy[i][j] == 0:
				return 10000
	return result

N, M = map(int, input().split())
graph = []
viruses = []
result = 10000
for i in range(N):
	graph.append(list(map(int, input().split())))
	for j in range(N):
		if graph[i][j] == 2:
			viruses.append((i, j))
			graph[i][j] = -2
		elif graph[i][j] == 1:
			graph[i][j] = -1

for candi in combinations(viruses, M):
	result = min(result, bfs(deque(list(candi)), deepcopy(graph)))

if result == 10000:
	print(-1)
else:
	print(result - 1)