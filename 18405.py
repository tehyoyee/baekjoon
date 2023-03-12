# 18405.py
# 23.03.12. 14:58 ~ 15:15

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
graph = [[-1] * (N + 2)]
q = []
for i in range(1, N + 1):
	graph.append([-1] + list(map(int, input().split())) + [-1])
	for j in range(1, N + 1):
		if graph[i][j] > 0:
			q.append([i, j, 0])
graph.append([-1] * (N + 2))
S, X, Y = map(int, input().split())
q.sort(key=lambda x:graph[x[0]][x[1]])
q = deque(q)

while q:
	ci, cj, cnt = q.popleft()
	if cnt == S:
		continue
	for k in range(4):
		ni, nj = ci + di[k], cj + dj[k]
		if graph[ni][nj] == 0:
			graph[ni][nj] = graph[ci][cj]
			q.append([ni, nj, cnt + 1])
print(graph[X][Y])