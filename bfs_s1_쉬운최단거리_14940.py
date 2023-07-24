# 14940.py
# 23.07.24. 23:47 ~

import sys
input = sys.stdin.readline
from collections import deque

di = (0, 0, 1, -1)
dj = (1, -1, 0, 0)

N, M = map(int, input().split())
graph = []
visit = [[0] * M for _ in range(M)]
q = deque([])

for i in range(N):
	graph.append(list(map(int, input().split())))
	for j in range(M):
		if graph[i][j] == 2:
			q.append((i, j))

while q:
	ci, cj = q.popleft()

	for k in range(4):
		ni, nj = ci + di[k], cj + dj[k]
		if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj] and graph[ni][nj] == 1:
			visit[ni][nj] = visit[ci][cj] + 1
			q.append((ni, nj))

for i in range(N):
	for j in range(M):
		if visit[i][j] == 0 and graph[i][j] == 1:
			print(-1, end=' ')
		else:
			print(visit[i][j], end=' ')
	print()



