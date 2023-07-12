# 1261.py
# 23.04.17. 18:53 ~ x 

import sys
input = sys.stdin.readline
import heapq

di = (0, 0, 1, -1)
dj = (1, -1, 0, 0)

M, N = map(int, input().split())
graph = []
for _ in range(N):
	graph.append(list(map(int, input().rstrip())))
visit = [[False] * M for _ in range(N)]

visit[0][0] = True
q = [(0, 0, 0)]
while q:
	wall, ci, cj = heapq.heappop(q)
	if ci == N - 1 and cj == M - 1:
		break
	for k in range(4):
		ni, nj = ci + di[k], cj + dj[k]
		if 0 <= ni < N and 0 <= nj < M:
			if graph[ni][nj] == 0 and not visit[ni][nj]:
				heapq.heappush(q, (wall, ni, nj))
				visit[ni][nj] = True
			elif not visit[ni][nj]:
				heapq.heappush(q, (wall + 1, ni, nj))
				visit[ni][nj] = True
print(wall)
