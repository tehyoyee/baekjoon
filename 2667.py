# 2667.py
# 23.05.12. 21:25 ~ 21:34

import sys
input = sys.stdin.readline
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N = int(input())
graph = []
visit = [[False] * N for _ in range(N)]
for _ in range(N):
	graph.append(list(map(int, input().rstrip())))

color = 0
result = []
for i in range(N):
	for j in range(N):
		if graph[i][j] and not visit[i][j]:
			color += 1
			visit[i][j] = True
			q = deque([[i, j]])
			area = 0
			while q:
				ci, cj = q.popleft()
				area += 1
				for k in range(4):
					ni, nj = ci + di[k], cj + dj[k]
					if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] and not visit[ni][nj]:
						visit[ni][nj] = True
						q.append([ni, nj])
			result.append(area)
print(color)
for x in sorted(result):
	print(x)

