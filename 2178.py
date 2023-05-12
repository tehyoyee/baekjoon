# 2178.py
# 23.05.12. 21:16 ~

# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# def dfs(ci, cj):
# 	if ci == N - 1 and cj == M - 1:
# 		return visit[ci][cj]
# 	for k in range(4):
# 		ni, nj = ci + di[k], cj + dj[k]
# 		if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 1 and visit[ni][nj] > visit[ci][cj]:
# 			visit[ni][nj] = visit[ci][cj] + 1
# 			dfs(ni, nj)


# N, M = map(int, input().split())
# graph = []
# visit = [[30000] * M for _ in range(N)]
# for _ in range(N):
# 	graph.append(list(map(int, input().rstrip())))
# visit[0][0] = 1
# dfs(0, 0)
# print(visit[N-1][M-1])

import sys
from collections import deque
input = sys.stdin.readline


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N, M = map(int, input().split())
graph = []
visit = [[0] * M for _ in range(N)]
for _ in range(N):
	graph.append(list(map(int, input().rstrip())))
visit[0][0] = 1
q = deque([[0, 0]])
while q:
	ci, cj = q.popleft()
	steps = visit[ci][cj]
	if ci == N - 1 and cj == M - 1:
		break
	for k in range(4):
		ni, nj = ci + di[k], cj + dj[k]
		if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] and not visit[ni][nj]:
			visit[ni][nj] = steps + 1
			q.append([ni, nj])
print(steps)	
